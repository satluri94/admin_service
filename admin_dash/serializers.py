from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from admin_dash.models import Food, Order, Availability, NewOrders

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['title', 'price']

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'title']

class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = ['status','opening', 'closing']

class NewOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewOrders
        fields = ['id', 'title', 'price']