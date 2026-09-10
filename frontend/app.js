let currentResult = null;
let savedVersions = [];

function setSample(text) {
  document.getElementById('raw-idea').value = text;
}

document.getElementById('research-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const rawIdea = document.getElementById('raw-idea').value.trim();
  const userLevel = document.getElementById('user-level').value;
  const contextLoc = document.getElementById('context-location').value.trim();
  const timeConstraint = document.getElementById('time-constraint').value;
  const btn = document.getElementById('btn-analyze');

  if (!rawIdea) return;

  btn.disabled = true;
  btn.innerHTML = `
    <svg class="animate-spin" width="18" height="18" fill="none" stroke="currentColor" viewBox="0 0 24 24" style="animation: spin 1s linear infinite;"><circle cx="12" cy="12" r="10" stroke-width="3" stroke-dasharray="32" stroke-linecap="round"/></svg>
    <span>Menganalisis Metodologi...</span>
  `;

  // Pipeline visual indicator
  setActiveNode('node-diag');

  try {
    const response = await fetch('/api/professionalize', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        raw_idea: rawIdea,
        user_level: userLevel,
        context_location: contextLoc,
        time_constraint: timeConstraint
      })
    });

    if (!response.ok) {
      const err = await response.json();
      throw new Error(err.detail || 'Terjadi kegagalan saat analisis.');
    }

    const data = await response.json();
    currentResult = data;
    renderResults(data);
    addToHistory(data);
    setActiveNode('node-blue');
  } catch (error) {
    alert('Error: ' + error.message);
  } finally {
    btn.disabled = false;
    btn.innerHTML = `
      <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
      <span>Bedah & Profesionalisasi Ide</span>
    `;
  }
});

function setActiveNode(nodeId) {
  const nodes = ['node-idea', 'node-diag', 'node-var', 'node-feas', 'node-title', 'node-blue'];
  let reached = false;
  nodes.forEach(id => {
    const el = document.getElementById(id);
    if (!el) return;
    el.classList.remove('active', 'completed');
    if (id === nodeId) {
      el.classList.add('active');
      reached = true;
    } else if (!reached) {
      el.classList.add('completed');
    }
  });
}

function renderResults(data) {
  document.getElementById('empty-state').style.display = 'none';
  document.getElementById('active-result').style.display = 'block';

  // Domain & Scope
  document.getElementById('domain-badge').textContent = data.domain;
  const scopeBanner = document.getElementById('scope-banner');
  const scopeStatus = document.getElementById('scope-status');
  scopeStatus.textContent = `STATUS CAKUPAN: ${data.scope_diagnosis.status.toUpperCase()}`;
  
  if (data.scope_diagnosis.status.toLowerCase() === 'appropriate') {
    scopeBanner.className = 'diagnostic-banner appropriate';
    scopeStatus.className = 'diag-status appropriate';
  } else {
    scopeBanner.className = 'diagnostic-banner';
    scopeStatus.className = 'diag-status';
  }
  
  document.getElementById('scope-explanation').textContent = data.scope_diagnosis.explanation;
  document.getElementById('scope-recommendation').textContent = 'Rekomendasi Penajaman: ' + data.scope_diagnosis.recommended_focus;

  // Critical questions
  const qList = document.getElementById('critical-questions-list');
  qList.innerHTML = '';
  data.critical_questions.forEach(q => {
    const li = document.createElement('li');
    li.textContent = q;
    li.style.marginBottom = '6px';
    qList.appendChild(li);
  });

  // Variables Table
  const vBody = document.getElementById('variables-tbody');
  vBody.innerHTML = '';
  data.variables.forEach(v => {
    const tr = document.createElement('tr');
    tr.innerHTML = `
      <td><span class="var-tag">${v.category}</span><br><b>${v.variable}</b></td>
      <td>${v.definition}</td>
      <td><span style="color: var(--secondary); font-weight: 500;">${v.indicator}</span></td>
      <td>${v.measurement}</td>
      <td><i>${v.instrument}</i></td>
    `;
    vBody.appendChild(tr);
  });

  // Feasibility
  document.getElementById('feasibility-overall-badge').textContent = 
    `Kelayakan Keseluruhan: ${data.feasibility.total_score}/5.0 (${data.feasibility.percentage}%) — ${data.feasibility.status}`;
  
  const fCards = document.getElementById('feasibility-cards');
  fCards.innerHTML = '';
  data.feasibility.details.forEach(item => {
    const div = document.createElement('div');
    div.className = 'feasibility-card';
    div.innerHTML = `
      <div class="feasibility-dim">${item.dimension}</div>
      <div class="feasibility-score-badge">${item.score}/5</div>
      <div class="feasibility-rating">${item.rating}</div>
      <div style="font-size: 0.74rem; color: var(--text-dim); margin-top: 4px;">${item.analysis}</div>
    `;
    fCards.appendChild(div);
  });

  // Risks & Mitigations
  const risksContainer = document.getElementById('risks-container');
  risksContainer.innerHTML = '';
  data.risks_and_mitigations.forEach(r => {
    const div = document.createElement('div');
    div.style.background = 'rgba(255,255,255,0.03)';
    div.style.border = '1px solid rgba(255,255,255,0.07)';
    div.style.borderRadius = '8px';
    div.style.padding = '10px 14px';
    div.innerHTML = `
      <div style="font-weight: 700; color: #fb7185; font-size: 0.84rem;">⚠ ${r.risk_type}</div>
      <div style="font-size: 0.8rem; color: #cbd5e1; margin-top: 2px;">${r.explanation}</div>
      <div style="font-size: 0.8rem; color: var(--success); margin-top: 4px;"><b>Solusi Metodologis:</b> ${r.solution}</div>
    `;
    risksContainer.appendChild(div);
  });

  // Title Options
  const titlesContainer = document.getElementById('title-options-container');
  titlesContainer.innerHTML = '';
  data.title_options.forEach((opt, idx) => {
    const isSelected = opt.title === data.selected_title;
    const card = document.createElement('div');
    card.className = `title-card ${isSelected ? 'selected' : ''}`;
    card.onclick = () => selectTitle(idx);
    card.innerHTML = `
      <div class="title-badge-row">
        <span class="option-tag">${opt.category}</span>
        <span class="title-score">Score: ${opt.overall_score}/10</span>
      </div>
      <div class="title-text">${opt.title}</div>
      <div class="title-meta">
        <div><b>Kekuatan:</b> ${opt.strength}</div>
        <div><b>Metode Cocok:</b> ${opt.suitable_method}</div>
      </div>
    `;
    titlesContainer.appendChild(card);
  });

  // Research Blueprint
  renderBlueprint(data.blueprint, data.novelty, data.literature);
}

