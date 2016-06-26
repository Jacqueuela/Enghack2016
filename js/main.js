$(document).ready(function(){
 	

 	$('#hostmodal').click(function(event) {
		$('#myModal').modal('show');
	});

	$('#submit').click(function(){
		 $.ajax({
            type: "POST",
            url: "http://localhost:8000/Store",
            data: {
                Genre1: document.getElementById("tag1").value,
                Genre2: document.getElementById("tag2").value
             },
             dataType: 'json',
            success: function(response){
            	$('#myModal').modal('hide');
        	}
        });
		
	});
	
});	 



   // ("#suggestform").validate({
			// rules: {
			// 	tag1: {
			// 		required: true,
			// 		min:{
			// 			depends: function(element){
			// 				console.log("depends");
			// 				var availableTags = [
			// 				  "Action",
			// 				  "Adventure",
			// 				  "Animation",
			// 				  "Comedy",
			// 				  "Crime",
			// 				  "Documentary",
			// 				  "Drama",
			// 				  "Family",
			// 				  "Fantasy",
			// 				  "Foreign",
			// 				  "History",
			// 				  "Horror",
			// 				  "Music",
			// 				  "Mystery",
			// 				  "Romance",
			// 				  "Science Fiction",
			// 				  "TV Movie",
			// 				  "Thriller",
			// 				  "War",
			// 				  "Western"
			// 				];

			// 				return availableTags.indexOf(element) > -1;
			// 			}
			// 		}
			// 	},
			// 	tag2: "required",
			// }})