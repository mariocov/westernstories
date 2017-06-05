var csrftoken = $('meta[name=csrf-token]').attr('content')
var loading = $('.loader').hide();
var message = $('.message').hide();

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken)
        }
    }
})

$(document).ready(function(){

  $("button").click(function(){
    loading.show()
    $.ajax({
      type: 'POST',
      url: "/quote",
      dataType: 'json',
      success: function(data){
        setTimeout(function(){
          loading.hide()
          message.hide()
          $(".story p").html(data);
          ga('send', 'pageview');
        },200);
      },
    });
});
});
