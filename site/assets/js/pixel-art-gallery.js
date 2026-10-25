/* Tiny Pixel Zoo: draw exact 8×8 and 16×16 codes and filter client-side. */
(function () {
  "use strict";
  const palette = [
    "#ffffff", "#111111", "#096ba6", "#06ad23", "#7b898f",
    "#e8c94f", "#c34635", "#fb8e31", "#ee3edc"
  ];
  document.querySelectorAll("canvas.pixel-zoo-preview[data-pixel-code]").forEach(function (canvas) {
    const code = canvas.dataset.pixelCode;
    const size = Number(canvas.dataset.pixelSize) || 8;
    if ((size !== 8 && size !== 16) || code.length !== size * size || !/^[0-8]+$/.test(code)) {
      canvas.setAttribute("aria-label", "Pixel art preview unavailable");
      return;
    }
    const context = canvas.getContext("2d");
    if (!context) return;
    context.imageSmoothingEnabled = false;
    for (let index = 0; index < code.length; index += 1) {
      context.fillStyle = palette[Number(code[index])];
      context.fillRect(index % size, Math.floor(index / size), 1, 1);
    }
  });
  document.querySelectorAll(".pixel-zoo").forEach(function (gallery) {
    const buttons = Array.from(gallery.querySelectorAll("[data-gallery-filter]"));
    const cards = Array.from(gallery.querySelectorAll(".pixel-zoo-card[data-pixel-size]"));
    const summary = gallery.querySelector(".pixel-zoo-filter-count");
    buttons.forEach(function (button) {
      button.addEventListener("click", function () {
        const filter = button.dataset.galleryFilter;
        if (filter !== "all" && filter !== "8" && filter !== "16") return;
        buttons.forEach(function (item) {
          const on = item === button;
          item.setAttribute("aria-pressed", String(on));
          item.classList.toggle("is-active", on);
        });
        let shown = 0;
        cards.forEach(function (card) {
          const visible = filter === "all" || card.dataset.pixelSize === filter;
          card.hidden = !visible;
          if (visible) shown += 1;
        });
        summary.textContent = "Showing " + shown + " of " + cards.length + " creatures";
      });
    });
  });
})();
