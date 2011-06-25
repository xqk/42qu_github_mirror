/*
61 word
62 note
*/
(function (){
var FEED_ATTR_BASE = "id zsite rt_list zsite_id cid reply_count create_time name pic vote_state vote",
    FEED_ATTR = {
        61:FEED_ATTR_BASE,
        62:FEED_ATTR_BASE+" txt",
        63:FEED_ATTR_BASE
    };

    for(var i in FEED_ATTR){
        FEED_ATTR[i]=FEED_ATTR[i].split(' ')
    }

    function array2zsite(a){
        return {
            name: a[0],
            link: a[1]
        } 
    }

    function init(result){
        var data = {},
        i=0,
        attr=FEED_ATTR[result[4]];

        for(;i<attr.length;++i){
            data[attr[i]] = result[i]
        }
        data.zsite = array2zsite(data.zsite);
        data.link = "/po/"+data.id;
        data.rt_list = $.map(data.rt_list, array2zsite);
        data.create_time = $.timeago(data.create_time) 
        return data
    }

    function init_result(result){
        var length = result.length, item=[], i=0;

        for(;i<length;++i){
            item.push(init(result[i]))
        }
        return item 
    }

    var feed_load=$("#feed_load").click(function(){
        render_feed()
        feed_load.hide()
        autocount=0;
    }), feed_loading=$("#feed_loading"), begin_id = $("#begin_id").val(0),is_loading=0, autocount=0;
    function render_feed(){
        if(is_loading)return;
        is_loading = 1;
        feed_load.hide()
        feed_loading.show()
        $.postJSON(
        "/j/feed/"+begin_id.val(),
        function(result){
            if(!result.length){
                feed_load.hide()
                feed_loading.hide()
                return
            }
            is_loading=0;
            $('#feed').tmpl(init_result(result)).appendTo("#feeds");
            feed_loading.slideUp(function(){
                feed_load.show()
            });
            begin_id.val(result[result.length-1][0])
        })
    }
    render_feed()
    var win = $(window)
    win.scroll(function() {
        if (
           autocount < 5 && !is_loading && win.scrollTop() > ($(document).height() - win.height() * 2)
        ){
            autocount += 1;
            render_feed();
        }

    });
    /*************/
    var po_word_tip = $("#po_word_tip"), po_word_txt = $("#po_word_txt"), po_word_max = 142, po_word_txt_bg="po_word_txt_bg";
    function po_word_update(value){
        var len = cnenlen(value),
            html, diff=0;
        if(len){
            diff = len-po_word_max; 
            if(diff>0){
    html = '<span style="color:red">超出<span>'+diff+"</span>字</span>"
            }else{
    html = "<span><span>"+len+"</span>字</span>"
    //为了ie6 多加一层span
            }
        }else{
    html = ''
        }
        po_word_tip.html(html);
        return diff
    }
    po_word_txt.blur().val('').focus(function(){
        $(this).removeClass(po_word_txt_bg)
    }).input(function po_word_change(){
        po_word_update(this.value)
    }).blur(function(){
        var self=$(this), val=self.val();
        if(!val||!val.length){
            self.addClass(po_word_txt_bg)
        }
    })
    .addClass(po_word_txt_bg)
    ;

    $("#po_word_form").submit(function(){
        if(po_word_update(po_word_txt.val())>0){
            po_word_txt.focus()
            return false
        }
    })

})()
