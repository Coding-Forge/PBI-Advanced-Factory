document.querySelectorAll(".copy").forEach((button) => {
  button.addEventListener("click", async () => {
    const text = document.getElementById(button.dataset.copy).textContent;
    await navigator.clipboard.writeText(text);
    const oldText = button.textContent;
    button.textContent = "Copied";
    setTimeout(() => button.textContent = oldText, 1200);
  });
});

document.querySelectorAll("[data-progress]").forEach((box) => {
  const key = "pbi-advanced-factory:" + box.dataset.progress;
  const checks = [...box.querySelectorAll("input")];
  let saved = [];
  try { saved = JSON.parse(localStorage.getItem(key) || "[]"); } catch {}
  checks.forEach((check, index) => {
    check.checked = !!saved[index];
    check.addEventListener("change", update);
  });
  function update() {
    const state = checks.map((check) => check.checked);
    localStorage.setItem(key, JSON.stringify(state));
    const done = state.filter(Boolean).length;
    box.querySelector(".count").textContent = done;
    box.querySelector(".bar").style.width = (checks.length ? done / checks.length * 100 : 0) + "%";
  }
  update();
});