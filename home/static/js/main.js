"use strict";

(function () {

	_initGallery();
	_initWs();

})();


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

function _initWs(){
	$('#open-ws').click(function(){
		$('.ws-chat').fadeIn();
	});
	$('#close-ws').click(function(){
		$('.ws-chat').fadeOut();
	});
}