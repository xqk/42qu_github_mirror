$("input[name=name]").focus(function(){
    $('#tag0').attr('checked',true)
}).defaultValue();

function tag(){
    $.fancybox({
        content:''
    })
}
