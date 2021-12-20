from django.db import models
from rest_framework import serializers
from .models import Journals, Supply, Theme

class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journals 
        fields = ['id', 'brand', 'paperweight', 'sizes', 'pages']
        
class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supply
        fields = ['id','brand', 'type', 'ink']
        
class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ['id','image', 'pagelayout', 'creator']