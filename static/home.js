let openMenu = document.querySelector('.hamburger-icon')
let closeMenu = document.querySelector('.menu-close')
let menu = document.querySelector('.menu')
let comp =document.querySelector('.comp')
let links = document.querySelector('.links_quick')
let openMobile = document.querySelector('.profile_mobile')
let profile = document.querySelector('.profile_mob')
let closeMobile = document.querySelector('.closeMobile')

openMenu.addEventListener('click', () => {
    menu.style.width = '50vw'
  })
  closeMenu.addEventListener('click', () => {
    menu.style.width = '0%'
  })

  comp.addEventListener('click' , () =>{
    links.classList.toggle('toggle')
  })

  profile.addEventListener('click', () => {
    openMobile.style.width = '100vw'
  })
  closeMobile.addEventListener('click', () => {
    openMobile.style.width = '0%'
  })
  