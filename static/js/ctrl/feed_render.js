/*
61 word
62 note
*/
(function (){
var FEED_ATTR_BASE = "id zsite rt_list zsite_id cid reply_total create_time name is_rt vote_state vote",
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

    var feed_load=$("#feed_load"), feed_loading=$("#feed_loading"), begin_id = $("#begin_id").val(0),feed_finish;
    function render_feed(){
        if(feed_finish)return;
        feed_load.hide()
        feed_loading.show()
        $.postJSON(
        "/j/feed/"+begin_id.val(),
        function(result){
            if(!result.length){
                feed_finish = true;
                feed_load.hide()
                feed_loading.hide()
                return
            }
            $('#feed').tmpl(init_result(result)).appendTo("#feeds");
            feed_loading.slideUp(function(){
                feed_load.show()
            });
            begin_id.val(result[result.length-1][0])
        })
    }
    render_feed()
    $("#feed_load").click(render_feed)
})()
function feed_load(){

}
