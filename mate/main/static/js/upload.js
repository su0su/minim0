for(i = 1 ; i <= 3 ; i++){
    $('#box0'+i).click(function(){
      $(this).find('.cont').toggle();
    });
  }