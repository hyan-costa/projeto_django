
let sidebar = document.querySelector(".sidebar");
let closeBtn = document.querySelector("#btn");
let searchBtn = document.querySelector(".bx-search");
window.onload=function(){
    closeBtn.addEventListener("click", ()=>{
        sidebar.classList.toggle("open");
        menuBtnChange();
    });

    // searchBtn.addEventListener("click", ()=>{
    //     sidebar.classList.toggle("open");
    //     menuBtnChange();
    // });
}

function menuBtnChange() {
if(sidebar.classList.contains("open")){
    closeBtn.classList.replace("bx-menu", "bx-menu-alt-right");
}else {
    closeBtn.classList.replace("bx-menu-alt-right","bx-menu");
}
}

// função  button acoes globais: apagar / aletrar / incluir
$(document).ready(function (){
    $('.acoes').mouseover(function (){
        if(this.id == 'apagar'){
            $(this).css('background-color', 'rgba(238, 8, 8, 0.59)')
        }
        else if(this.id == 'alterar'){
            $(this).css('background-color','rgba(255, 204, 0, 0.59)')
        }
    })
    $('.acoes').mouseout(function (){
        if(this.id == 'apagar'){
            $(this).css('background-color', 'white')
        }
        else if(this.id == 'alterar'){
            $(this).css('background-color','white')
        }
    })
})
