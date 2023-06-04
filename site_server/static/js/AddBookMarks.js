function AddBookMarks(button){
    var imgElement = button.querySelector('.imgClickAndChange');
    imgElement.src = '../static/icons/bookmark_active.png';
    if (imgElement.src == '../static/icons/bookmark_active.png')
    {
        imgElement.src = '../static/icons/bookmark_dis.png';
    }
    else
    {
        imgElement.src = '../static/icons/bookmark_active.png';
    }
}
