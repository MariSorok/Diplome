from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from django.conf import settings

from project import views

urlpatterns = [
    # path('adin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('', views.MainView.as_view(), name='main'),
    path('worker-profile/', views.WorkerView.as_view()),
    path('admin_profile/', views.AdminView.as_view()),
    path('worker-edit/', views.WorkerEditView.as_view()),
    path('admin_profile/', include([
        path('confirmation/', views.ConfirmationView.as_view()),
        path('edit-menu/', views.EditMenuView.as_view()),
        path('history/', views.HistoryView.as_view()),
    ])),
    path('client-profile/', include([
        path('', views.ClientProfileView.as_view()),
        path('edit/', views.ClientEditView.as_view()),
        path('history/', views.ClientHistoryView.as_view()),
    ])),
    path('menu/', views.MenuView.as_view()),
] 
