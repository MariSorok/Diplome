let selector_count1 = 0;
let selector_count2 = 0;
function Selector_profile(e){
  let thisValue = e.getAttribute('data-value')
  let carousel_item = document.querySelectorAll('.account_carousel')
  if(thisValue != selector_count1){
    let allSelectorAction = document.querySelectorAll('.account__selector_item_active')
    allSelectorAction[0].classList.remove('account__selector_item_active')
    e.classList.add('account__selector_item_active')

    for (var i = 0; i < carousel_item.length; i++) {
      if(carousel_item[i].getAttribute('data-value') == thisValue){
        carousel_item[selector_count1].classList.remove('active')
        carousel_item[i].classList.add('active')
      }
    }

    selector_count1 = thisValue
  }
}


function Selector_events(e){
  let thisValue = e.getAttribute('data-value')
  let carousel_item = document.querySelectorAll('.events_carousel')
  if(thisValue != selector_count2){
    let allSelectorAction = document.querySelectorAll('.events__selector_item_active')
    allSelectorAction[0].classList.remove('events__selector_item_active')
    e.classList.add('events__selector_item_active')

    for (var i = 0; i < carousel_item.length; i++) {
      if(carousel_item[i].getAttribute('data-value') == thisValue){
        carousel_item[selector_count2].classList.remove('active')
        carousel_item[i].classList.add('active')
      }
    }

    selector_count2 = thisValue
  }
}

function enterButton(e){
  let thisValue = e.getAttribute('data-value')
  let carousel_item = document.querySelectorAll('.account_carousel')
  let account__selector_item = document.querySelectorAll('.account__selector_item')

  if(thisValue != selector_count1){
    let allSelectorAction = document.querySelectorAll('.account__selector_item_active')
    allSelectorAction[0].classList.remove('account__selector_item_active')
    account__selector_item[1].classList.add('account__selector_item_active')

    for (var i = 0; i < carousel_item.length; i++) {
      if(carousel_item[i].getAttribute('data-value') == thisValue){
        carousel_item[selector_count1].classList.remove('active')
        carousel_item[i].classList.add('active')
      }
    }

    selector_count1 = thisValue
  }
}

function registrationButton(e){
  let thisValue = e.getAttribute('data-value')
  let carousel_item = document.querySelectorAll('.account_carousel')
  let account__selector_item = document.querySelectorAll('.account__selector_item')

  if(thisValue != selector_count1){
    let allSelectorAction = document.querySelectorAll('.account__selector_item_active')
    allSelectorAction[0].classList.remove('account__selector_item_active')
    account__selector_item[0].classList.add('account__selector_item_active')

    for (var i = 0; i < carousel_item.length; i++) {
      if(carousel_item[i].getAttribute('data-value') == thisValue){
        carousel_item[selector_count1].classList.remove('active')
        carousel_item[i].classList.add('active')
      }
    }

    selector_count1 = thisValue
  }
}

function Nav(e){
  let nav_item = document.querySelectorAll('.nav-item')

  for (var i = 0; i < nav_item.length; i++) {
    nav_item[i].classList.remove('active')
  }

  e.classList.add('active')
}

function Enter() {
  let login = document.getElementById('login').value;
  if (login == 'client') {
    window.location.href = './client_profile.html';
  }
  if (login == 'worker') {
    window.location.href = './worker_profile.html';
  }
  if (login == 'admin') {
    window.location.href = './admin_profile.html';
  }
}
