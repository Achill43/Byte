$(document).ready(function()
{
    var menuShow=false;
    var myHeight = $(window).height();
    //$("#myHeader").height(myHeight);
    console.log("Program by ÂхиλΛ ;)");
    //$("#mainMenu").hide(0);
    $('#showMenu').on('click', function(){
        menuShow=!menuShow;
        $(this).toggleClass("is-active");
        $(".mainMenu").toggleClass("nav-active");
        $("body").toggleClass("body-active");
    });
    $('#scrollHesader').on('click', function(e){
        $('html,body').stop().animate({ scrollTop: $('#content').offset().top }, 1000);
        e.preventDefault();
      });
      //нумерация строк для тєгов code и pre
    (function() {
        var pre = document.getElementsByTagName('pre'),
            pl = pre.length;
        for (var i = 0; i < pl; i++) {
            pre[i].innerHTML = '<span class="line-number"></span>' + pre[i].innerHTML + '<span class="cl"></span>';
            var num = pre[i].innerHTML.split(/\n/).length;
            for (var j = 0; j < num; j++) {
                var line_num = pre[i].getElementsByTagName('span')[0];
                line_num.innerHTML += '<span>' + (j + 1) + '</span>';
            }
        }
    })();
});