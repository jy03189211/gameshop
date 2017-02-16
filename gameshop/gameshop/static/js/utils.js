var submitParent = function(e) {
  e.preventDefault();
  e.target.parentNode.submit();
};

var submitParentWithConfirm = function(e) {
  e.preventDefault();
  if (window.confirm("Are you sure you want to remove this game?")) {
    e.target.parentNode.submit();
  }
};

var enableMobileGameScaling = function() {
  /*
   * Allow the iframe to be scaled according to the viewport width.
   * Scales all content in the iframe, i.e. not only resizes the iframe.
   */

  var scale_target = $('#scale-target-width');
  var iframe_wrap = $('#iframe-wrap');
  var iframe = $('#game-iframe');

  var initial_w = iframe.width();
  var initial_h = iframe.height();

  var window_w = $(window).width();
  if (window_w >= 768) {
    margin = 30;
  } else {
    margin = 15;
  }

  // target size, keeping the aspect ratio
  var target_w = scale_target.width() - 2 * margin;
  var scale_ratio = (target_w / initial_w);
  var target_h = initial_h * scale_ratio;

  iframe.css({
    '-webkit-transform' : 'scale(' + scale_ratio + ')',
    '-moz-transform'    : 'scale(' + scale_ratio + ')',
    '-ms-transform'     : 'scale(' + scale_ratio + ')',
    '-o-transform'      : 'scale(' + scale_ratio + ')',
    'transform'         : 'scale(' + scale_ratio + ')'
  });
  iframe_wrap.css({
    'width': target_w + 'px',
    'height': target_h + 'px'
  });
};

var disableMobileGameScaling = function() {
  /*
   * Disable iframe scaling according to viewport width.
   */

  var iframe_wrap = $('#iframe-wrap');
  var iframe = $('#game-iframe');

  iframe.css({
    '-webkit-transform' : 'scale(1)',
    '-moz-transform'    : 'scale(1)',
    '-ms-transform'     : 'scale(1)',
    '-o-transform'      : 'scale(1)',
    'transform'         : 'scale(1)',
  });
  iframe_wrap.css({
    'width': '',
    'height': ''
  });
};

$(document).ready(function() {
  var scale_enabled = false;

  // add listener for scale toggle click
  var scale_toggle = $('#scale-toggle');

  if (scale_toggle) {
    scale_toggle.on('click', function(e) {
      e.preventDefault();
      if (scale_enabled) {
        disableMobileGameScaling();
        scale_enabled = false;
      } else {
        enableMobileGameScaling();
        scale_enabled = true;
      }
    });
  }

  // disable scaling when resolution is changed
  $(window).on('message', function(e) {
    var receivedMessage = e.originalEvent.data;
    if (receivedMessage.messageType === 'SETTING') {
      if (receivedMessage.hasOwnProperty('options')) {
        if (scale_enabled) {
          disableMobileGameScaling();
          scale_enabled = false;
        }
      }
    }

  });

});