const items = document.querySelectorAll('.saleyear');
for (var item in items){
    if (items[item].innerText.includes("−")){
        items[item].classList.add('red');
    }else{
        items[item].classList.add('green');
    }
}

