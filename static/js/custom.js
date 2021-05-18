$('.field input').on('checkval', function () {
  let label = $(this).next('label');

  if(this.value !== '') {
    label.addClass('show');
  if (this.name == 'summ_to_cabinet') {
    if ( this.value  > $(this).data('limit')) {
      $(this).closest('.cabinet_form').find('.ooops').html('Не хватает средств');
      $(this).closest('.cabinet_form').find('.right .bonus .summ').html("0 <span class='ruble'>₽</span>");
      $(this).closest('.cabinet_form').find('.right .bonus').fadeOut(300);
    } else {
      $(this).closest('.cabinet_form').find('.ooops').html('');
      $(this).closest('.cabinet_form').find('.right .bonus .summ').html(Math.floor(this.value / 10) + " <span class='ruble'>₽</span>");
      $(this).closest('.cabinet_form').find('.right .bonus').fadeIn(300);
    }
  }
  if (this.name == 'account_address') {
    $('.cabinet .users .ooops').html('Пользователь не найден');
  }
  if (this.name == 'summ_to_payment') {
    $(this).closest('form').find('.item1 span.digit').html(Math.ceil(this.value * $(this).data('com')));
  }

  } else {
    label.removeClass('show');

  if (this.name == 'summ_to_cabinet') {
    $(this).closest('.cabinet_form').find('.ooops').html('');
    $('.cabinet_form .right .bonus .summ').html("0 <span class='ruble'>₽</span>");
    $('.cabinet_form .right .bonus').fadeOut(300);
  }

  if (this.name == 'account_address') {
    $('.cabinet .users .ooops').html('');
  }
  if (this.name == 'summ_to_payment') {
    $(this).closest('form').find('.item1 span.digit').html(0);
  }
  }
}).on('keyup', function () {
  $(this).trigger('checkval');
});
