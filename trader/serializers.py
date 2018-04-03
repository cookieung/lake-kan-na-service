from .models import ItemTags,TradingTags,Trader,User,Tag,Basket,Image,Inventory,Item,Review,Trading,ItemOfBasket,ItemOfInventory,ImageOfItem,ReviewLog,Voting
from rest_framework import serializers


class TraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trader
        fields = ('id','id_number','name','lname', 'gender','birthdate','facebook','lineid','deleted')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','trader_id','username','password', 'deleted')



class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ('id','owner','deleted')


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ('id','created','name','status','deleted')


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
        fields = ('id','owner','trade_id','deleted')

class TradingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trading
        fields = ('id','executeDate','owner','receiver', 'deleted')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','comment','deleted')

class ItemTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTags
        fields = ('id', 'item_id', 'tags' ,'deleted')


class TradingTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingTags
        fields = ('id', 'trading_id', 'tags' ,'deleted')

class ItemOfBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOfBasket
        fields = ('id','basket_id','items','deleted')


class ItemOfInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOfInventory
        fields = ('id','inventory_id','items','deleted')

class ImageOfItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageOfItem
        fields = ('id','item_id','images','deleted')

class ReviewLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLog
        fields = ('id','writer','trade_id','review_id','deleted')

class VotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voting
        fields = ('id','receiver','voter','rate','deleted')
