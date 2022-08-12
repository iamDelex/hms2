let body = document.querySelector('body');
let light = document.querySelector('.light');
let moon = document.querySelector('.fa-moon');

light.addEventListener('click', ()=>{
    body.classList.toggle('dark')
    if(body.classList.contains('dark')){
        icon.classList.replace('fa-moon', 'fa-sun')
    }else{
        icon.classList.replace('fa-sun', 'fa-moon')
    }
})