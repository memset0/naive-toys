Array.from(document.getElementsByClassName('btn-ripple')).forEach($btn => {
  $btn.addEventListener('click', event => {
    const $ripple = document.createElement('div');
    const x = event.x - $btn.getBoundingClientRect().x - 10;
    const y = event.y - $btn.getBoundingClientRect().y - 10;
    $ripple.style.left = x + 'px';
    $ripple.style.top = y + 'px';
    $ripple.classList.add('ripple');
    $btn.appendChild($ripple);
    const listener = function() {
      $btn.removeChild($ripple);
      $ripple.removeEventListener('animationend', listener);
    };
    $ripple.addEventListener('animationend', listener);
  });
});