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