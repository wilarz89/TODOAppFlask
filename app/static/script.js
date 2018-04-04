$ready(function(){
	$('button').click(function(){
		var user = $('#email').val();
		var pass = $('#password').val();
		var fname = $('#first_name').val();
		var lname = $('#last_name').val();

		$.ajax({
			url: '/registerUser',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});