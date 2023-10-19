from rest_framework.serializers import ModelSerializer
from .models import dessert , drinks,food ,chef ,appetizer , steak


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

class ChefSerializer(ModelSerializer):
    class Meta:
        model = chef
        fields = '__all__'

class AppetizerSerializer(ModelSerializer):
    class Meta:
        model = appetizer
        fields = '__all__'


class SteakSerializer(ModelSerializer):
    class Meta:
        model = steak
        fields = '__all__'