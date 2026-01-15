document.querySelector(".search-box")?.addEventListener("input", function () {
  const term = this.value.toLowerCase();
  document.querySelectorAll(".feedback-card").forEach(card => {
    card.style.display = card.innerText.toLowerCase().includes(term)
      ? "block"
      : "none";
  });
});
