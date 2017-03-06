/*
 * NOTE: This script ensures that the iframe element is loaded only after
 * the parent document is loaded. Otherwise, if the iframe load event would
 * happen before the parent document load event, the messaging service cannot
 * be guaranteed to work if the iframe loads faster than the parent page.
 *
 * Reads the game URL from the #iframe-wrap element's data-game-url attribute
 * and creates the iframe element.
 *
 * Must be loaded after the message service (message.js).
 */

$(document).ready(function() {
  var iframeWrap = document.getElementById('iframe-wrap');

  if (iframeWrap) {
    var url = iframeWrap.dataset.gameUrl;

    if (url) {
      var iframe = document.createElement("iframe");
      iframe.id = "game-iframe";
      iframe.src = url;
      iframe.frameBorder = 0;
      iframeWrap.appendChild(iframe);

      // try to set focus on the iframe since games may utilize key presses
      iframe.focus();
    }
  }
});