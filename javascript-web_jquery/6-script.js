#!/usr/bin/node
// Write a JavaScript script that updates the text of
// <header> element to New Header!!! when the user
// clicks on DIV#update_header
$('DIV#update_header').click(() => $('HEADER').text('New Header!!!'));
