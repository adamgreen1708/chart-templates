/* Tiny Pixel Zoo: render the same 8x8, 0–8 colour codes as the Pixel Art Builder. */
(function () {
  "use strict";
  const palette = [
    "#ffffff", "#111111", "#096ba6", "#06ad23", "#7b898f",
    "#e8c94f", "#c34635", "#fb8e31", "#ee3edc"
  ];
  const validCode = /^[0-8]{64}$/;

  document.querySelectorAll("canvas.pixel-zoo-preview[data-pixel-code]").forEach(function (canvas) {
    const code = canvas.dataset.pixelCode;
    if (!validCode.test(code)) {
      canvas.setAttribute("aria-label", "Pixel art preview unavailable");
      return;
    }
    const context = canvas.getContext("2d");
    if (!context) return;
    context.imageSmoothingEnabled = false;
    for (let index = 0; index < code.length; index += 1) {
      context.fillStyle = palette[Number(code[index])];
      context.fillRect(index % 8, Math.floor(index / 8), 1, 1);
    }
  });
})();
