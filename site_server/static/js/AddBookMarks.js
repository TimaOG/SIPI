const items_bookmarks = document.querySelectorAll('.bookmarksItem');
function AddBookMarks(){
    for (var item in items_bookmarks){
        if(document.getElementById("imgClickAndChange").src == "../static/icons/bookmark_dis.png"){
            console.log("Yes");
        }else{
            document.getElementById("imgClickAndChange").src = "../static/icons/bookmark_active.png"
        }
        console.log(items_bookmarks[item]);
    }
}
