(function(){
    var mail=$("#mail");
    if(mail.val()==''){
        mail.focus();
    }else{
        $('#password').focus();
    }
    function load(ico_list){
        var t=ico_list.shift();
        ico_list.push(t);
        $('#zsite_ico').tmpl([t]).appendTo("#zsite_list");
    }

     zsite_ico_list = function(ico_list){
        for(var i=0;i<4;++i){
            load(ico_list)
        }
        function _(){
            var t = $('#zsite_list .zsite_ico:first')
            t.slideUp(function(){
                $(this).remove()
                load(ico_list)
                setTimeout( _ , 1000)
            })
        }
        setTimeout( _ , 200)
    }
})()



