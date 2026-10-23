/* coffeetableviz 8×8 Pixel Art Builder — dependency-free, on-device only. */
(function () {
  "use strict";
  const root = document.getElementById("pixel-art-studio");
  if (!root) return;

  const colours = [
    { name: "White", hex: "#ffffff" },
    { name: "Black", hex: "#111111" },
    { name: "Blue", hex: "#096ba6" },
    { name: "Green", hex: "#06ad23" },
    { name: "Slate", hex: "#7b898f" },
    { name: "Yellow", hex: "#e8c94f" },
    { name: "Red", hex: "#c34635" },
    { name: "Orange", hex: "#fb8e31" },
    { name: "Pink", hex: "#ee3edc" }
  ];
  const storageKey = "coffeetableviz.pixel-art.v1";
  const board = document.getElementById("pixel-grid");
  const preview = document.getElementById("pixel-preview");
  const previewContext = preview.getContext("2d");
  const status = document.getElementById("pixel-status");
  const count = document.getElementById("pixel-count");
  const eraser = document.getElementById("pixel-eraser");
  const undoButton = document.getElementById("pixel-undo");
  const redoButton = document.getElementById("pixel-redo");
  const swatches = Array.from(root.querySelectorAll("[data-colour]"));
  const past = [];
  const future = [];
  let pixels = new Array(64).fill(0);
  let active = 1;
  let focusIndex = 0;
  let stroke = null;

  function validCode(value) {
    return typeof value === "string" && /^[0-8]{64}$/.test(value);
  }
  function decode(code) {
    return code.split("").map(Number);
  }
  function save() {
    try { localStorage.setItem(storageKey, pixels.join("")); } catch (_) { /* Storage may be disabled. */ }
  }
  function restore() {
    const share = window.location.hash.match(/^#art=([0-8]{64})$/);
    if (share) { pixels = decode(share[1]); return; }
    try {
      const saved = localStorage.getItem(storageKey);
      if (validCode(saved)) pixels = decode(saved);
    } catch (_) { /* Storage may be disabled. */ }
  }
  function say(message) { status.textContent = message; }
  function setActive(index) {
    active = index;
    swatches.forEach(function (swatch) {
      const on = Number(swatch.dataset.colour) === active;
      swatch.classList.toggle("is-active", on);
      swatch.setAttribute("aria-pressed", String(on));
    });
    eraser.classList.toggle("is-active", active === 0);
    eraser.setAttribute("aria-pressed", String(active === 0));
  }
  function render() {
    Array.from(board.children).forEach(function (cell, index) {
      const col = colours[pixels[index]];
      cell.style.backgroundColor = col.hex;
      cell.setAttribute("aria-label", "Row " + (Math.floor(index / 8) + 1) + ", column " + ((index % 8) + 1) + ": " + col.name);
    });
    if (previewContext) {
      previewContext.imageSmoothingEnabled = false;
      pixels.forEach(function (colourIndex, index) {
        previewContext.fillStyle = colours[colourIndex].hex;
        previewContext.fillRect(index % 8, Math.floor(index / 8), 1, 1);
      });
    }
    count.textContent = pixels.filter(function (value) { return value !== 0; }).length + " / 64 painted";
    undoButton.disabled = past.length === 0;
    redoButton.disabled = future.length === 0;
  }
  function record(before) {
    if (before.every(function (value, index) { return value === pixels[index]; })) return false;
    past.push(before);
    if (past.length > 50) past.shift();
    future.length = 0;
    save();
    render();
    return true;
  }
  function paint(index, colour) {
    if (pixels[index] === colour) return;
    pixels[index] = colour;
    render();
  }
  function start(index) {
    if (stroke) return;
    const colour = active !== 0 && pixels[index] === active ? 0 : active;
    stroke = { before: pixels.slice(), colour: colour };
    paint(index, colour);
  }
  function finish() {
    if (!stroke) return;
    const changed = record(stroke.before);
    stroke = null;
    if (changed) say("Looking good. Keep going, or save your masterpiece.");
  }
  function changeFocus(index) {
    const children = board.children;
    children[focusIndex].tabIndex = -1;
    focusIndex = index;
    children[focusIndex].tabIndex = 0;
    children[focusIndex].focus({ preventScroll: true });
  }
  for (let index = 0; index < 64; index += 1) {
    const cell = document.createElement("button");
    cell.type = "button";
    cell.className = "pixel-cell";
    cell.dataset.index = String(index);
    cell.tabIndex = index === 0 ? 0 : -1;
    board.appendChild(cell);
  }
  restore();
  render();
  setActive(active);

  swatches.forEach(function (swatch) {
    swatch.addEventListener("click", function () {
      setActive(Number(swatch.dataset.colour));
      say(colours[active].name + " selected.");
    });
  });
  eraser.addEventListener("click", function () {
    setActive(0);
    say("Eraser selected. Tap or drag to turn squares white.");
  });
  board.addEventListener("focusin", function (event) {
    const cell = event.target.closest(".pixel-cell");
    if (!cell) return;
    const index = Number(cell.dataset.index);
    if (index !== focusIndex) {
      board.children[focusIndex].tabIndex = -1;
      focusIndex = index;
      cell.tabIndex = 0;
    }
  });
  board.addEventListener("pointerdown", function (event) {
    const cell = event.target.closest(".pixel-cell");
    if (!cell || (event.pointerType === "mouse" && event.button !== 0)) return;
    event.preventDefault();
    if (stroke) return;
    const index = Number(cell.dataset.index);
    changeFocus(index);
    start(index);
    try { board.setPointerCapture(event.pointerId); } catch (_) { /* Capture is optional. */ }
  });
  board.addEventListener("pointermove", function (event) {
    if (!stroke) return;
    const underPointer = document.elementFromPoint(event.clientX, event.clientY);
    const cell = underPointer && underPointer.closest(".pixel-cell");
    if (cell && board.contains(cell)) paint(Number(cell.dataset.index), stroke.colour);
  });
  board.addEventListener("pointerup", finish);
  board.addEventListener("pointercancel", finish);
  window.addEventListener("pointerup", finish);
  // Keyboard activation emits a click with detail=0. Pointer actions are handled above.
  board.addEventListener("click", function (event) {
    if (event.detail !== 0) return;
    const cell = event.target.closest(".pixel-cell");
    if (!cell) return;
    start(Number(cell.dataset.index));
    finish();
  });
  board.addEventListener("keydown", function (event) {
    const cell = event.target.closest(".pixel-cell");
    if (!cell) return;
    const index = Number(cell.dataset.index);
    let next = index;
    if (event.key === "ArrowRight") next = Math.min(63, index + 1);
    else if (event.key === "ArrowLeft") next = Math.max(0, index - 1);
    else if (event.key === "ArrowDown") next = Math.min(63, index + 8);
    else if (event.key === "ArrowUp") next = Math.max(0, index - 8);
    else if (event.key === "Home") next = index - (index % 8);
    else if (event.key === "End") next = index + (7 - (index % 8));
    else return;
    event.preventDefault();
    changeFocus(next);
  });

  undoButton.addEventListener("click", function () {
    if (!past.length) return;
    future.push(pixels.slice());
    pixels = past.pop();
    save();
    render();
    say("Last change undone.");
  });
  redoButton.addEventListener("click", function () {
    if (!future.length) return;
    past.push(pixels.slice());
    pixels = future.pop();
    save();
    render();
    say("Change restored.");
  });
  document.getElementById("pixel-reset").addEventListener("click", function () {
    const before = pixels.slice();
    pixels.fill(0);
    if (record(before)) say("Canvas cleared. Undo will bring it back.");
    else say("Your canvas is already clear.");
  });
  const presets = {
    heart: [
      "00000000", "06600660", "66666666", "66666666",
      "06666660", "00666600", "00066000", "00000000"
    ].join(""),
    smile: [
      "00000000", "05555550", "55000055", "50100105",
      "50000005", "50111105", "55000055", "05555550"
    ].join("")
  };
  root.querySelectorAll("[data-preset]").forEach(function (button) {
    button.addEventListener("click", function () {
      const code = presets[button.dataset.preset];
      if (!validCode(code)) return;
      const before = pixels.slice();
      pixels = decode(code);
      if (record(before)) say("A little " + button.dataset.preset + ". Now make it your own.");
    });
  });
  const exportPanel = document.getElementById("pixel-export-panel");
  const exportPreview = document.getElementById("pixel-export-preview");
  const exportLink = document.getElementById("pixel-export-link");
  const exportName = "coffeetableviz-8x8-pixel-art.png";

  function makePng() {
    const canvas = document.createElement("canvas");
    canvas.width = 1024;
    canvas.height = 1024;
    const context = canvas.getContext("2d");
    if (!context) throw new Error("Canvas unavailable");
    context.imageSmoothingEnabled = false;
    pixels.forEach(function (index, position) {
      context.fillStyle = colours[index].hex;
      context.fillRect((position % 8) * 128, Math.floor(position / 8) * 128, 128, 128);
    });
    const dataUrl = canvas.toDataURL("image/png");
    if (!dataUrl.startsWith("data:image/png;base64,")) throw new Error("PNG encoding failed");
    return dataUrl;
  }

  document.getElementById("pixel-download").addEventListener("click", function () {
    let dataUrl;
    try { dataUrl = makePng(); }
    catch (_) { say("Sorry, this browser couldn't create the PNG. Your drawing is still here."); return; }

    // Visible fallback: mobile browsers and in-app webviews can ignore scripted downloads.
    exportPreview.src = dataUrl;
    exportLink.href = dataUrl;
    exportLink.download = exportName;
    exportPanel.hidden = false;
    const touch = typeof window.matchMedia === "function" &&
      window.matchMedia("(pointer: coarse)").matches;

    // Invoke share synchronously from the tap (transient user activation is required).
    if (touch && typeof navigator.share === "function" &&
        typeof navigator.canShare === "function" && typeof File === "function") {
      try {
        const binary = atob(dataUrl.split(",")[1]);
        const bytes = Uint8Array.from(binary, function (c) { return c.charCodeAt(0); });
        const png = new File([bytes], exportName, { type: "image/png" });
        if (navigator.canShare({ files: [png] })) {
          const sharing = navigator.share({ files: [png], title: "8×8 pixel art" });
          say("Choose Save Image or Save to Files in the Share sheet. The preview below is a backup.");
          Promise.resolve(sharing).then(function () {
            say("Share sheet closed. Your PNG is still available below.");
          }, function (error) {
            say(error && error.name === "AbortError"
              ? "Sharing cancelled. You can save from the preview below."
              : "Sharing wasn't available. You can save from the preview below.");
          });
          return;
        }
      } catch (_) { /* Fall back to the visible image and download link. */ }
    }

    if (touch) {
      say("PNG ready. Touch and hold the preview below to save it, or try Download PNG.");
    } else {
      // Keep the existing one-click desktop download; leave a clickable backup.
      try {
        exportLink.click();
        say("PNG prepared. If it didn't download, use the link or image below.");
      } catch (_) {
        say("PNG prepared. Use Download PNG below.");
      }
    }
  });

  document.getElementById("pixel-share").addEventListener("click", async function () {
    const shareUrl = window.location.origin + window.location.pathname + "#art=" + pixels.join("");
    try {
      if (!navigator.clipboard || !navigator.clipboard.writeText) throw new Error("Clipboard unavailable");
      await navigator.clipboard.writeText(shareUrl);
      say("Link copied. It opens your design, colours and all.");
    } catch (_) {
      const input = document.createElement("textarea");
      input.value = shareUrl;
      input.setAttribute("readonly", "");
      input.style.cssText = "position:fixed;left:-9999px;top:0";
      document.body.appendChild(input);
      input.select();
      let copied = false;
      try { copied = document.execCommand("copy"); } catch (_) { /* Not supported. */ }
      input.remove();
      if (copied) say("Link copied. It opens your design, colours and all.");
      else {
        window.location.hash = "art=" + pixels.join("");
        say("The share link is now in your address bar, ready to copy.");
      }
    }
  });
})();
