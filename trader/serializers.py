from .models import Trader,Tag,Basket,Image,Inventory,Item,Review,Trading
from rest_framework import serializers

class TraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trader
        fields = ('id','id_number','name','lname', 'gender','birthdate','facebook','lineid','deleted')


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id','name','owner','deleted')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id','name','inventory_id','status','tags','images','deleted')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name','deleted')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id','url','deleted')


class BasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basket
        fields = ('id','owner','trade_id','items','deleted')

class TradingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trading
        fields = ('id','executeDate','owner','receiver','tags','deleted')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','writer','trade_id','comment','rate','deleted')

