$(function(){
    var name=$("#name").focus();

    $("#po_form").submit(function(){
        $("[placeholder]").each(function(){
            if(this.value==this.placeholder){
                this.value='';
            }
        })
        if(name.val()==''){
            alert("没有标题 , 不可以 ...")
            name.focus()
            return false
        }
    })


    var win = $(window),
        txt = $("#txt");
    
    function txtresize() {
        var inpo = $("#po_btn"),
        h = Math.max(win.height() - inpo.height() - txt.offset().top - 50, 250);
        txt.height(h)
    }
    txtresize()
    win.resize(txtresize)

    $("#rm").click(function(){
        if(!confirm("删除 , 确定 ?")){
            return false
        }
    }) 

    $("#txt").bind("keydown",insertTab);
})

$(function(){
    autocomplete_tag('#search', [['减肥',10226353]], 0)
    function show_placeholder(){
        if(!$('#token-input-search').val().length>0 && !$('.token-input-token').length>0){
            $('.token-input-list').hide()
            $('#search').val("").show()
            $('#token-input-search').unbind('blur')
        }
        if(document.activeElement.id!='token-input-search'){
            $('.token-input-dropdown').hide()
        }
    }
    function show_token_input(){
        $('#token-input-search').focus().blur(show_placeholder).focus(function(){
            if($('#token-input-search').val().length>0)
            $('.token-input-dropdown').show()}
        )
    }
    show_placeholder()
    $('#search').bind('click',function(){
        $(".token-input-list").show()
        $(this).hide()
        if(navigator.userAgent.indexOf("MSIE")>0) { 
            setTimeout(show_token_input,10)
        }else{
            show_token_input()
        }
    })
    $('#search').show().click()

    $('.po_btn').click(function(){
        if($('.token-input-token').length>0 && $('#tag_cid').val()==0){
            alert('请选择类别')
        }else{
           $('form')[0].submit() 
        }
    })
})

