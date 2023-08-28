from django.urls import path
#from .import views
from .views import home,Index4,Rooms,signin,contactus,Dining,Events,Gallery,Admin_add_amenities,Logout


urlpatterns = [
    #path("home", views.home)
    path("home", home),
    path("", Index4),
    path("rooms/",  Rooms),
    path("sign_in/",  signin),
    path("contactus/", contactus),
    path("dining/", Dining),
    path("events/", Events),
    path("gallery/", Gallery),
    path("logout/", Logout),
    path("admin_add_amenities/", Admin_add_amenities),
    
]