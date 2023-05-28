from django.shortcuts import render

from django.http import JsonResponse
import requests
from rest_framework import status
from admin_dash.models import Food, NewOrders, Order, Availability
from admin_dash.serializers import FoodSerializer, OrderSerializer, AvailabilitySerializer, NewOrderSerializer
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import generics
from django.conf import settings
import json

@api_view(['POST'])
def addMenuItem(request):
    if request.method == 'POST':
        new_menu_data = JSONParser().parse(request)
        food_title = new_menu_data['title']
        food_price = new_menu_data['price']
        if food_title is not None and food_price is not None:
            items = Food.objects.all()
            item = items.filter(title=food_title)
            if(item is not None):
                serializer = None
                serializer = FoodSerializer(data=new_menu_data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                return JsonResponse({'message': 'Item already exists!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'One of the fields is empty!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['PUT'])
def updateMenuItem(request):
    if request.method == 'PUT':
        update_menu_data = JSONParser().parse(request)
        food_title = update_menu_data['title']
        food_price = update_menu_data['price']
        if food_title is not None and food_price is not None:
            items = Food.objects.all()
            item = items.get(title=food_title)
            if(item is not None):
                serializer = None
                serializer = FoodSerializer(item, data=update_menu_data)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                return JsonResponse({'message': 'Item does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'One of the fields is empty!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def deleteMenuItem(request):
    if request.method == 'DELETE':
        delete_menu_data = JSONParser().parse(request)
        food_title = delete_menu_data['title']
        if food_title is not None:
            items = Food.objects.all()
            item = items.filter(title=food_title)
            if(item is not None):
                item.delete()
                return JsonResponse({'message': 'Item deleted successfully'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'message': 'Item does not exist!'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'Title is empty!'}, status=status.HTTP_204_NO_CONTENT)

class listMenuItems(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


@api_view(['POST'])
def toggleAvailability(request):
    if request.method == 'POST':
        # we expect to have only one row in the availability model
        # so always get id 1 
        avail = Availability.objects.get(id=1)
        if avail.status == True:
            avail.status = False
            avail.save()
            return JsonResponse({'message': 'Availability set to false'}, status=status.HTTP_200_OK)
        else:
            avail.status = True
            avail.save()
            return JsonResponse({'message': 'Availability set to true'}, status=status.HTTP_200_OK)
            

class getAvailability(generics.ListCreateAPIView):
    queryset = Availability.objects.all()
    serializer_class = AvailabilitySerializer

@api_view(['POST'])
def setTimings(request):
    if request.method == 'POST':
        new_timings = JSONParser().parse(request)
        open_timing = new_timings['opening']
        close_timing = new_timings['closing']
        if open_timing is not None and close_timing is not None:
            # we expect to have only one row in the availability model
            # so always get id 1 
            avail = Availability.objects.get(id=1)
            if avail is not None:
                avail.opening = open_timing
                avail.closing = close_timing
                avail.save()
                return JsonResponse({'message': 'Timings set successfully'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'message': 'Unable to find object in the DB'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'Field is empty'}, status=status.HTTP_400_BAD_REQUEST)
    

class getNewOrders(generics.ListCreateAPIView):
    queryset = NewOrders.objects.all()
    serializer_class = NewOrderSerializer


@api_view(['POST'])
def acceptOrder(request):
    if request.method == 'POST':
        accept_order = JSONParser().parse(request)
        order_id = accept_order['id']
        order_title = accept_order['title']
        if order_id is not None and order_title is not None:
                serializer = None
                serializer = OrderSerializer(data=accept_order)
                if serializer.is_valid():
                    #remove this order from New orders since it is accepted
                    order = NewOrders.objects.get(id=order_id)
                    order.delete()
                    serializer.save()
                    return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
                return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'One of the fields is empty!'}, status=status.HTTP_400_BAD_REQUEST)


class getAcceptedOrders(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

@api_view(['POST'])
def placeNewOrder(request):
    if request.method == 'POST':
        new_orders = JSONParser().parse(request)
        if new_orders is not None:
            serializer = None
            serializer = NewOrderSerializer(data=new_orders, many=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, safe=False, status=status.HTTP_200_OK)
            return JsonResponse(serializer.errors, safe=False,  status=status.HTTP_400_BAD_REQUEST)
        else:
            return JsonResponse({'message': 'No orders found!'}, status=status.HTTP_400_BAD_REQUEST)

