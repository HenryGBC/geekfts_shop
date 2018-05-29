"use strict";


function _initGallery(){

  
  $('.shirts').slick({
      infinite: true,
      slidesToShow: 1,
      slidesToScroll: 1,
      lazyLoad: 'ondemand',
      dots: true
    });
}

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
    },
    sendWs: function(){
    	let name = $('#btn-ws').data('name');
    	let text = 'Hola quiero la camiseta '+name;
    	text = text.replace(' ', '%20');
    	window.open('https://api.whatsapp.com/send?phone=573058628798&text='+text+'', '_blank');
    }
  },
  created: function () {
    setTimeout(()=>{
      _initGallery();
    }, 500)
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