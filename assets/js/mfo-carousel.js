function fixImg() {

  var curHeight = $('.item.active').height();
  console.log('curHeight:', curHeight);

	var maxHeightText = $('#mfoCarousel').css('max-height');
  var maxHeight = parseInt(maxHeightText,10);
	console.log('maxHeight:', maxHeight);

  var offset = 0;

  var translate = "none";

  if (curHeight > maxHeight) {
    offset = (maxHeight - curHeight) / 2;
    //console.log('offset:', offset);
    translate = 'translateY(' + offset + 'px)';
  }
  console.log("transform: ", translate);

// this is picking up the items from the sponsor carousel too i think
//  var images = $('.item img');
  var images = $("#mfoCarousel .carousel-inner .item img");

	images.each(function(){
    $(this).css( 'transform' , translate);
    var itemID = $(this).attr('src');
    console.log(itemID, ":" ,translate);
})

};

fixImg(); //run on page load

$(window).resize(fixImg);
