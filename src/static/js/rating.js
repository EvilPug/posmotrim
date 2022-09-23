$(".rating a").on('click', function(e){
	let value = $(this).data('value');
   $.ajax({
      url: "some_url",
      type: 'POST',
      data: {'rating': value},
      success: function (d){
       // some processing
      }
   })
});