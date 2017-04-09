$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip(); 
});

$(".paste-index").click(function(e){
	e.preventDefault();
	var id= e.target.id;
	$.get("/paste/"+id+"/remove", function(data, status){
		if(data == "1"){
			e.target.parentElement.parentElement.remove();
		}
	});
});

$(".btn-sort").click(function(e){
	var button= $("#"+e.target.id);
	if(button.hasClass("btn-primary")){
		button.removeClass("btn-primary");
		Cookies.remove(e.target.id);
	}else{
		button.addClass("btn-primary");
		Cookies.set(e.target.id, "1");
	}
});

$('#input_username').on('input', function(e) {
    Cookies.set("username", e.target.value);
});

$('#refresh_pastes').click(function(e){
	location.reload();
});

$('#paste_area').bind('input propertychange', function(e) {
	if($('#paste_name').val() == ""){
		var content= e.target.value;
		if(content.length > 20){
			content= content.substring(0, 17)+"...";
		}
		$('#paste_name').val(content);
	}
});

$('.module-header').click(function(e){
	var module_body= $(this).parent().children('.module-body');
	
	if(module_body.is(":hidden")){

		
	}

	module_body.toggle();

	
});

$('.module-star').click(function(e){
	$(this).toggleClass('glyphicon-star');
	$(this).toggleClass('glyphicon-star-empty');	
	e.stopPropagation();
});

function refreshModule(){
	var id= $(module_body).children('#module_id').val();
	var paste_content= $('#paste_content').val();
	var module_area= module_body.children('#module_content');
	
	$.ajax({
		type: "POST",
		contentType: "application/json; charset=utf-8",
		url: "/module/"+id+"/process",
		data: JSON.stringify({data: paste_content}),
		success : function(text)
		{
			$(module_area).val(text);
		}
	});
}


