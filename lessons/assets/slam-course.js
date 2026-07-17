window.lessonKit = {
  answer(button, targetId) {
    const target = document.getElementById(targetId);
    if (!target) return;
    const correct = button.dataset.correct === "yes";
    const explanation = button.dataset.explanation || "";
    target.className = "quiz-feedback show " + (correct ? "correct" : "wrong");
    target.innerHTML = (correct ? "<strong>回答到位：</strong>" : "<strong>再想一步：</strong>") + explanation;
  },
  openTab(group, id) {
    document.querySelectorAll(`[data-tab-panel="${group}"]`).forEach((panel) => {
      panel.classList.toggle("active", panel.dataset.tabId === id);
    });
    document.querySelectorAll(`[data-tab-button="${group}"]`).forEach((button) => {
      const active = button.dataset.tabId === id;
      const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      button.style.background = active
        ? (isDark ? '#E8A88C' : '#cc785c')
        : (isDark ? 'rgba(34,34,58,0.6)' : '#fff7f3');
      button.style.color = active
        ? (isDark ? '#1A1A2E' : '#ffffff')
        : (isDark ? '#C8C8D0' : '#7d4c3b');
    });
  }
};
document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".tab-group").forEach((group) => {
    const first = group.querySelector("[data-tab-button]");
    if (first) {
      window.lessonKit.openTab(first.dataset.tabButton, first.dataset.tabId);
    }
  });
});
