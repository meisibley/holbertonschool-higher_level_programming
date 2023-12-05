#!/usr/bin/node
// Write a JavaScript script that toggles the class of
// <header> element when the user clicks on tag DIV#toggle_header:
const headerColor = $('#toggle_header').click(function() {
  $('header').toggleClass('red green');
});
