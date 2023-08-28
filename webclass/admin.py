from django.contrib import admin
from .models  import Product,Contact,Signin, Contactus
# Register your models here.

admin.site.register(Product)
admin.site.register(Contact)
admin.site.register(Signin)
admin.site.register(Contactus)