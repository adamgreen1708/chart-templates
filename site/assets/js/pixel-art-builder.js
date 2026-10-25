/* coffeetableviz Pixel Art Studio: 8×8 Classic and 16×16 Detail.
 * Both canvases are saved locally. Legacy #art=64-digit links remain valid.
 * 16×16 links use #size=16&art=256-digits. No network or external libraries.
 */
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
  const storageKeys = { 8: "coffeetableviz.pixel-art.v1", 16: "coffeetableviz.pixel-art.16.v1" };
  const boards = {
    8: { pixels: new Array(64).fill(0), past: [], future: [] },
    16: { pixels: new Array(256).fill(0), past: [], future: [] }
  };
  const board = document.getElementById("pixel-grid");
  const viewport = document.getElementById("pixel-grid-viewport");
  const preview = document.getElementById("pixel-preview");
  const count = document.getElementById("pixel-count");
  const status = document.getElementById("pixel-status");
  const eraser = document.getElementById("pixel-eraser");
  const undoButton = document.getElementById("pixel-undo");
  const redoButton = document.getElementById("pixel-redo");
  const zoomTools = document.getElementById("pixel-zoom-tools");
  const zoomButton = document.getElementById("pixel-zoom");
  const panButton = document.getElementById("pixel-pan");
  const exportPanel = document.getElementById("pixel-export-panel");
  const exportPreview = document.getElementById("pixel-export-preview");
  const exportLink = document.getElementById("pixel-export-link");
  const swatches = Array.from(root.querySelectorAll("[data-colour]"));
  const sizeButtons = Array.from(root.querySelectorAll("[data-pixel-size]"));
  const presetButtons = Array.from(root.querySelectorAll("[data-preset]"));
  let size = 8;
  let active = 1;
  let focusIndex = 0;
  let stroke = null;
  let zoomed = false;
  let panMode = false;

  function current() { return boards[size]; }
  function validCode(code, dimension) {
    return typeof code === "string" &&
      (dimension === 8 || dimension === 16) &&
      code.length === dimension * dimension &&
      /^[0-8]+$/.test(code);
  }
  function parseHash(fragment) {
    const legacy = /^#art=([0-8]{64})$/.exec(fragment);
    if (legacy) return { size: 8, code: legacy[1] };
    const detailed = /^#size=16&art=([0-8]{256})$/.exec(fragment);
    if (detailed) return { size: 16, code: detailed[1] };
    return null;
  }
  function fragmentFor(dimension, code) {
    return dimension === 8 ? "#art=" + code : "#size=16&art=" + code;
  }
  function say(message) { status.textContent = message; }
  function restoreSaved() {
    [8, 16].forEach(function (dimension) {
      try {
        const saved = localStorage.getItem(storageKeys[dimension]);
        if (validCode(saved, dimension)) {
          boards[dimension].pixels = saved.split("").map(Number);
        }
      } catch (_) { /* Storage may be disabled. */ }
    });
    const linked = parseHash(window.location.hash);
    if (linked) {
      size = linked.size;
      boards[size].pixels = linked.code.split("").map(Number);
    }
  }
  function save() {
    try { localStorage.setItem(storageKeys[size], current().pixels.join("")); }
    catch (_) { /* Storage may be disabled. */ }
  }
  function clearExport() { exportPanel.hidden = true; }
  function selectColour(index) {
    active = index;
    swatches.forEach(function (swatch) {
      const selected = Number(swatch.dataset.colour) === active;
      swatch.classList.toggle("is-active", selected);
      swatch.setAttribute("aria-pressed", String(selected));
    });
    const erasing = active === 0;
    eraser.classList.toggle("is-active", erasing);
    eraser.setAttribute("aria-pressed", String(erasing));
  }
  function buildGrid() {
    board.replaceChildren();
    board.style.setProperty("--pixel-dimension", String(size));
    board.setAttribute("aria-label", size + " by " + size + " paintable grid");
    preview.width = size;
    preview.height = size;
    focusIndex = 0;
    const fragment = document.createDocumentFragment();
    for (let index = 0; index < size * size; index += 1) {
      const cell = document.createElement("button");
      cell.type = "button";
      cell.className = "pixel-cell";
      cell.dataset.index = String(index);
      cell.tabIndex = index === 0 ? 0 : -1;
      fragment.appendChild(cell);
    }
    board.appendChild(fragment);
  }
  function render() {
    const st = current();
    Array.from(board.children).forEach(function (cell, index) {
      const ink = colours[st.pixels[index]];
      cell.style.backgroundColor = ink.hex;
      cell.setAttribute("aria-label", "Row " + (Math.floor(index / size) + 1) +
        ", column " + ((index % size) + 1) + ": " + ink.name);
    });
    const context = preview.getContext("2d");
    if (context) {
      context.imageSmoothingEnabled = false;
      st.pixels.forEach(function (ink, index) {
        context.fillStyle = colours[ink].hex;
        context.fillRect(index % size, Math.floor(index / size), 1, 1);
      });
    }
    count.textContent = st.pixels.filter(function (ink) { return ink !== 0; }).length +
      " / " + (size * size) + " painted";
    undoButton.disabled = st.past.length === 0;
    redoButton.disabled = st.future.length === 0;
    sizeButtons.forEach(function (button) {
      const selected = Number(button.dataset.pixelSize) === size;
      button.classList.toggle("is-active", selected);
      button.setAttribute("aria-pressed", String(selected));
    });
    zoomTools.hidden = size !== 16;
    updateZoom();
  }
  function updateZoom() {
    const on = size === 16 && zoomed;
    board.classList.toggle("is-zoomed", on);
    board.classList.toggle("is-panning", on && panMode);
    viewport.classList.toggle("is-zoomed", on);
    zoomButton.setAttribute("aria-pressed", String(on));
    zoomButton.textContent = on ? "Fit grid" : "Zoom 2×";
    panButton.disabled = !on;
    panButton.setAttribute("aria-pressed", String(on && panMode));
    panButton.textContent = on && panMode ? "Move view: ON" : "Move view: OFF";
  }
  function record(before) {
    const st = current();
    if (before.every(function (value, index) { return value === st.pixels[index]; })) return false;
    st.past.push(before);
    if (st.past.length > 50) st.past.shift();
    st.future.length = 0;
    save();
    clearExport();
    render();
    return true;
  }
  function changeSize(nextSize, manual) {
    if (nextSize !== 8 && nextSize !== 16) return;
    finish();
    if (manual && window.history && typeof window.history.replaceState === "function") {
      window.history.replaceState(null, "", window.location.pathname + window.location.search);
    }
    if (size !== nextSize) {
      size = nextSize;
      stroke = null;
      zoomed = false;
      panMode = false;
      buildGrid();
    }
    render();
    if (manual) say(size + "×" + size + " canvas selected. Your other drawing is saved separately.");
  }
  function setPixel(index, ink) {
    const st = current();
    if (st.pixels[index] !== ink) {
      st.pixels[index] = ink;
      render();
    }
  }
  function start(index) {
    if (stroke || (zoomed && panMode)) return;
    const st = current();
    const ink = active !== 0 && st.pixels[index] === active ? 0 : active;
    stroke = { before: st.pixels.slice(), ink: ink };
    setPixel(index, ink);
  }
  function finish() {
    if (!stroke) return;
    const changed = record(stroke.before);
    stroke = null;
    if (changed) say("Looking good. Keep going, or save your masterpiece.");
  }
  function focusCell(index) {
    board.children[focusIndex].tabIndex = -1;
    focusIndex = index;
    board.children[index].tabIndex = 0;
    board.children[index].focus({ preventScroll: true });
  }
  function applyLinkedArt(info, scroll) {
    if (!info || !validCode(info.code, info.size)) return;
    if (size !== info.size) changeSize(info.size, false);
    const st = current();
    const before = st.pixels.slice();
    st.pixels = info.code.split("").map(Number);
    stroke = null;
    if (record(before)) say("Design loaded. Remix it — Undo restores your previous drawing.");
    else { save(); render(); say("This design is on the canvas and ready to remix."); }
    if (scroll && typeof root.scrollIntoView === "function") {
      root.scrollIntoView({ behavior: "smooth", block: "start" });
    }
  }

  restoreSaved();
  buildGrid();
  render();
  selectColour(active);

  sizeButtons.forEach(function (button) {
    button.addEventListener("click", function () { changeSize(Number(button.dataset.pixelSize), true); });
  });
  swatches.forEach(function (swatch) {
    swatch.addEventListener("click", function () {
      selectColour(Number(swatch.dataset.colour));
      say(colours[active].name + " selected.");
    });
  });
  eraser.addEventListener("click", function () { selectColour(0); say("Eraser selected."); });

  zoomButton.addEventListener("click", function () {
    if (size !== 16) return;
    zoomed = !zoomed;
    panMode = zoomed;
    updateZoom();
    if (!zoomed) { viewport.scrollLeft = 0; viewport.scrollTop = 0; }
    say(zoomed ? "Zoomed in. Swipe to move the view, then turn Move view OFF to paint." :
      "Whole canvas fits in view. Tap or drag to paint.");
  });
  panButton.addEventListener("click", function () {
    if (!zoomed || size !== 16) return;
    panMode = !panMode;
    updateZoom();
    say(panMode ? "Move view ON: swipe to navigate without painting." :
      "Move view OFF: touch a square to paint.");
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
    if (zoomed && panMode) return; // Allow native scrolling of the zoomed grid.
    event.preventDefault();
    if (stroke) return;
    focusCell(Number(cell.dataset.index));
    start(Number(cell.dataset.index));
    try { board.setPointerCapture(event.pointerId); } catch (_) { /* Optional. */ }
  });
  board.addEventListener("pointermove", function (event) {
    if (!stroke) return;
    const pointed = document.elementFromPoint(event.clientX, event.clientY);
    const cell = pointed && pointed.closest(".pixel-cell");
    if (cell && board.contains(cell)) setPixel(Number(cell.dataset.index), stroke.ink);
  });
  board.addEventListener("pointerup", finish);
  board.addEventListener("pointercancel", finish);
  window.addEventListener("pointerup", finish);
  board.addEventListener("click", function (event) {
    if (event.detail !== 0) return; // Keyboard activation only.
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
    if (event.key === "ArrowRight") next = Math.min(size * size - 1, index + 1);
    else if (event.key === "ArrowLeft") next = Math.max(0, index - 1);
    else if (event.key === "ArrowDown") next = Math.min(size * size - 1, index + size);
    else if (event.key === "ArrowUp") next = Math.max(0, index - size);
    else if (event.key === "Home") next = index - (index % size);
    else if (event.key === "End") next = index + (size - 1 - (index % size));
    else return;
    event.preventDefault();
    focusCell(next);
  });

  undoButton.addEventListener("click", function () {
    const st = current();
    if (!st.past.length) return;
    st.future.push(st.pixels.slice());
    st.pixels = st.past.pop();
    save(); clearExport(); render(); say("Last change undone.");
  });
  redoButton.addEventListener("click", function () {
    const st = current();
    if (!st.future.length) return;
    st.past.push(st.pixels.slice());
    st.pixels = st.future.pop();
    save(); clearExport(); render(); say("Change restored.");
  });
  document.getElementById("pixel-reset").addEventListener("click", function () {
    const st = current();
    const before = st.pixels.slice();
    st.pixels.fill(0);
    if (record(before)) say("Canvas cleared. Undo can bring it back.");
    else say("Your canvas is already clear.");
  });
  const presets = {
    heart: ["00000000","06600660","66666666","66666666","06666660","00666600","00066000","00000000"].join(""),
    smile: ["00000000","05555550","55000055","50100105","50000005","50111105","55000055","05555550"].join("")
  };
  function presetCode(name) {
    const source = presets[name];
    if (!source) return null;
    if (size === 8) return source;
    let result = "";
    for (let row = 0; row < 8; row += 1) {
      let expanded = "";
      for (let col = 0; col < 8; col += 1) {
        const digit = source[row * 8 + col];
        expanded += digit + digit;
      }
      result += expanded + expanded;
    }
    return result;
  }
  presetButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      const code = presetCode(button.dataset.preset);
      if (!validCode(code, size)) return;
      applyLinkedArt({ size: size, code: code }, false);
      say("A little " + button.dataset.preset + ". Now make it your own.");
    });
  });

  function makePng() {
    const canvas = document.createElement("canvas");
    canvas.width = 1024;
    canvas.height = 1024;
    const context = canvas.getContext("2d");
    if (!context) throw new Error("Canvas unavailable");
    context.imageSmoothingEnabled = false;
    const side = 1024 / size;
    current().pixels.forEach(function (ink, index) {
      context.fillStyle = colours[ink].hex;
      context.fillRect((index % size) * side, Math.floor(index / size) * side, side, side);
    });
    const dataUrl = canvas.toDataURL("image/png");
    if (!dataUrl.startsWith("data:image/png;base64,")) throw new Error("PNG encoding failed");
    return dataUrl;
  }
  document.getElementById("pixel-download").addEventListener("click", function () {
    let dataUrl;
    try { dataUrl = makePng(); }
    catch (_) { say("Sorry, this browser couldn't create the PNG. Your drawing is still here."); return; }
    const fileName = "coffeetableviz-" + size + "x" + size + "-pixel-art.png";
    exportPreview.src = dataUrl;
    exportLink.href = dataUrl;
    exportLink.download = fileName;
    exportPanel.hidden = false;
    const touch = typeof window.matchMedia === "function" &&
      window.matchMedia("(pointer: coarse)").matches;
    if (touch && typeof navigator.share === "function" &&
        typeof navigator.canShare === "function" && typeof File === "function") {
      try {
        const binary = atob(dataUrl.split(",")[1]);
        const bytes = Uint8Array.from(binary, function (c) { return c.charCodeAt(0); });
        const png = new File([bytes], fileName, { type: "image/png" });
        if (navigator.canShare({ files: [png] })) {
          const sharing = navigator.share({ files: [png], title: size + "×" + size + " pixel art" });
          say("Choose Save Image or Save to Files in the Share sheet. The preview is a backup.");
          Promise.resolve(sharing).then(function () {
            say("Share sheet closed. Your PNG is still available below.");
          }, function (error) {
            say(error && error.name === "AbortError" ?
              "Sharing cancelled. You can save from the preview below." :
              "Sharing wasn't available. You can save from the preview below.");
          });
          return;
        }
      } catch (_) { /* Use the preview fallback. */ }
    }
    if (touch) {
      say("PNG ready. Touch and hold the preview to save it, or try Download PNG.");
    } else {
      try { exportLink.click(); say("PNG prepared. If it didn't download, use the link below."); }
      catch (_) { say("PNG prepared. Use Download PNG below."); }
    }
  });

  window.addEventListener("hashchange", function () {
    const info = parseHash(window.location.hash);
    if (info) applyLinkedArt(info, true);
  });
  const gallery = document.getElementById("tiny-pixel-zoo");
  if (gallery) gallery.addEventListener("click", function (event) {
    const link = event.target.closest("a.pixel-zoo-open");
    if (!link || !gallery.contains(link)) return;
    const href = link.getAttribute("href") || "";
    const fragment = href.indexOf("#") >= 0 ? href.slice(href.indexOf("#")) : "";
    const info = parseHash(fragment);
    if (!info) return;
    event.preventDefault();
    applyLinkedArt(info, true);
    window.location.hash = fragment;
  });

  document.getElementById("pixel-share").addEventListener("click", async function () {
    const shared = fragmentFor(size, current().pixels.join(""));
    const url = window.location.origin + window.location.pathname + shared;
    try {
      if (!navigator.clipboard || !navigator.clipboard.writeText) throw new Error("Clipboard unavailable");
      await navigator.clipboard.writeText(url);
      say(size + "×" + size + " link copied. It will open your exact design.");
    } catch (_) {
      const input = document.createElement("textarea");
      input.value = url;
      input.setAttribute("readonly", "");
      input.style.cssText = "position:fixed;left:-9999px;top:0";
      document.body.appendChild(input);
      input.select();
      let copied = false;
      try { copied = document.execCommand("copy"); } catch (_) { /* Unsupported. */ }
      input.remove();
      if (copied) say("Design link copied.");
      else {
        window.location.hash = shared;
        say("The share link is in your address bar, ready to copy.");
      }
    }
  });
})();
