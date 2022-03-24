
let handleToggle = () => {
    document.querySelector('.bars').classList.toggle('active')
    document.querySelector('.accaunt-navigator-hidden-container').classList.toggle('active')
    document.querySelector('.accaunt-navigator-hidden').classList.toggle('active')
}

// Slider 






let modal = document.querySelector('.modal_')
let modal_btn = document.querySelector('.modal_btn')
let btn_close = document.querySelector('.btn_close')



modal_btn.addEventListener('click', ()=>{
    modal.classList.remove('d-none')
    modal.classList.add('d-flex')
 
})
btn_close.addEventListener('click', ()=>{
    modal.classList.add('d-none')
    modal.classList.remove('d-flex')

 
})





