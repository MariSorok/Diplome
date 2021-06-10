document.getElementById('date').valueAsDate = new Date();

document.getElementById('time').value = "15:12";

function Reserv(e){
  let popup = document.getElementById('popup')
  let y = e.getAttribute('data-value');
  let x = e.getAttribute('data-user');
  document.getElementById('table_number').innerHTML = y
  if (x == "close") {
    popup.style.visibility = 'visible'
    document.getElementById('bookingForm__content_map').style.marginTop = 10+'px'
    document.getElementsByClassName('popup_button')[0].style.visibility = "hidden"
    document.getElementById('popup').style.background = '#b8484fc0'
  }else{
    popup.style.visibility = 'hidden'
    document.getElementById('bookingForm__content_map').style.marginTop = -150+'px'
    document.getElementsByClassName('popup_button')[0].style.visibility = "visible"
    document.getElementById('popup').style.background = '#B38867'
  }
}

function Close_popup(){
  let popup = document.getElementById('popup')
  popup.style.visibility = 'hidden'
  document.getElementById('bookingForm__content_map').style.marginTop = -150+'px'
}
