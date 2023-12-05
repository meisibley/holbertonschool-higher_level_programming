#!/usr/bin/node
// Write a JavaScript script that toggles the class of
// <header> element when the user clicks on tag DIV#toggle_header:
$('DIV#toggle_header').off('click').click(() => {
  $('HEADER').toggleClass('red green');
});
