// Power BI Advanced Factory - Jeopardy engine
// Expects a global JEOPARDY_DATA object defined by the host page before this script runs:
//   window.JEOPARDY_DATA = {
//     boardId: "lab01",                 // unique key for localStorage
//     title: "Module 1: Advanced Semantic Modeling",
//     categories: [
//       { name: "Star Schema Basics", clues: [ { value: 100, question: "...", answer: "..." }, ... 5 clues ] },
//       ... 5-6 categories
//     ]
//   };
(() => {
  const data = window.JEOPARDY_DATA;
  if (!data) { console.error("JEOPARDY_DATA missing"); return; }

  const storageKey = "pbi-advanced-factory:jeopardy:" + data.boardId;
  const root = document.getElementById("jeopardy-root");
  if (!root) { console.error("#jeopardy-root not found"); return; }

  const defaultState = {
    teams: [
      { name: "Team 1", score: 0 },
      { name: "Team 2", score: 0 },
    ],
    used: {}, // "catIndex-clueIndex" -> true
  };

  let state = loadState();

  function loadState() {
    try {
      const saved = JSON.parse(localStorage.getItem(storageKey) || "null");
      if (saved && Array.isArray(saved.teams)) return saved;
    } catch {}
    return structuredClone(defaultState);
  }

  function saveState() {
    localStorage.setItem(storageKey, JSON.stringify(state));
  }

  function clueKey(ci, qi) { return ci + "-" + qi; }

  function render() {
    const totalClues = data.categories.reduce((sum, c) => sum + c.clues.length, 0);
    const usedCount = Object.keys(state.used).length;
    const allUsed = usedCount >= totalClues;

    root.innerHTML = `
      <div class="jp-title-block">
        <div class="jp-eyebrow">Jeopardy review</div>
        <h1 class="jp-title">${escapeHtml(data.title)}</h1>
        <p class="jp-sub">${usedCount} of ${totalClues} clues played</p>
      </div>
      <div class="jp-board">
        <div class="jp-board-inner">
          <div class="jp-cat-row" style="grid-template-columns: repeat(${data.categories.length}, 1fr);">
            ${data.categories.map(c => `<div class="jp-cat">${escapeHtml(c.name)}</div>`).join("")}
          </div>
          ${renderClueRows()}
        </div>
      </div>
      <div class="jp-controls">
        <button class="jp-btn" id="jp-add-team">+ Add team</button>
        <button class="jp-btn" id="jp-reset-board">Reset board</button>
        <button class="jp-btn jp-btn--primary" id="jp-end-game">End game / show winner</button>
      </div>
      <div class="jp-teams" id="jp-teams"></div>
      ${allUsed ? `<div class="jp-final"><h2>All clues played</h2><p>Click "End game / show winner" to reveal the final standings.</p></div>` : ""}
    `;

    renderTeams();
    attachBoardHandlers();
    attachControlHandlers();
  }

  function renderClueRows() {
    const maxClues = Math.max(...data.categories.map(c => c.clues.length));
    let rows = "";
    for (let qi = 0; qi < maxClues; qi++) {
      rows += `<div class="jp-clue-row" style="grid-template-columns: repeat(${data.categories.length}, 1fr);">`;
      data.categories.forEach((cat, ci) => {
        const clue = cat.clues[qi];
        if (!clue) { rows += `<div></div>`; return; }
        const used = !!state.used[clueKey(ci, qi)];
        rows += `<div class="jp-tile ${used ? "jp-tile--used" : ""}" data-ci="${ci}" data-qi="${qi}">${used ? "" : "$" + clue.value}</div>`;
      });
      rows += `</div>`;
    }
    return rows;
  }

  function renderTeams() {
    const wrap = document.getElementById("jp-teams");
    wrap.innerHTML = state.teams.map((team, ti) => `
      <div class="jp-team" data-ti="${ti}">
        <input class="jp-team-name" value="${escapeAttr(team.name)}" data-ti="${ti}">
        <div class="jp-team-score">${team.score}</div>
        <div class="jp-team-actions">
          <button class="jp-team-plus" data-ti="${ti}">+100</button>
          <button class="jp-team-minus" data-ti="${ti}">-100</button>
        </div>
        <button class="jp-team-remove" data-ti="${ti}">Remove team</button>
      </div>
    `).join("");

    wrap.querySelectorAll(".jp-team-name").forEach(input => {
      input.addEventListener("change", () => {
        state.teams[Number(input.dataset.ti)].name = input.value || ("Team " + (Number(input.dataset.ti) + 1));
        saveState();
      });
    });
    wrap.querySelectorAll(".jp-team-plus").forEach(btn => {
      btn.addEventListener("click", () => adjustScore(Number(btn.dataset.ti), 100));
    });
    wrap.querySelectorAll(".jp-team-minus").forEach(btn => {
      btn.addEventListener("click", () => adjustScore(Number(btn.dataset.ti), -100));
    });
    wrap.querySelectorAll(".jp-team-remove").forEach(btn => {
      btn.addEventListener("click", () => {
        state.teams.splice(Number(btn.dataset.ti), 1);
        saveState();
        renderTeams();
      });
    });
  }

  function adjustScore(ti, delta) {
    state.teams[ti].score += delta;
    saveState();
    renderTeams();
  }

  function attachControlHandlers() {
    document.getElementById("jp-add-team").addEventListener("click", () => {
      state.teams.push({ name: "Team " + (state.teams.length + 1), score: 0 });
      saveState();
      renderTeams();
    });
    document.getElementById("jp-reset-board").addEventListener("click", () => {
      if (!confirm("Reset the board? This clears used clues and all team scores.")) return;
      state = structuredClone(defaultState);
      saveState();
      render();
    });
    document.getElementById("jp-end-game").addEventListener("click", showWinner);
  }

  function showWinner() {
    if (!state.teams.length) { alert("Add at least one team first."); return; }
    const sorted = [...state.teams].sort((a, b) => b.score - a.score);
    const top = sorted[0];
    const tie = sorted.filter(t => t.score === top.score);
    const winnerText = tie.length > 1
      ? "Tie: " + tie.map(t => t.name).join(" & ") + ` (${top.score} pts)`
      : `${top.name} wins with ${top.score} pts!`;
    alert(winnerText);
  }

  function attachBoardHandlers() {
    root.querySelectorAll(".jp-tile:not(.jp-tile--used)").forEach(tile => {
      tile.addEventListener("click", () => openClue(Number(tile.dataset.ci), Number(tile.dataset.qi)));
    });
  }

  function openClue(ci, qi) {
    const cat = data.categories[ci];
    const clue = cat.clues[qi];
    const overlay = document.getElementById("jp-overlay");
    overlay.hidden = false;
    overlay.innerHTML = `
      <div class="jp-modal">
        <div class="jp-modal-value">$${clue.value}</div>
        <div class="jp-modal-cat">${escapeHtml(cat.name)}</div>
        <div class="jp-modal-question">${escapeHtml(clue.question)}</div>
        <div class="jp-modal-answer" id="jp-modal-answer">${escapeHtml(clue.answer)}</div>
        <div class="jp-modal-actions">
          <button class="jp-btn jp-btn--primary" id="jp-reveal">Reveal answer</button>
          <button class="jp-btn" id="jp-close">Close (skip)</button>
        </div>
        <div class="jp-award-row" id="jp-award-row"></div>
      </div>
    `;

    document.getElementById("jp-reveal").addEventListener("click", () => {
      document.getElementById("jp-modal-answer").classList.add("jp-modal-answer--shown");
      const awardRow = document.getElementById("jp-award-row");
      awardRow.classList.add("jp-award-row--shown");
      awardRow.innerHTML = state.teams.map((t, ti) =>
        `<button class="jp-award-btn" data-ti="${ti}">${escapeHtml(t.name)} correct (+${clue.value})</button>`
      ).join("") + `<button class="jp-award-btn jp-award-btn--wrong" id="jp-no-award">No one got it</button>`;

      awardRow.querySelectorAll(".jp-award-btn[data-ti]").forEach(btn => {
        btn.addEventListener("click", () => {
          adjustScore(Number(btn.dataset.ti), clue.value);
          markUsedAndClose(ci, qi);
        });
      });
      document.getElementById("jp-no-award").addEventListener("click", () => markUsedAndClose(ci, qi));
    });

    document.getElementById("jp-close").addEventListener("click", () => markUsedAndClose(ci, qi));
  }

  function markUsedAndClose(ci, qi) {
    state.used[clueKey(ci, qi)] = true;
    saveState();
    document.getElementById("jp-overlay").hidden = true;
    render();
  }

  function escapeHtml(str) {
    return String(str).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
  }
  function escapeAttr(str) { return escapeHtml(str); }

  render();
})();
