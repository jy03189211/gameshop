var cartUrlPrefix = '/cart';

var updateCartBadge = function(cart) {
  var count = Object.keys(cart).length;
  var cartBadge = $('.navbar-basket .navbar-item-badge');
  cartBadge.text(count);
  cartBadge.removeClass('hidden');
  cartBadge.animate({ top: '-=10' }, 150)
  cartBadge.animate({ top: '+=20' }, 200)
  cartBadge.animate({ top: '-=10' }, 150)
};

var addToCart = function(e) {
  e.preventDefault();
  if (e.target.dataset.hasOwnProperty('gameId')) {
    $.ajax({
      url: cartUrlPrefix + '/add/' + e.target.dataset.gameId + '/',
      method: 'post'
    }).done(function(res) {
      console.log('res:', res);
      updateCartBadge(res);
    }).fail(function(err) {
      console.log('err:', err);
    });
  } else {
    console.log('Cannot add to cart. Game ID missing.');
  }
};



$(document).ready(function() {
  $('*[data-action="cart-add"]').on('click', addToCart);
});