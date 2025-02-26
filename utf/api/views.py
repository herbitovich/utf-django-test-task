from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Food, FoodCategory, FoodListSerializer, FoodSerializer
from rest_framework import generics

class ListFood(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        queryset = FoodCategory.objects.prefetch_related('food').filter(food__is_publish=True).distinct()

        return queryset

