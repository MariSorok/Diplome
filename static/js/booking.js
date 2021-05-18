if(localStorage.getItem('test') == null){

}else{
    document.getElementById('date').value = localStorage.getItem('test')
}



function Reserv(e){
  let popup = document.getElementById('popup')
  let y = e.getAttribute('data-value');
  let x = e.getAttribute('data-user');
  console.log(x)
  console.log(1111)
  document.getElementById('bookingForm__content_map').style.marginTop = 10+'px'
  popup.style.visibility = 'visible'
  document.getElementById('table_number').innerHTML = y
  document.getElementById('popup_date').innerHTML = document.getElementById('date').value
  document.getElementById('date_book').value = document.getElementById('date').value
  // document.getElementById('popup_time').innerHTML = document.getElementById('time').value
  document.getElementById('popup_piople').innerHTML = document.getElementById('piople').value
  document.getElementById('num_book').value = document.getElementById('piople').value
  document.getElementById('num_table').value = y

  if (x == "close") {
    document.getElementsByClassName('popup_button')[0].style.visibility = "hidden"
    document.getElementById('popup').style.background = '#b8484fc0'
  }else{
    document.getElementsByClassName('popup_button')[0].style.visibility = "visible"
    document.getElementById('popup').style.background = '#B38867'
  }
}

function Close_popup(){
  let popup = document.getElementById('popup')
  popup.style.visibility = 'hidden'
  document.getElementById('bookingForm__content_map').style.marginTop = -150+'px'
}
