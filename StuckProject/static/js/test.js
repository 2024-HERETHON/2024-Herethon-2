document.addEventListener("DOMContentLoaded", function () {
    
    const resultbtn = document.querySelector(".gotoresult");
    const result = document.querySelector(".result");
    const download = document.querySelector(".download");
    const test = document.querySelector(".test_main .wrap");
    resultbtn.addEventListener("click", ()=>{
        result.classList.remove("nodisplay");
        download.classList.add("nodisplay");
        test.classList.add("gray");
        
        resultbtn.classList.add("nodisplay");
        window.scrollTo({
            top: 0,
            behavior: 'smooth'  
        });
    })
    window.scrollTo({
        top: 0,
        behavior: 'smooth'  
    });
})