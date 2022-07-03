// let ul = document.getElementsByClassName("main_body");
// let li = ul.querySelectorAll('.main_body.main_body_jobs')
let input = document.getElementsByClassName('nav_input');
const image_input = document.querySelector("#image-input");
const listArray = Array.from(li);



// const filterUsers = (event) => {
//   ul.innerHTML = ""
//   let keyword = input.value.toLowerCase();
//   listArray.forEach((item) => {
//     if (item.textContent.toLowerCase().includes(keyword)) {
//       ul.appendChild(item)
//     }
//   })
// }

// input.addEventListener('keyup', filterUsers);


image_input.addEventListener("change", function () {
  const reader = new FileReader();
  reader.addEventListener("load", () => {
    const uploaded_image = reader.result;
    document.querySelector("#display-image").style.backgroundImage = `url(${uploaded_image})`;
  });
  reader.readAsDataURL(this.files[0]);
});





