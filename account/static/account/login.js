const form = document.querySelector("form");
eField = form.querySelector(".Username"),
eInput = eField.querySelector("input"),
pField = form.querySelector(".password"),
pInput = pField.querySelector("input");

form.onsubmit = (e)=>{
  e.preventDefault(); 
  if(eInput.value == "" || pInput.value == ""){
    (eInput.value == "") ? eField.classList.add("shake", "error") : eField.classList.remove("shake", "error");
    (pInput.value == "") ? pField.classList.add("shake", "error") : pField.classList.remove("shake", "error");
  }
  else {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", form.action);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log("Form successfully submitted");
            var response = JSON.parse(xhr.responseText);
            if (response.success) {
                // redirect to specified page
                window.location.href = response.redirect_url;
            } else {
                alert(response.error);
            }
        }
    };
    var data = new FormData(form);
    xhr.send(data);
  }

  setTimeout(()=>{ 
    eField.classList.remove("shake");
    pField.classList.remove("shake");
  }, 500);

  eInput.onkeyup = ()=>{checkEmail();} 
  pInput.onkeyup = ()=>{checkPass();} 


  function checkPass(){
    if(pInput.value == ""){
      pField.classList.add("error");
      pField.classList.remove("valid");
    }else{
      pField.classList.remove("error");
      pField.classList.add("valid");
    }
  }

}
