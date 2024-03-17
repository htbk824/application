from django.urls import path
from . import views

urlpatterns = [
    path("home", views.home, name="home"),
    path("borrowed_games", views.borrowed_games, name="borrowed_games"),
    path("return_games", views.return_games, name="return_games"),
    path('get_rental_info/<str:game_name>/', views.get_rental_info, name='get_rental_info'),
    path("sign_up", views.sign_up, name="sign_up"),
    path("sign_out", views.sign_out, name="sign_out"),
    path("", views.sign_in, name="sign_in"),

]