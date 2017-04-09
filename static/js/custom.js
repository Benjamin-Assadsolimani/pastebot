$(document).ready(function(){
    $('[data-toggle="tooltip"]').tooltip(); 
});

$('body').on('click', '.paste-index', function(e){
	e.preventDefault();
	var id= e.target.id;
	$.get("/paste/"+id+"/remove", function(data, status){
		if(data == "1"){
			e.target.parentElement.parentElement.remove();
		}
	});
});

$('#input_username').on('input', function(e) {
    Cookies.set("username", e.target.value);
});

$('body').on('click', '#refresh_pastes', function(e){
	location.reload();
});

$('#paste_content').bind('input propertychange', function(e) {
	if($('#paste_name').val() == ""){
		var content= e.target.value;
		if(content.length > 20){
			content= content.substring(0, 17)+"...";
		}
		$('#paste_name').val(content);
	}
	matchModules();
});

$('body').on('click', '.module-header', function(e){
	var module_body= $(this).parent().children('.module-body');
	
	if(module_body.is(":hidden")){
		refreshModule(module_body);
	}
	module_body.toggle();
});

$('body').on('click', '.module-star', function(e){
	$(this).toggleClass('glyphicon-star');
	$(this).toggleClass('glyphicon-star-empty');	
	e.stopPropagation();
});


function refreshModule(module_body){
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

function matchModules(){
	var paste_content= $('#paste_content').val();
	
	$.ajax({
		type: "POST",
		contentType: "application/json; charset=utf-8",
		url: "/module/match",
		data: JSON.stringify({data: paste_content}),
		success : function(text)
		{
			$('#modules-container').html(text);
		}
	});
}


