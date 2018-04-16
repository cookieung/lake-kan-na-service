from .models import ItemTags,TradingTags,Trader,User,Tag,Basket,Image,Inventory,Item,Review,Trading,ItemOfBasket,ItemOfInventory,ImageOfItem,ReviewLog,Voting
from rest_framework import serializers
# import json
# from django.http import HttpResponse

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
        fields = ('id','owner','trade_id', 'status', 'deleted')
    def to_representation(self, obj):
        return {
            "id": obj.id,
            "owner": {
                    "id": obj.owner.id,
                    "trader_id": {
                            "id": obj.owner.trader_id.id,
                            "name": obj.owner.trader_id.name,
                            "lname": obj.owner.trader_id.lname
                    }
            },
            "trade_id": obj.trade_id.id,
            "deleted": obj.deleted
        }

class TradingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trading
        fields = ('id','executeDate','name','description','owner','receiver', 'status', 'deleted')
    def to_representation(self, obj):
        if obj.receiver is None:
            return {
                "id": obj.id,
                "executeDate": obj.executeDate,
                "name": obj.name,
                "description": obj.description,
                "owner": {
                        "id": obj.owner.id,
                        "trader_id": {
                                "id": obj.owner.trader_id.id,
                                "name": obj.owner.trader_id.name,
                                "lname": obj.owner.trader_id.lname
                        }
                },
                "receiver": None,
                "deleted": obj.deleted
            }
        return {
            "id": obj.id,
            "executeDate": obj.executeDate,
            "name": obj.name,
            "description": obj.description,
            "owner": {
                    "id": obj.owner.id,
                    "trader_id": {
                            "id": obj.owner.trader_id.id,
                            "name": obj.owner.trader_id.name,
                            "lname": obj.owner.trader_id.lname
                    }
            },
            "receiver": {
                    "id": obj.receiver.id,
                    "trader_id": {
                            "id": obj.receiver.trader_id.id,
                            "name": obj.receiver.trader_id.name,
                            "lname": obj.receiver.trader_id.lname
                    }
            },
            "deleted": obj.deleted
        }

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('id','comment','deleted')

class ItemTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemTags
        fields = ('id', 'item_id', 'tags' ,'deleted')
    def to_representation(self, obj):
        return {
            "id": obj.id,
            "item_id": {"id": obj.item_id.id,"created": obj.item_id.created,"name": obj.item_id.name,"status": obj.item_id.status,"deleted": obj.item_id.deleted} ,
            "tags": {"id": obj.tags.id, "name": obj.tags.name, "deleted": obj.tags.deleted},
            "deleted": obj.deleted
        }


class TradingTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradingTags
        fields = ('id', 'trading_id', 'tags' ,'deleted')
    def to_representation(self, obj):
        return {
            "id": obj.id,
            "trading_id": {"id": obj.trading_id.id, "executeDate": obj.trading_id.executeDate, "name": obj.trading_id.name,"description": obj.trading_id.description,"owner": obj.trading_id.owner.id,"receiver": obj.trading_id.receiver.id, "deleted": obj.trading_id.deleted},
            "tags": {"id": obj.tags.id, "name": obj.tags.name, "deleted": obj.tags.deleted},
            "deleted": obj.deleted
        }

class ItemOfBasketSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOfBasket
        fields = ('id','basket_id','items','deleted')
    def to_representation(self, obj):
        return {
            "id": obj.id,
            "basket_id": {"id": obj.basket_id.id, "owner": obj.basket_id.owner.id, "trade_id": obj.basket_id.trade_id.id, "deleted": obj.basket_id.deleted},
            "items": {"id": obj.items.id,"created": obj.items.created,"name": obj.items.name,"status": obj.items.status,"deleted": obj.items.deleted} ,
            "deleted": obj.deleted
        }

class ItemOfInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemOfInventory
        fields = ('id','inventory_id','items','deleted')
    def to_representation(self, obj):
        return {
            "id": obj.id,
            "inventory_id": {"id": obj.inventory_id.id, "owner": obj.inventory_id.owner.id, "deleted": obj.inventory_id.deleted},
            "items": {"id": obj.items.id,"created": obj.items.created,"name": obj.items.name,"status": obj.items.status,"deleted": obj.items.deleted} ,
            "deleted": obj.deleted
        }

class ImageOfItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageOfItem
        fields = ('id','item_id','images','deleted')
    def to_representation(self, obj):
        return {
            "id": obj.id,
            "item_id": {"id": obj.item_id.id,"created": obj.item_id.created,"name": obj.item_id.name,"status": obj.item_id.status,"deleted": obj.item_id.deleted} ,
            "images": {"id": obj.images.id, "url": obj.images.url, "deleted": obj.images.deleted},
            "deleted": obj.deleted
        }

class ReviewLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewLog
        fields = ('id','writer','trade_id','review_id','deleted')

class VotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voting
        fields = ('id','receiver','voter','rate','deleted')
