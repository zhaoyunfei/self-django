/**
 * Created by 疯小埋 on 17/9/14.
 */

$(document).ready(function (){
    $(".line-operation").click(function (){
        $('html, body').animate({
            scrollTop: $(".menu_list").offset().top
        }, 500);
    });
});