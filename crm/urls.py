from django.urls import path
from crm.views import login
from crm  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('login/', login.as_view(), name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('create/', views.create_record, name='create'),
    path('update/<int:pk>', views.update_record, name='update'),
    path('delete/<int:pk>', views.delete_record, name='delete'),

]