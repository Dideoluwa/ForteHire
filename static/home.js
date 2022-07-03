let openMenu = document.querySelector('.hamburger-icon')
let closeMenu = document.querySelector('.menu-close')
let menu = document.querySelector('.menu')

openMenu.addEventListener('click', () => {
    console.log('good')
    menu.style.width = '50vw'
  })
  closeMenu.addEventListener('click', () => {
    menu.style.width = '0%'
  })
  