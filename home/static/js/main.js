"use strict";


function _initGallery(){

  
  $('.gallery').slick({
      infinite: true,
      slidesToShow: 4,
      slidesToScroll: 4,
      lazyLoad: 'ondemand',
      dots: true,
      responsive: [
          {
            breakpoint: 768,
            settings: {
              slidesToShow: 2,
              slidesToScroll: 2
            }
          },
          {
            breakpoint: 540,
            settings: {
              slidesToShow: 1,
              slidesToScroll: 1
            }
          }
      ]
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