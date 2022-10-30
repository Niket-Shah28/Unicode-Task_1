from django.urls import path
from . import views

urlpatterns = [
    path("",views.Sign_IN,name="login"),
    path("register/",views.signup,name="register"),
    path("display/",views.display_page,name="display"),
    path("list/",views.list,name="list"),
    path("logout/",views.signout,name="logout"),
    path("update/<int:id>/",views.update,name="update"),
    path("delete/<int:id>/",views.delete,name="delete"),
    path("profile/",views.viewprofile,name="ViewProfile"),
]