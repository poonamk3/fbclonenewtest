from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('home/',views.IndexView.as_view(),name="home"),
    path('', views.HomeView.as_view()),
    path('postsuccess/', views.PostSuccessView.as_view()),
    path('register', views.RegisterView.as_view(),name="register"),
    path('accounts/profile/',views.ProfileView.as_view(),name="profile"),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='enroll/logout.html'), name='logout'),
    path('post/', views.PostView.as_view(),name="post"),
    path('blog/', views.BlogView.as_view(),name="post"),
]

