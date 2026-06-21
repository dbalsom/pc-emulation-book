(function () {
    "use strict";

    function ensureModal() {
        var modal = document.getElementById("imageModal");
        var image = document.getElementById("modalImg");

        if (modal && image) {
            return { modal: modal, image: image };
        }

        modal = document.createElement("div");
        modal.id = "imageModal";
        modal.setAttribute("role", "dialog");
        modal.setAttribute("aria-modal", "true");
        modal.setAttribute("aria-label", "Image preview");

        image = document.createElement("img");
        image.id = "modalImg";
        image.alt = "";

        var closeButton = document.createElement("button");
        closeButton.className = "image-modal-close";
        closeButton.type = "button";
        closeButton.setAttribute("aria-label", "Close image preview");
        closeButton.innerHTML = "&times;";

        modal.addEventListener("click", function () {
            window.closeModal();
        });

        image.addEventListener("click", function (event) {
            event.stopPropagation();
        });

        closeButton.addEventListener("click", function (event) {
            event.stopPropagation();
            window.closeModal();
        });

        modal.appendChild(image);
        modal.appendChild(closeButton);
        document.body.appendChild(modal);

        return { modal: modal, image: image };
    }

    window.openModal = function (sourceImage) {
        var parts = ensureModal();

        parts.image.src = sourceImage.currentSrc || sourceImage.src;
        parts.image.alt = sourceImage.alt || "";
        parts.modal.classList.add("is-open");
    };

    window.closeModal = function () {
        var modal = document.getElementById("imageModal");
        var image = document.getElementById("modalImg");

        if (!modal) {
            return;
        }

        modal.classList.remove("is-open");

        if (image) {
            image.removeAttribute("src");
            image.alt = "";
        }
    };

    document.addEventListener("keydown", function (event) {
        if (event.key === "Escape") {
            window.closeModal();
        }
    });

    document.addEventListener("DOMContentLoaded", function () {
        ensureModal();
    });
})();