function selectTitle(index) {
  if (!currentResult) return;
  const chosenTitle = currentResult.title_options[index];
  currentResult.selected_title = chosenTitle.title;
  currentResult.blueprint.proposed_title = chosenTitle.title;
  currentResult.blueprint.research_design = chosenTitle.suitable_method;

  // Re-render title cards and blueprint
  const cards = document.querySelectorAll('.title-card');
  cards.forEach((c, idx) => {
    if (idx === index) c.classList.add('selected');
    else c.classList.remove('selected');
  });

  renderBlueprint(currentResult.blueprint, currentResult.novelty, currentResult.literature);
}

function renderBlueprint(bp, novelty, literature) {
  document.getElementById('bp-title').textContent = bp.proposed_title;
  document.getElementById('bp-domain').textContent = bp.research_field;
  document.getElementById('bp-level').textContent = bp.research_maturity_level;
  document.getElementById('bp-feasibility').textContent = bp.feasibility_score;

  document.getElementById('bp-problem').textContent = bp.research_problem;
  document.getElementById('bp-background').textContent = bp.research_background;
  document.getElementById('bp-gap').textContent = bp.research_gap;
  
  if (novelty) {
    document.getElementById('bp-novelty').innerHTML = `<b>Pernyataan Kebaruan:</b> ${novelty.potential_novelty_statement}`;
  }

  const qUl = document.getElementById('bp-questions');
  qUl.innerHTML = '';
  bp.research_questions.forEach(q => {
    const li = document.createElement('li');
    li.textContent = q;
    qUl.appendChild(li);
  });

  const hUl = document.getElementById('bp-hypotheses');
  hUl.innerHTML = '';
  (bp.hypotheses || []).forEach(h => {
    const li = document.createElement('li');
    li.textContent = h;
    hUl.appendChild(li);
  });

  document.getElementById('bp-design').textContent = bp.research_design;
  document.getElementById('bp-population').textContent = bp.population;
  document.getElementById('bp-sample').textContent = bp.sample;
  document.getElementById('bp-sampling').textContent = bp.sampling_technique;
  document.getElementById('bp-instruments').textContent = bp.research_instruments;

  document.getElementById('bp-analysis').textContent = bp.data_analysis;
  const sUl = document.getElementById('bp-stats');
  sUl.innerHTML = '';
  bp.recommended_statistical_methods.forEach(s => {
    const li = document.createElement('li');
    li.textContent = s;
    sUl.appendChild(li);
  });

  document.getElementById('bp-contribution').textContent = bp.expected_contribution;
  document.getElementById('bp-ethics').textContent = bp.ethical_considerations;
  document.getElementById('bp-limitations').textContent = bp.potential_limitations;

  // Real literature list
  const litDiv = document.getElementById('bp-literature');
  litDiv.innerHTML = '';
  (literature || []).forEach(lit => {
    const row = document.createElement('div');
    row.style.fontSize = '0.78rem';
    row.style.background = 'rgba(0,0,0,0.2)';
    row.style.padding = '6px 10px';
    row.style.borderRadius = '4px';
    row.innerHTML = `
      <b>${lit.title}</b> (${lit.year || 'n.d.'}) &mdash; <i>${lit.authors.join(', ')}</i>
      <br><span style="color: var(--text-dim);">${lit.journal} | DOI: ${lit.doi || 'N/A'}</span>
    `;
    litDiv.appendChild(row);
  });
}

function addToHistory(item) {
  savedVersions.push(item);
  const container = document.getElementById('history-container');
  if (savedVersions.length === 1) {
    container.innerHTML = '';
  }

  const hDiv = document.createElement('div');
  hDiv.className = 'history-item';
  hDiv.onclick = () => {
    currentResult = item;
    renderResults(item);
  };
  hDiv.innerHTML = `
    <div class="history-version">Versi ${item.version} &bull; ${item.domain}</div>
    <div class="history-idea">"${item.raw_idea}"</div>
  `;
  container.prepend(hDiv);
}

async function copyBlueprintMarkdown() {
  if (!currentResult) return;
  try {
    const res = await fetch('/api/export/markdown', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(currentResult.blueprint)
    });
    const data = await res.json();
    navigator.clipboard.writeText(data.markdown);
    alert('Markdown Research Blueprint berhasil disalin ke clipboard!');
  } catch (err) {
    alert('Gagal menyalin markdown: ' + err.message);
  }
}

async function downloadBlueprintTxt() {
  if (!currentResult) return;
  const res = await fetch('/api/export/markdown', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(currentResult.blueprint)
  });
  const data = await res.json();
  const blob = new Blob([data.markdown], { type: 'text/plain;charset=utf-8' });
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `Research_Blueprint_v${currentResult.version}.txt`;
  a.click();
}
