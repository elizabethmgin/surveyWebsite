$(document).ready(function(){
  $('#rating-0').click(function() {
    $('#dialog').dialog('open');
  });
  
  $('#dialog').dialog({
    autoOpen: false,
    height: 280,
    modal: true,
    resizable: false,
    buttons: {
      Share: function() {
        $(this).dialog('close');
        // Submit Rating
      }
    }
  });
  
  
});

$(document).ready(function(){
  $(':submit').click(function(e) {
    $(':input').each(function() {
      if($(this).val().length == 0) {
        $(this).css('border', '2px solid red');
      }
    });
    e.preventDefault();
  });
});
