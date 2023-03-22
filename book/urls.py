from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path("idx/",views.index,name="index"),
    path("l/",views.user_login,name="user-login"),
    path("",views.user_registration,name="user-registration"),
path("logout", views.logout_request, name= "logout"),
path("add-contact", views.contact_creation_view, name= "add-contact"),
path("all-contacts", views.all_contacts_view, name= "all-contacts"),
path("contact-update/<int:id>/", views.contact_update_view, name= "contact-update"),
path("contact-delete/<int:id>/", views.contact_delete_view, name= "contact-delete"),

]
