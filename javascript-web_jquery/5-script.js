#!/usr/bin/node
// Write a JavaScript script that adds a <li> element to
// a list when the user clicks on the tag DIV#add_item:
const headerColor = $('#add_item').click(function() {
  $('UL.my_list').append('<li>Item</li>');
});
