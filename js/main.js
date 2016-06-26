$(document).ready(function(){
 	

 	$('#hostmodal').click(function(event) {
		$('#myModal').modal('show');
	});

	$('#submit').click(function(){
		console.log("running");
		 $.ajax({
            type: "POST",
            url: "http://localhost:8000/Store",
            data: {
                Genre1: $('#tag1'),
                Genre2: $('#tag2')
             },
             dataType: 'json',
            success: function(response){
            	$('#myModal').modal('close');
        	}
        });
	});
	
});	 