from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('user/', views.userPage,name="user"),
    path('dashboard/', views.dashboardPage,name="dashboard"),
    path('room/', views.roomPage,name="room"),
    path('inform/', views.infoPage,name="inform"),
    # path('choose_room/', views.chooseRoom,name="choose_room"),
    path('update_student/<str:pk>/', views.updateStudent, name="update_student"),
    path('delete_student/<str:pk>/', views.deleteStudent, name="delete_student"),
    path('account/', views.accountSettings, name="account"),
    path('allot/', views.allot,name="allot"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('reset_password/',
     auth_views.PasswordResetView.as_view(template_name="hostelapp/password_reset.html"),
     name="reset_password"),

    path('reset_password_sent/', 
        auth_views.PasswordResetDoneView.as_view(template_name="hostelapp/password_reset_sent.html"), 
        name="password_reset_done"),

    path('reset/<uidb64>/<token>/',
     auth_views.PasswordResetConfirmView.as_view(template_name="hostelapp/password_reset_form.html"), 
     name="password_reset_confirm"),

    path('reset_password_complete/', 
        auth_views.PasswordResetCompleteView.as_view(template_name="hostelapp/password_reset_done.html"), 
        name="password_reset_complete"),
]
