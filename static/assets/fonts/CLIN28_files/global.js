
$(document).ready(function () {
    $('#map').addClass('scrolloff');                // set the mouse events to none when doc is ready

    $('#overlay-map').on("mouseup",function(){          // lock it when mouse up
        $('#map').addClass('scrolloff');
        //somehow the mouseup event doesn't get call...
    });
    $('#overlay-map').on("mousedown",function(){        // when mouse down, set the mouse events free
        $('#map').removeClass('scrolloff');
    });
    $("#map").mouseleave(function () {              // becuase the mouse up doesn't work...
        $('#map').addClass('scrolloff');            // set the pointer events to none when mouse leaves the map area
                                                    // or you can do it on some other event
    });

});

$(document).ready(function(){
var my_posts = $("[rel=tooltip]");

var size = $(window).width();
for(i=0;i<my_posts.length;i++){
    the_post = $(my_posts[i]);

    if(the_post.hasClass('invert') && size >=767 ){
        the_post.tooltip({ placement: 'left'});
        the_post.css("cursor","pointer");
    }else{
        the_post.tooltip({ placement: 'rigth'});
        the_post.css("cursor","pointer");
    }
}
});

$(function () {
    var active = true;
    $('#day1').on('show.bs.collapse', function () {
        if (active) $('#day1 .in').collapse('hide');
    });
});
$(function () {
    var active = true;
    $('#day2').on('show.bs.collapse', function () {
        if (active) $('#day2 .in').collapse('hide');
    });
});



$('#registerform').submit(function() {
    if ($("#registerform input:checkbox:checked").length > 0)
    {
          $('#loading').css('visibility', 'visible');
          return true;
    }
    else
    {
         alert('Please choose at least one event')
         return false;
    }

});
