function popreply(cid, title_html, href, counter){
    var content = $(
        '<div class="fcmpop" id="reply_reply_pop"><a target="_blank" id="reply_name"></a><div id="reply_reply_body" class="reply_reply_loading"></div><textarea></textarea><div class="tr"><span class="ctrl_enter_hint"></span><span class="btnw"><button type="submit" class="button">回复</button></span></div></div>'
        ),
        link = '<a href="'+href+'" class="pop_reply_po_link" target="_blank"></a>',
        hint = 'Ctrl + Enter 直接提交',
        cbody = content.find('#reply_reply_body'), 
        t=cbody[0],
        textarea = content.find('textarea'),
        fancybox = $.fancybox,
        button = content.find('button'),
        reply_name=content.find('#reply_name'),
        id = href.split("/")[4].split("#")[0],
        count=true,
        ctrl_enter_hint=content.find(".ctrl_enter_hint").html(link)

        if(counter){
            count=counter.html()
            if(count.length){
                count-=0
            }else{
                count=0
            }
        }
    function btc(){
        var v=textarea.val(), 
            fancybox=$.fancybox;
        if(!v.length)return;
        textarea.val('')
        fancybox.showActivity();
        post_reply(id, v,function(data){
            fancybox.hideActivity();
            textarea.focus()
            _result(data)
            if(counter){
                count+=1
                counter.html(count)
            }
        })
    }
    textarea.focus(function(){ctrl_enter_hint.html(hint)}).blur(function(){ctrl_enter_hint.html(link)}).ctrl_enter(btc);
    reply_name.html(title_html).attr('href',href)

    button.click(btc)
    function _(data){
        if(data.cid==61){
            reply_name.remove()
        }else{
            reply_name.text(data.name)
        }
        _result(data.result,1)
    }
    function _h0(){
        cbody.css('height',0).removeClass('reply_reply_loading')
    }
    function _result(result,i){
        if(result.length){
            cbody.removeClass('reply_reply_loading').append(render_reply(result,i))
            codesh()
            var height = t.scrollHeight+2, 
                winheight=$(window).height() - 260;

            if(height>winheight){
                height = winheight;
            }else{
                cbody.css("padding","0")
            }

            cbody.css({
                height:height
            })
            if(count===true){ //有count的就从第一个开始显示
                t.scrollTop=t.scrollHeight-t.offsetHeight-5
            }
        }else{
            _h0()
        }
        fancybox.resize()
    }
    if(!count){
        _h0()
    }
    fancybox({
        content:content, 
        onComplete:function(){
            textarea.focus()
            if(count){ 
                $.getJSON( '/j/po-'+cid+'/json/'+id, _)
            }
        }
    })
}


$(function(){
    $(".bzreply").live("click",function(){
        var self=$(this)
        popreply(
            "reply",
            self.parents('.readpad').find('.readtitle').html(),
            this.href,
            self.find('.count')
        )
        return false
    })
})

function recreply(elem){
    popreply(
        "reply",
        '',
        elem.href
    )
    return false
}
