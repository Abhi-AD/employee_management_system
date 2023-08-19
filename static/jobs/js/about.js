let accordion = document.getElementById("accordion")
let button = document.getElementById("btn")

accordion.style.display="none"
accordion.style.transition=".5s ease-in-out"
button.addEventListener("click",() =>{
     accordion.style.display = "block"
     accordion.style.transition=".5s ease-in-out"
})


