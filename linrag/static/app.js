const $ = (id) => document.getElementById(id);
const form = $('query-form');
let busy = false;
let composing = false;
const input = $('query');
input.addEventListener('compositionstart', () => { composing = true; });
input.addEventListener('compositionend', () => { composing = false; });
input.addEventListener('keydown', event => {
  if (event.key === 'Enter' && (event.isComposing || composing || event.keyCode === 229)) event.preventDefault();
});

async function health() {
  try {
    const res = await fetch('/api/health');
    if (!res.ok) throw new Error();
    const state = await res.json();
    $('health').textContent = state.index_ready ? `${state.commands.toLocaleString()} 个命令 · ${state.vector_ready ? '混合检索' : '关键词检索'}` : '等待建立知识库';
    if (!state.index_ready) $('notice').textContent = state.error || '请先审核 Markdown 知识库，再按 README 配置向量化。';
  } catch { $('health').textContent = '服务暂不可用'; }
}

function addCopyButtons() {
  $('evidence').querySelectorAll('pre').forEach(pre => {
    const code = pre.querySelector('code');
    if (!code) return;
    const button = document.createElement('button');
    button.type = 'button'; button.className = 'copy'; button.textContent = '复制';
    button.addEventListener('click', async () => {
      try { await navigator.clipboard.writeText(code.textContent); button.textContent = '已复制'; }
      catch { button.textContent = '请手动选择复制'; }
      setTimeout(() => { button.textContent = '复制'; }, 2000);
    });
    pre.append(button);
  });
  $('evidence').querySelectorAll('a').forEach(link => { link.target = '_blank'; link.rel = 'noopener noreferrer'; });
}

function showEvidence(rows) {
  $('evidence').replaceChildren();
  $('evidence-count').textContent = rows.length;
  rows.forEach(row => {
    const details = document.createElement('details'); details.id = `result-${row.citation}`; details.open = row.citation === 1;
    const summary = document.createElement('summary');
    const title = document.createElement('span'); title.className = 'command'; title.textContent = `[${row.citation}] ${row.command}`;
    const badge = document.createElement('span'); badge.className = 'source'; badge.textContent = `${row.source} / ${row.language} / ${row.platform}`;
    summary.append(title, badge);
    const body = document.createElement('div'); body.className = 'evidence-body';
    const content = document.createElement('div'); content.className = 'document';
    // HTML is rendered by our server with raw HTML disabled.
    content.innerHTML = row.html;
    const link = document.createElement('a'); link.className = 'source-link'; link.textContent = '查看固定版本原文 ↗';
    if (row.url.startsWith('https://github.com/')) link.href = row.url;
    link.target = '_blank'; link.rel = 'noopener noreferrer';
    const meta = document.createElement('div'); meta.className = 'metadata';
    meta.textContent = `${row.attribution} · ${row.license} · ${row.revision.slice(0, 12)} · RRF ${row.score}`;
    body.append(content, link, meta); details.append(summary, body); $('evidence').append(details);
  });
}

form.addEventListener('submit', async event => {
  event.preventDefault();
  if (busy || composing) return;
  const query = $('query').value.trim();
  if (!query) { $('query').focus(); return; }
  busy = true; $('submit').disabled = true; $('submit').textContent = '检索中…';
  $('notice').textContent = '正在检索文档…'; $('response').hidden = true;
  const controller = new AbortController(); const timeout = setTimeout(() => controller.abort(), 110000);
  try {
    const res = await fetch('/api/search', { method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({query}), signal: controller.signal });
    if (!res.ok) throw new Error(`请求失败（HTTP ${res.status}）`);
    const data = await res.json();
    $('welcome').hidden = true; $('response').hidden = false;
    $('empty-results').hidden = data.results.length !== 0;
    $('mode').textContent = data.mode === 'hybrid' ? '关键词 + 语义' : data.mode === 'lexical' ? '关键词检索' : '索引未就绪';
    $('notice').textContent = (data.warnings || []).join('\n');
    showEvidence(data.results); addCopyButtons();
  } catch (error) { $('notice').textContent = error.name === 'AbortError' ? '请求超时，请稍后重试。' : `无法完成请求：${error.message}`; }
  finally { clearTimeout(timeout); busy = false; $('submit').disabled = false; $('submit').textContent = '搜索 ↵'; }
});
document.querySelectorAll('[data-query]').forEach(button => button.addEventListener('click', () => { input.value = button.dataset.query; input.focus(); form.requestSubmit(); }));
document.addEventListener('keydown', event => {
  if (event.isComposing || composing || event.keyCode === 229) return;
  const editing = event.target.closest('input, textarea, [contenteditable="true"]');
  if (((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k') ||
      (event.key === '/' && !editing && !event.ctrlKey && !event.metaKey && !event.altKey)) {
    event.preventDefault(); input.focus(); input.select();
  }
});
input.focus({preventScroll: true});
health();
