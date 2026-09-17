/* 图片点击放大 —— 手机查看论文原图用。
   用法：页面 </body> 前引用 <script src="assets/paillier/lightbox.js"></script>
   自动为所有 figure img 绑定点击放大（含双指缩放支持）。 */
(function () {
  'use strict';

  function build() {
    var box = document.createElement('div');
    box.className = 'lightbox';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-label', '图片放大查看');
    var img = document.createElement('img');
    img.alt = '';
    var close = document.createElement('button');
    close.className = 'lb-close';
    close.type = 'button';
    close.setAttribute('aria-label', '关闭');
    close.textContent = '✕';
    var hint = document.createElement('div');
    hint.className = 'lb-hint';
    hint.textContent = '双指缩放 · 点击空白关闭';
    box.appendChild(img);
    box.appendChild(close);
    box.appendChild(hint);
    document.body.appendChild(box);

    function open(src, alt) {
      img.src = src;
      img.alt = alt || '';
      box.classList.add('on');
      document.documentElement.style.overflow = 'hidden';
    }
    function shut() {
      box.classList.remove('on');
      img.removeAttribute('src');
      document.documentElement.style.overflow = '';
    }

    close.addEventListener('click', shut);
    box.addEventListener('click', function (e) {
      if (e.target === box) shut();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && box.classList.contains('on')) shut();
    });

    var imgs = document.querySelectorAll('figure img');
    Array.prototype.forEach.call(imgs, function (im) {
      im.addEventListener('click', function () {
        open(im.currentSrc || im.src, im.getAttribute('alt'));
      });
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();
