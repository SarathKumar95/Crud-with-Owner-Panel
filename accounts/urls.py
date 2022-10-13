from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.register, name='register'),
    path('accounts/login/', views.login_view, name='signin'),
    path('owner', views.owner_home, name='owner'),
    path('accounts/logout', views.sign_out, name='signout'),
    path('delete/<int:id>', views.delete_view, name='delete'),
    path('update/<int:id>/', views.update_view, name='update'),
    path('create', views.create_user, name='create'),
    path('search_users', views.search_user, name='search_user'),
    path('customer', views.user_home, name='customer')
]
