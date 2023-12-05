#!/usr/bin/node
// Write a JavaScript script that adds the class red to
// <header> element when the user clicks on the tag DIV#red_header
const headerColor = $('#red_header').click(function() {
  $('header').addClass('red');
});
