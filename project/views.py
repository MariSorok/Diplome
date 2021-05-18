from typing import ContextManager
from django.http import HttpResponseRedirect, request
from django.shortcuts import render
from django.views import View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.db.models import Max, Min

from project.models import Booking, Table, Dish, Preorder
from project.forms import DishForm

User = get_user_model()


class MainView(View):
    template_name = 'main.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        data = request.POST
        context = {}

        if request.POST.get("button") == "1":
            user = User.objects.create_user(data.get('login'), data.get('email'), data.get('password1'))
            user.profile.phone = data.get('phone')
            user.save()

            if user.profile.perm == "CLI":
                return HttpResponseRedirect('/client-profile/')
            if user.profile.perm == "ADM":
                return HttpResponseRedirect('/admin_profile/')
            if user.profile.perm == "WOR":
                return HttpResponseRedirect('/worker-profile/')

        if request.POST.get("button") == "2":
            user = authenticate(request, username=data.get('login'), password=data.get('password'))
            if user is not None:
                login(request, user)
            else:
                context = {'error': "Неправильные параметры входа. Проверьте логин и пароль."}
                print("Неправильные параметры входа. Проверьте логин и пароль.")
                return render(request, self.template_name, context)

            if user.profile.perm == "CLI":
                return HttpResponseRedirect('/client-profile/')
            if user.profile.perm == "ADM":
                return HttpResponseRedirect('/admin_profile/')
            if user.profile.perm == "WOR":
                return HttpResponseRedirect('/worker-profile/')

        if request.POST.get("button") == "3":
            pass

        return render(request, self.template_name, context)


@method_decorator([login_required], name='dispatch')
class WorkerView(View):
    template_name = 'worker_profile.html'

    def get_context(self):
        context = {}
        bookings = Booking.objects.filter(status='AC', closed=False)
        context['bookings'] = bookings
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        booking_id = request.POST.get('delete')
        booking = Booking.objects.get(id=booking_id)
        booking.closed = True
        booking.save()

        context = self.get_context()
        return render(request, self.template_name, context)



@method_decorator([login_required], name='dispatch')
class AdminView(View):
    template_name = 'admin_profile.html'
    form = DishForm()

    def get_context(self):
        context = {}
        context['dish'] = self.form
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        print(self.form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = request.POST

        if data.get('login'):
            user = User.objects.create_user(data.get('login'), data.get('email'), data.get('password1'))
            user.profile.phone = data.get('phone')
            user.profile.perm = "WOR"
            user.save()

            for table_num in range(int(data.get('table_from')), int(data.get('table_to'))+1):
                try:
                    table = Table.objects.get(number=table_num)
                    table.user = user
                    table.save()
                except Table.DoesNotExist:
                    pass
        if data.get('image'):
            form = DishForm(request.POST)
            dish = form.save()

        
        print(request.POST)

        return render(request, self.template_name)
    


@method_decorator([login_required], name='dispatch')
class ConfirmationView(View):
    template_name = 'admin_confirmation.html'

    def get_context(self):
        context = {}
        bookings = Booking.objects.filter(status='WA', closed=False)
        print(bookings)
        context['bookings'] = bookings
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        print(request.POST)

        if request.POST.get('disline'):
            booking_id = request.POST.get('disline')
            booking = Booking.objects.get(id=booking_id)
            booking.status = "RE"
            booking.save()
        if request.POST.get('accept'):
            booking_id = request.POST.get('accept')
            booking = Booking.objects.get(id=booking_id)
            booking.status = "AC"
            booking.save()

        context = self.get_context()
        return render(request, self.template_name, context)


@method_decorator([login_required], name='dispatch')
class EditMenuView(View):
    template_name = 'edit_menu.html'
    form = DishForm()

    def get_context(self):
        context = {}
        context['form'] = self.form
        context['dishes'] = Dish.objects.all()
        context['snaks'] = Dish.objects.filter(category="SNA")
        context['hot'] = Dish.objects.filter(category="HOT")
        context['drinks'] = Dish.objects.filter(category="DRI")
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        print(self.form)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = request.POST

        if data.get('save'):
            dish = Dish.objects.get(id=data.get('save'))
            dish.category = data.get('category')
            dish.name = data.get('name')
            dish.description = data.get('description')
            dish.price = data.get('price')
            dish.save()
        if data.get('delete'):
            dish = Dish.objects.get(id=data.get('delete'))
            dish.delete()
        
        print(request.POST)
        context = self.get_context()
        return render(request, self.template_name, context)


@method_decorator([login_required], name='dispatch')
class HistoryView(View):
    template_name = 'admin_history.html'

    def get_context(self):
        context = {}
        context['bookings'] = Booking.objects.filter(closed=True)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        pass
        

@method_decorator([login_required], name='dispatch')
class WorkerEditView(View):
    template_name = 'worker_editProfile.html'

    def get_context(self, request):
        context = {}
        min = Table.objects.filter(user=request.user).aggregate(Min('number'))
        max = Table.objects.filter(user=request.user).aggregate(Max('number'))
        context['table_from'] = min.get('number__min')
        context['table_to'] = max.get('number__max')
        context['profile'] = request.user
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context(request)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data)
        user = User.objects.get(id=request.user.id)
        user.username = data.get('login')
        user.email = data.get('email')
        user.profile.phone = data.get('phone')
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        # , data.get('email'), data.get('password1'))
        # user.profile.phone = data.get('phone')
        # user.profile.perm = "WOR"
        user.save()
        if data.get('table_from'):
            for table_num in range(int(data.get('table_from')), int(data.get('table_to'))+1):
                try:
                    table = Table.objects.get(number=table_num)
                    table.user = user
                    table.save()
                except Table.DoesNotExist:
                    pass

        context = self.get_context(request)
        return render(request, self.template_name, context)


