from django.contrib import admin

# Register your models here.
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import dessert,drinks,food,chef,appetizer,steak


class FoodResource(resources.ModelResource):
    class Meta:
        model = food
class FoodAdmin(ImportExportModelAdmin):
    resource_class = FoodResource



class DrinkResource(resources.ModelResource):
    class Meta:
        model = drinks
class DrinkAdmin(ImportExportModelAdmin):
    resource_class = DrinkResource



class DessertResource(resources.ModelResource):
    class Meta:
        model = dessert
class DessertAdmin(ImportExportModelAdmin):
    resource_class = DessertResource

class ChefResource(resources.ModelResource):
    class Meta:
        model = chef
class ChefAdmin(ImportExportModelAdmin):
    resource_class = ChefResource



class AppetizerResource(resources.ModelResource):
    class Meta:
        model = appetizer
class AppetizerAdmin(ImportExportModelAdmin):
    resource_class = AppetizerResource



class SteakResource(resources.ModelResource):
    class Meta:
        model = steak
class SteakAdmin(ImportExportModelAdmin):
    resource_class = SteakResource


admin.site.register(dessert , DessertAdmin)
admin.site.register(drinks, DrinkAdmin)
admin.site.register(food , FoodAdmin)
admin.site.register(chef , ChefAdmin)
admin.site.register(appetizer , AppetizerAdmin)
admin.site.register(steak , SteakAdmin)



