let btn = document.querySelector('.btn')
let form = document.querySelector('.form')
let inpt = document.querySelector('.input1')
let inpt1 = document.querySelector('.input2')
const image_input = document.querySelector("#image-input");
let inpt2 = document.querySelector('.input3')
let inpt3 = document.querySelector('.input4')
let inpt4 = document.querySelector('.input6')

image_input.addEventListener("change", function() {
    const reader = new FileReader();
    reader.addEventListener("load", () => {
      const uploaded_image = reader.result;
      document.querySelector("#display-image").style.backgroundImage = `url(${uploaded_image})`;
    });
    reader.readAsDataURL(this.files[0]);
  });
    form.addEventListener("input", function (e) {
        if (inpt.value.trim() && inpt1.value.trim() && inpt2.value.trim() && inpt3.value.trim() && inpt4.value.trim() === 0) {
            btn.disabled = true
            btn.style.cursor = 'no-drop'
            btn.style.backgroundColor = 'white'
            btn.style.color = 'black'
        } else {
            btn.disabled = false
            btn.style.backgroundColor = '#8325B0'
            btn.style.color = '#FFFFFF'
            btn.style.cursor = 'pointer'
        }
    })


    // function updateSubmitBtn(){
    //     const firstNameValue = input.value.trim();
    //     const countryValue = input1.value.trim();
    //     const commentValue = input2.value.trim();
    //     const skillsValue = input3.value.trim();

    //     if(firstNameValue && countryValue && commentValue && skillsValue){
    //       btn.removeAttribute('disabled');
    //     }else {
    //       btn.setAttribute('disabled', 'disabled');
    //     }
    //   }
      
    //   firstName.addEventListener('change', updateSubmitBtn);
    //   countryValue.addEventListener('change', updateSubmitBtn);
    //   comment.addEventListener('change', updateSubmitBtn);
    //   skillsValue.addEventListener('change', updateSubmitBtn);




//if (input.value.length <= 0){
    //         btn.disabled = true
    //   console.log('good')
    //     } else{
    //         console.log('gooder')
    //         btn.classList.add
    //     }