from datetime import date

today = date.today()

@method_decorator([login_required], name='dispatch')
class ClientProfileView(View):
    template_name = 'client_profile.html'

    def get_context(self, request, date=today):
        context = {}
        # context['i'] = list(Table.objects.filter(booking=True, date).values_list('number', flat=True))
        date = str(date).split('-')
        context['tables'] = Table.objects.all()
        context['i'] = Table.objects.filter(booking__booked_at__year=date[0], 
                                            booking__booked_at__month=date[1], 
                                            booking__booked_at__day=date[2])
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context(request)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data)
        date_time = data.get('date')        
        context = self.get_context(request, date_time)

        if data.get('comment'):
            Booking.objects.create(
                persons_num=data.get('num'),
                booked_at=data.get('date'),
                status="WA",
                user=request.user,
                table=Table.objects.get(number=data.get('num_table')),
                preorder=Preorder.objects.create(number=1, dishes=data.get('comment')),
            )
        return render(request, self.template_name, context)



@method_decorator([login_required], name='dispatch')
class ClientEditView(View):
    template_name = 'client_editProfile.html'

    def get_context(self, request):
        context = {}
        # min = Table.objects.filter(user=request.user).aggregate(Min('number'))
        # max = Table.objects.filter(user=request.user).aggregate(Max('number'))
        # context['table_from'] = min.get('number__min')
        # context['table_to'] = max.get('number__max')
        context['profile'] = request.user
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context(request)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data)
        user = User.objects.get(id=request.user.id)
        user.username = data.get('login')
        user.email = data.get('email')
        user.profile.phone = data.get('phone')
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        # , data.get('email'), data.get('password1'))
        # user.profile.phone = data.get('phone')
        # user.profile.perm = "WOR"
        user.save()
        if data.get('table_from'):
            for table_num in range(int(data.get('table_from')), int(data.get('table_to'))+1):
                try:
                    table = Table.objects.get(number=table_num)
                    table.user = user
                    table.save()
                except Table.DoesNotExist:
                    pass

        context = self.get_context(request)
        return render(request, self.template_name, context)


@method_decorator([login_required], name='dispatch')
class ClientHistoryView(View):
    template_name = 'history.html'

    def get_context(self, request):
        context = {}
        bookings = Booking.objects.filter(user=request.user)
        context['bookings'] = bookings
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context(request)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context(request)
        return render(request, self.template_name, context)


@method_decorator([login_required], name='dispatch')
class MenuView(View):
    template_name = 'menu.html'

    def get_context(self):
        context = {}
        context['dishes'] = Dish.objects.all()
        context['snaks'] = Dish.objects.filter(category="SNA")
        context['hot'] = Dish.objects.filter(category="HOT")
        context['drinks'] = Dish.objects.filter(category="DRI")
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context()
        return render(request, self.template_name, context)