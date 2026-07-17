(function () {
  'use strict';

  /* =========================================
   *  健壮 ID 检测（多级 fallback）
   * ========================================= */
  function detectLessonId() {
    try {
      // 1. 从页面标题提取 4 位数字
      var title = document.title || '';
      var m = title.match(/(\d{4})/);
      if (m) return m[1];
      // 2. 从 URL 路径提取 4 位数字
      m = window.location.pathname.match(/(\d{4})/);
      if (m) return m[1];
      // 3. 从 URL 最后一段提取末尾数字（如 /lesson/123 → 123）
      var segments = window.location.pathname.replace(/\/$/, '').split('/');
      var last = segments[segments.length - 1] || '';
      m = last.match(/(\d+)$/);
      if (m) return m[1];
    } catch (e) {}
    return null;
  }

  var lessonId = detectLessonId();
  if (!lessonId) {
    console.log('[PaperLesson Tools] no lesson ID detected, skipping');
    return;
  }

  /* =========================================
   *  工具条容器（SpeakScope 风格）
   *  放在 .lesson 内的 .footer-nav 前面，
   *  或 .lesson 末尾。
   * ========================================= */
  function createToolbar() {
    // Try .lesson first, then .nav as fallback for E2Map-style pages
    var container = document.querySelector('.lesson') || document.querySelector('.nav');
    if (!container) {
      console.log('[PaperLesson Tools] no .lesson or .nav found, toolbar skipped');
      return null;
    }

    var isNavFallback = container.classList.contains('nav');

    var toolbar = document.createElement('div');
    toolbar.id = 'pl-toolbar';
    toolbar.style.cssText = [
      'display: flex',
      'flex-wrap: wrap',
      'gap: 8px',
      'margin-bottom: 16px',
      'padding: 12px 16px',
      'background: #F7F4EE',
      'border: 1px solid #F0ECE4',
      'border-radius: 8px',
      'align-items: center',
      'box-sizing: border-box',
      'font-family: inherit'
    ].join(';') + ';';

    if (isNavFallback) {
      // E2Map lessons: insert toolbar before .nav
      container.parentNode.insertBefore(toolbar, container);
    } else {
      // 在 .footer-nav 前面插入，找不到则追加到 .lesson 末尾
      var footerNav = container.querySelector('.footer-nav');
      if (footerNav) {
        container.insertBefore(toolbar, footerNav);
      } else {
        container.appendChild(toolbar);
      }
    }

    console.log('[PaperLesson Tools] done button initialized');
    return toolbar;
  }

  /* =========================================
   *  1. 标记已学
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
      btn.textContent = '✅ 已学完';
      btn.disabled = true;
      btn.style.opacity = '0.6';
      btn.style.cursor = 'default';
      btn.style.background = 'var(--paper)';
      btn.style.borderColor = 'var(--accent-light)';
      btn.style.color = 'var(--ink-40)';
    } else {
      btn.textContent = '✅ 标记为已学';
      btn.disabled = false;
      btn.style.opacity = '1';
      btn.style.cursor = 'pointer';
      btn.style.background = 'var(--paper-light)';
      btn.style.borderColor = 'var(--accent)';
      btn.style.color = 'var(--accent)';
    }
  }

  function initDoneButton() {
    var toolbar = createToolbar();
    if (!toolbar) return;

    var btn = document.createElement('button');
    btn.id = 'pl-done-btn';
    btn.textContent = '✅ 标记为已学';
    btn.style.cssText = [
      'padding: 8px 16px',
      'border: 1px solid var(--border)',
      'border-radius: 6px',
      'cursor: pointer',
      'font-size: 0.9rem',
      'font-weight: 700',
      'background: var(--paper-light)',
      'color: var(--accent)',
      'border-color: var(--accent)',
      'transition: all 0.2s ease',
      'box-sizing: border-box',
      'font-family: inherit',
      'line-height: 1.4',
      'text-align: center'
    ].join(';') + ';';

    btn.onmouseover = function () {
      if (!btn.disabled) btn.style.background = 'var(--accent-dim)';
    };
    btn.onmouseout = function () {
      if (!btn.disabled) btn.style.background = 'var(--paper-light)';
    };
    btn.onclick = markDone;

    toolbar.appendChild(btn);
    updateDoneButton();
  }

  /* =========================================
   *  2. 滚动位置保存（每 3 秒防抖）
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
   *  3. 个人笔记（可折叠，位于工具条下方）
   * ========================================= */

  function initNotes() {
    var toolbar = document.getElementById('pl-toolbar');
    if (!toolbar) return;

    var outer = document.createElement('div');
    outer.style.cssText = [
      'margin-top: 20px',
      'border-top: 1px solid #e0d6d0',
      'padding-top: 12px'
    ].join(';') + ';';

    var toggle = document.createElement('button');
    toggle.textContent = '📝 我的笔记 ▸';
    toggle.style.cssText = [
      'background: none',
      'border: none',
      'cursor: pointer',
      'font-size: 14px',
      'color: #888',
      'padding: 8px 0',
      'width: 100%',
      'text-align: left',
      'font-family: inherit',
      'transition: color 0.12s'
    ].join(';') + ';';
    toggle.onmouseover = function () { toggle.style.color = '#CC785C'; };
    toggle.onmouseout = function () { toggle.style.color = '#888'; };

    var noteArea = document.createElement('div');
    noteArea.style.display = 'none';

    var textarea = document.createElement('textarea');
    textarea.style.cssText = [
      'width: 100%',
      'min-height: 100px',
      'border: 1px solid #d4c8c0',
      'border-radius: 8px',
      'padding: 12px',
      'font-size: 14px',
      'font-family: inherit',
      'resize: vertical',
      'box-sizing: border-box',
      'margin-top: 8px',
      'background: #fcfcfc',
      'color: #333',
      'line-height: 1.6'
    ].join(';') + ';';
    textarea.placeholder = '写下你的学习笔记…';

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
        toggle.textContent = '📝 我的笔记 ▾';
      } else {
        noteArea.style.display = 'none';
        toggle.textContent = '📝 我的笔记 ▸';
      }
    });

    noteArea.appendChild(textarea);
    outer.appendChild(toggle);
    outer.appendChild(noteArea);

    // 插入到工具条后面（工具栏已通过 insertBefore 放在 footer-nav 前）
    if (toolbar.parentNode) {
      toolbar.parentNode.insertBefore(outer, toolbar.nextSibling);
    }
  }

  /* =========================================
   *  初始化
   * ========================================= */

  function init() {
    initDoneButton();
    initNotes();
    restoreScroll();
    console.log('[PaperLesson Tools] inited');
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
