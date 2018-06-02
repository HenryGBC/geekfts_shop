"use strict";



var app = new Vue({
  delimiters: ['[[', ']]'],
  el: '#app',
  data: {
    showChat: false,
  },
  methods: {
    toggleChat: function (event) {
      // `this` inside methods points to the Vue instance
      console.log(this.showChat);
      this.showChat = !this.showChat;
    }
  }
});



// (function () {

// 	_initGallery();
// 	_initWs();

// })();




// function _initWs(){
// 	$('#open-ws').click(function(){
// 		$('.ws-chat').fadeIn();
// 	});
// 	$('#close-ws').click(function(){
// 		$('.ws-chat').fadeOut();
// 	});
// }