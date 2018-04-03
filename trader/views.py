from trader.models import ItemTags,TradingTags,Trader,User,Tag,Basket,Image,Inventory,Item,Review,Trading,ItemOfBasket,ItemOfInventory,ImageOfItem,ReviewLog,Voting
from trader.serializers import TraderSerializer,UserSerializer,TagSerializer,ItemTagsSerializer,TradingTagsSerializer,BasketSerializer,ImageSerializer,InventorySerializer,ItemSerializer,ReviewSerializer,TradingSerializer,ItemOfBasketSerializer,ItemOfInventorySerializer,ImageOfItemSerializer,ReviewLogSerializer,VotingSerializer
from rest_framework import generics

#1
class TraderList(generics.ListCreateAPIView):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer

#For get profile of a trader
class TraderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trader.objects.all()
    serializer_class = TraderSerializer

#2
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

#3

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

#4
class TagList(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

#5
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

#6
class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

#7
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

#8
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

#9
class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all().order_by('-created')
    serializer_class = ItemSerializer
    def get_queryset(self):
        queryset = Item.objects.all()
        inventory = self.request.query_params.get('inventory',None)
        if inventory is not None:
            queryset = queryset.filter(inventory_id=inventory)
        return queryset.order_by('-created')

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

#10
class ItemTagsList(generics.ListCreateAPIView):
    queryset = ItemTags.objects.all()
    serializer_class = ItemTagsSerializer
    def get_queryset(self):
        queryset = ItemTags.objects.all()
        item = self.request.query_params.get('item',None)
        if item is not None:
            queryset = queryset.filter(item_id=item)
        return queryset

class ItemTagsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemTags.objects.all()
    serializer_class = ItemTagsSerializer

#11
class TradingTagsList(generics.ListCreateAPIView):
    queryset = TradingTags.objects.all()
    serializer_class = TradingTagsSerializer
    def get_queryset(self):
        queryset = ItemTags.objects.all()
        trading = self.request.query_params.get('trading',None)
        if trading is not None:
            queryset = queryset.filter(trading_id=trading)
        return queryset

class TradingTagsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TradingTags.objects.all()
    serializer_class = TradingTagsSerializer

#12
class ItemOfInventoryList(generics.ListCreateAPIView):
    queryset = ItemOfInventory.objects.all()
    serializer_class = ItemOfInventorySerializer

class ItemOfInventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemOfInventory.objects.all()
    serializer_class = ItemOfInventorySerializer


#13
class ItemOfBasketList(generics.ListCreateAPIView):
    queryset = ItemOfBasket.objects.all()
    serializer_class = ItemOfBasketSerializer

class ItemOfBasketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemOfBasket.objects.all()
    serializer_class = ItemOfBasketSerializer


#14
class ImageOfItemList(generics.ListCreateAPIView):
    queryset = ImageOfItem.objects.all()
    serializer_class = ImageOfItemSerializer

class ImageOfItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageOfItem.objects.all()
    serializer_class = ImageOfItemSerializer


#15
class ReviewLogList(generics.ListCreateAPIView):
    queryset = ReviewLog.objects.all()
    serializer_class = ReviewLogSerializer

class ReviewLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewLog.objects.all()
    serializer_class = ReviewLogSerializer


#16
class VotingList(generics.ListCreateAPIView):
    queryset = Voting.objects.all()
    serializer_class = VotingSerializer

class VotingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voting.objects.all()
    serializer_class = VotingSerializer
