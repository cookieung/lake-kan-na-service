from trader.models import Trader,User,Tag,Basket,Image,Inventory,Item,Review,Trading
from trader.serializers import TraderSerializer,UserSerializer,TagSerializer,BasketSerializer,ImageSerializer,InventorySerializer,ItemSerializer,ReviewSerializer,TradingSerializer
from rest_framework import generics

class TraderList(generics.ListCreateAPIView):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer

#For get profile of a trader
class TraderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_queryset(self):
        queryset = User.objects.all()
        username = self.request.query_params.get('username',None)
        password = self.request.query_params.get('password',None)
        if username is not None and password is not None:
            queryset = queryset.filter(username=username).filter(password=password)
            return queryset
        elif username is not None or password is not None:
            return None
        return queryset

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class TradingList(generics.ListCreateAPIView):
    queryset = Trading.objects.all()
    serializer_class = TradingSerializer
    def get_queryset(self):
        queryset = Trading.objects.all()
        owner = self.request.query_params.get('owner',None)
        receiver = self.request.query_params.get('receiver',None)
        tag = self.request.query_params.get('tag',None)
        if owner is not None:
            queryset = queryset.filter(owner=owner)
        if receiver is not None:
            queryset = queryset.filter(receiver=receiver)
        if tag is not None:
            queryset = queryset.filter(tags=tag)
        return queryset

class TradingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trading.objects.all()
    serializer_class = TradingSerializer


class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class BasketList(generics.ListCreateAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    def get_queryset(self):
        queryset = Basket.objects.all()
        user = self.request.query_params.get('user',None)
        if user is not None:
            queryset = queryset.filter(owner=user)
        return queryset

class BasketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer


class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    def get_queryset(self):
        queryset = Inventory.objects.all()
        user = self.request.query_params.get('user',None)
        if user is not None:
            queryset = queryset.filter(owner=user)
        return queryset

class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def get_queryset(self):
        queryset = Review.objects.all()
        writer = self.request.query_params.get('writer',None)
        trade = self.request.query_params.get('trade',None)
        if writer is not None:
            queryset = queryset.filter(writer=writer)
        if trade is not None:
            queryset = queryset.filter(trade_id=trade)
        return queryset

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    def get_queryset(self):
        queryset = Item.objects.all()
        inventory = self.request.query_params.get('inventory',None)
        if inventory is not None:
            queryset = queryset.filter(inventory_id=inventory)
        return queryset

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


