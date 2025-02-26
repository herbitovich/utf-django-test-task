from .models import Food, FoodCategory, FoodListSerializer
from rest_framework import generics
from django.db.models import Prefetch

class ListFood(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        published_foods = Food.objects.filter(is_publish=True)
        queryset = FoodCategory.objects.prefetch_related(Prefetch('food', queryset=published_foods)).distinct().order_by('id', 'food__code')
        return queryset