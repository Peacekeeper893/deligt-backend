from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FoodSerializer , DrinksSerializer , DessertSerializer
from .models import dessert , drinks , food

# Create your views here.


@api_view(['GET'])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)



@api_view(['GET'])
def getDessert(request):
    desserts = dessert.objects.all().order_by('price')
    serializer = DessertSerializer(desserts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getDrinks(request):
    drinkitems = drinks.objects.all().order_by('price')
    serializer = DessertSerializer(drinkitems, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getFood(request):
    foods = food.objects.all().order_by('price')
    serializer = FoodSerializer(foods, many=True)
    return Response(serializer.data)

