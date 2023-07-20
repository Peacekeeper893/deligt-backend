from django.contrib import admin

# Register your models here.


from .models import dessert,drinks,food


admin.site.register(dessert)
admin.site.register(drinks)
admin.site.register(food)


