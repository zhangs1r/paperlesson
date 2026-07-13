(function () {
  'use strict';

  /* ─── 检测当前课程 ID ─── */
  function detectLessonId() {
    try {
      var title = document.title || '';
      var m = title.match(/(\d{4})/);
      if (m) return m[1];
      m = window.location.pathname.match(/(\d{4})/);
      if (m) return m[1];
    } catch (e) {}
    return null;
  }

  var lessonId = detectLessonId();
  if (!lessonId) return; /* 取不到课号，静默跳过 */

  /* =========================================
   *  1. 标记已学  —  按钮紧贴在 footer-nav 上方
   * ========================================= */

  function getDoneIds() {
    try { return JSON.parse(localStorage.getItem('paperlesson_done')) || []; } catch (e) { return []; }
  }

  function saveDoneIds(ids) {
    try { localStorage.setItem('paperlesson_done', JSON.stringify(ids)); } catch (e) {}
  }

  function isDone() {
    return getDoneIds().indexOf(lessonId) !== -1;
  }

  function recordStudyDate() {
    try {
      var today = new Date().toISOString().slice(0, 10);
      var tally = JSON.parse(localStorage.getItem('paperlesson_vtally')) || {};
      tally[lessonId] = today;
      localStorage.setItem('paperlesson_vtally', JSON.stringify(tally));
    } catch (e) {}
  }

  function markDone() {
    var ids = getDoneIds();
    if (ids.indexOf(lessonId) === -1) {
      ids.push(lessonId);
      saveDoneIds(ids);
    }
    recordStudyDate();
    updateDoneButton();
  }

  function updateDoneButton() {
    var btn = document.getElementById('pl-done-btn');
    if (!btn) return;
    if (isDone()) {
      btn.textContent = '\u2705 \u5DF2\u5B66\u5B8C';
      btn.disabled = true;
      btn.style.opacity = '0.6';
      btn.style.cursor = 'default';
      btn.style.background = 'rgba(204,120,92,0.03)';
    } else {
      btn.textContent = '\u2705 \u6807\u8BB0\u4E3A\u5DF2\u5B66';
      btn.disabled = false;
      btn.style.opacity = '1';
      btn.style.cursor = 'pointer';
      btn.style.background = 'rgba(204,120,92,0.06)';
    }
  }

  function initDoneButton() {
    var footerNav = document.querySelector('.footer-nav');
    if (!footerNav) return;

    var btn = document.createElement('button');
    btn.id = 'pl-done-btn';
    btn.style.cssText = 'display:block;width:100%;padding:var(--space-3);border:2px solid var(--accent);border-radius:8px;background:rgba(204,120,92,0.06);color:var(--accent-deep);font-size:var(--text-base);font-weight:700;cursor:pointer;transition:all .18s ease;margin-bottom:var(--space-5);box-sizing:border-box;';
    btn.onmouseover = function () {
      if (!btn.disabled) btn.style.background = 'rgba(204,120,92,0.15)';
    };
    btn.onmouseout = function () {
      if (!btn.disabled) btn.style.background = 'rgba(204,120,92,0.06)';
    };
    btn.onclick = markDone;

    footerNav.parentNode.insertBefore(btn, footerNav);
    updateDoneButton();
  }

  /* =========================================
   *  2. 滚动位置保存（每 3 秒一次）
   * ========================================= */

  var scrollKey = 'paperlesson_scroll_' + lessonId;
  var scrollTimer = null;

  function saveScroll() {
    try { localStorage.setItem(scrollKey, window.scrollY.toString()); } catch (e) {}
  }

  function restoreScroll() {
    try {
      var saved = localStorage.getItem(scrollKey);
      if (saved !== null) {
        var pos = parseInt(saved, 10);
        if (!isNaN(pos) && pos > 0) {
          setTimeout(function () { window.scrollTo(0, pos); }, 100);
        }
      }
    } catch (e) {}
  }

  window.addEventListener('scroll', function () {
    if (scrollTimer) clearTimeout(scrollTimer);
    scrollTimer = setTimeout(saveScroll, 3000);
  });

  /* =========================================
   *  3. 个人笔记（可折叠，位于 footer-nav 下方）
   * ========================================= */

  function initNotes() {
    var footerNav = document.querySelector('.footer-nav');
    if (!footerNav) return;

    var container = document.createElement('div');
    container.style.cssText = 'margin-top:var(--space-6);border-top:1px solid var(--border);padding-top:var(--space-4);';

    var toggle = document.createElement('button');
    toggle.textContent = '\uD83D\uDCDD \u6211\u7684\u7B14\u8BB0 \u25B8';
    toggle.style.cssText = 'background:none;border:none;cursor:pointer;font-size:var(--text-sm);color:var(--ink-60);padding:var(--space-2) 0;width:100%;text-align:left;font-family:var(--font-sans);transition:color .12s;';
    toggle.onmouseover = function () { toggle.style.color = 'var(--accent-deep)'; };
    toggle.onmouseout = function () { toggle.style.color = 'var(--ink-60)'; };

    var noteArea = document.createElement('div');
    noteArea.style.display = 'none';

    var textarea = document.createElement('textarea');
    textarea.style.cssText = 'width:100%;min-height:100px;border:1px solid var(--border);border-radius:8px;padding:var(--space-3);font-size:var(--text-sm);font-family:var(--font-sans);resize:vertical;box-sizing:border-box;margin-top:var(--space-2);background:var(--paper-light);color:var(--ink);';
    textarea.placeholder = '\u5199\u4E0B\u4F60\u7684\u5B66\u4E60\u7B14\u8BB0\u2026';

    var noteKey = 'paperlesson_note_' + lessonId;
    try {
      var savedNote = localStorage.getItem(noteKey);
      if (savedNote) textarea.value = savedNote;
    } catch (e) {}

    textarea.addEventListener('input', function () {
      try { localStorage.setItem(noteKey, textarea.value); } catch (e) {}
    });

    toggle.addEventListener('click', function () {
      if (noteArea.style.display === 'none') {
        noteArea.style.display = 'block';
        toggle.textContent = '\uD83D\uDCDD \u6211\u7684\u7B14\u8BB0 \u25BE';
      } else {
        noteArea.style.display = 'none';
        toggle.textContent = '\uD83D\uDCDD \u6211\u7684\u7B14\u8BB0 \u25B8';
      }
    });

    noteArea.appendChild(textarea);
    container.appendChild(toggle);
    container.appendChild(noteArea);
    footerNav.parentNode.insertBefore(container, footerNav.nextSibling);
  }

  /* =========================================
   *  初始化
   * ========================================= */

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initDoneButton();
      initNotes();
      restoreScroll();
    });
  } else {
    initDoneButton();
    initNotes();
    restoreScroll();
  }

})();
