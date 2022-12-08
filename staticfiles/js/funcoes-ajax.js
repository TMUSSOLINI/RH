function utilizouHoraExtra(id){
    console.log(id);
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;
    $.ajax({
        type: 'POST',
        url: '/hora-extra/utilizou-hora-extra/'+ id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log(result)
            $("#mensagem").text("foi");
        }
    });
}