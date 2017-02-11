$(document).ready(function() {

  // wait for the iframe to load
  $('#game-iframe').on('load', function() {

    var iframe = document.getElementById('game-iframe');
    var iframeWindow = iframe.contentWindow || iframe;

    var baseUrl = window.location.protocol + "//" + window.location.host + "/";
    var urls = {
      'SCORE': 'message/score/',
      'SAVE': 'message/save/',
      'LOAD_REQUEST': 'message/load_request/',
      'LOAD': 'message/load/',
      'ERROR': 'message/error/',
      'SETTING': 'message/setting/'
    };

    var handleServiceResponse = function(response) {

    };

    var forwardMessageToService = function(message) {
      $.ajax({
        url: baseUrl + urls[message.messageType],
        method: 'post'
      }).done(function(response) {
        handleServiceResponse(response)
      }).fail(function(error) {
        console.log('error:', error);
      });
    };

    var sendErrorToGame = function(errorMessage) {
      var msg = {
        'messageType': 'ERROR',
        'info': errorMessage
      };
      iframeWindow.postMessage(msg, "*");
    };

    // listen for incoming messages
    $(window).on('message', function(e) {
      var receivedMessage = e.originalEvent.data;

      /*
       * Perform validation already on the client to avoid unnecessary requests
       */

      // check that the messageType attribute exists
      if (!receivedMessage.hasOwnProperty('messageType')) {
        sendErrorToGame('Incorrect message format');

      // check that the messageType itself is recognized
      } else if (!urls.hasOwnProperty(receivedMessage.messageType)) {
        sendErrorToGame('Message type not recognized')
      }

      // type recognized, continue
      else {
        // the game submitted a new score
        if (receivedMessage.messageType === 'SCORE') {
          if (receivedMessage.hasOwnProperty('score')) {
            forwardMessageToService(receivedMessage);
          } else {
            sendErrorToGame('Incorrect message format');
          }

        // the game sent a savegame
        } else if (receivedMessage.messageType === 'SAVE') {
          if (receivedMessage.hasOwnProperty('gameState')) {
            receivedMessage.gameState = JSON.stringify(receivedMessage.gameState)
            forwardMessageToService(receivedMessage);
          } else {
            sendErrorToGame('Incorrect message format');
          }

        // the game requested a savegame
        } else if (receivedMessage.messageType === 'LOAD_REQUEST') {
            forwardMessageToService(receivedMessage);

        // the game sent options
        } else if (receivedMessage.messageType === 'SETTING') {
          if (receivedMessage.hasOwnProperty('options')) {

            /*
             * Settings are not forwarded to the service when only used
             * for resolution, since resolution is adjusted without reload
             *
             * NOTE: at this point no other options are supported,
             *       so in no case will the options be sent to the backend
             */

            var includes_h = receivedMessage.options.hasOwnProperty('height')
            var includes_w = receivedMessage.options.hasOwnProperty('width')
            if (includes_h && includes_w) {
              var h = receivedMessage.options.height
              var w = receivedMessage.options.width

              // clamp to [(150x150), (1024x768)]
              // i.e. don't allow too large or too small
              h = Math.min(Math.max(h, 150), 768) + 'px';
              w = Math.min(Math.max(w, 150), 1024) + 'px';

              iframe.style.height = h;
              iframe.style.width = w;
            }

          } else {
            sendErrorToGame('Incorrect message format');
          }
        }
      }

    });

  });

});