#!/usr/bin/node
// Write a JavaScript script that adds the class red to
// <header> element when the user clicks on the tag DIV#red_header
$('DIV#red_header').off('click').click(() => $('HEADER').addClass('red'));
