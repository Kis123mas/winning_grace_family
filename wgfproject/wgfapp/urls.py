from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.landingPage, name='landingpage'),
    path('home/', views.homePage, name='homepage'),
    path('profile/', views.profilePage, name='profilepage'),
    path('contact/', views.contactPage, name='contactpage'),
    path('member/', views.memberPage, name='memberpage'),
    path('calender/', views.calenderPage, name='calenderpage'),
    path('prayer/', views.prayerPage, name='prayerpage'),
    path('testimony/', views.testimonyPage, name='testimonypage'),
    path('success/', views.successPage, name='successpage'),

    path('register/', views.registerationPage, name='registerpage'),
    path('login/', views.loginPage, name='loginpage'),
    path('logout/', views.logoutUser, name='logoutpage'),

    path('bloghome/', views.bloghomePage, name='bloghomepage'),
    path('article/<str:slug>', views.detailblogPage, name='detailpage'),
    path('createpost', views.createPost, name = 'create'),
    path('updatepost/<str:slug>', views.updatePost, name = 'update'),
    path('deletepost/<str:slug>', views.deletePost, name = 'delete'),
    path('article/<str:slug>/comment/', views.createComment, name = 'add_comment'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registeration/password_resetform.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name ="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
