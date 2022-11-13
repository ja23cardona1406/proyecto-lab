$(document).ready(function(){

  $('.categorias-list .categoria-item[categoria="todos"]').addClass('ct_item-active');

  $('.categoria-item').click(function(){
    var catProduct = $(this).attr('categoria');
    console.log(catProduct);

    $('.categoria-item').removeClass('ct_item-active');
    $(this).addClass('ct_item-active');

    $('.product-item').css('transform', 'scale(0)');
		function hideProduct(){
			$('.product-item').hide();
		} setTimeout(hideProduct,400);

		function showProduct(){
			$('.product-item[categoria="'+catProduct+'"]').show();
			$('.product-item[categoria="'+catProduct+'"]').css('transform', 'scale(1)');
		} setTimeout(showProduct,400);
	});


	$('.categoria-item[categoria="todos"]').click(function(){
		function showAll(){
			$('.product-item').show();
			$('.product-item').css('transform', 'scale(1)');
		} setTimeout(showAll,400);
	
  });
});

