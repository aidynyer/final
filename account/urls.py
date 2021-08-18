from django.urls import path, include

from account import views

urlpatterns = [
    path("<int:id>", views.userApi),
    # path('user/', views.profile_page, name="profile"),
    path('', include('account.api.urls')),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
]
