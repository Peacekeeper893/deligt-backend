from rest_framework.serializers import ModelSerializer
from .models import dessert , drinks,food


class DessertSerializer(ModelSerializer):
    class Meta:
        model = dessert
        fields = '__all__'

class FoodSerializer(ModelSerializer):
    class Meta:
        model = food
        fields = '__all__'


class DrinksSerializer(ModelSerializer):
    class Meta:
        model = drinks
        fields = '__all__'