from trader.models import ItemTags,TradingTags,Trader,User,Tag,Basket,Image,Inventory,Item,Review,Trading,ItemOfBasket,ItemOfInventory,ImageOfItem,ReviewLog,Voting,Message
from trader.serializers import TraderSerializer,UserSerializer,TagSerializer,ItemTagsSerializer,TradingTagsSerializer,BasketSerializer,ImageSerializer,InventorySerializer,ItemSerializer,ReviewSerializer,TradingSerializer,ItemOfBasketSerializer,ItemOfInventorySerializer,ImageOfItemSerializer,ReviewLogSerializer,VotingSerializer,MessageSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.db.models import Q

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
        user = self.request.query_params.get('user',None)
        owner = self.request.query_params.get('owner',None)
        receiver = self.request.query_params.get('receiver',None)
        tag = self.request.query_params.get('tag',None)
        status = self.request.query_params.get('status',None)
        timeline = self.request.query_params.get('timeline',None)
        if user is not None:
            queryset = queryset.filter(Q(owner=user) | Q(receiver=user))
        if owner is not None:
            queryset = queryset.filter(owner=owner)
        if receiver is not None:
            queryset = queryset.filter(receiver=receiver)
        if tag is not None:
            queryset = queryset.filter(tags=tag)
        if status is not None:
            queryset = queryset.filter(status=status)
        if timeline is not None:
            queryset = queryset.filter(status__in=['O','P'])
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
        trade = self.request.query_params.get('trade',None)
        status = self.request.query_params.get('status',None)
        if user is not None:
            queryset = queryset.filter(owner=user)
        if trade is not None:
            queryset = queryset.filter(trade_id=trade)
        if status is not None:
            queryset = queryset.filter(status=status)
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
        status = self.request.query_params.get('status',None)
        picked = self.request.query_params.get('picked',None)
        if status is not None:
            queryset = queryset.filter(status=status)
        if picked is not None:
            queryset = queryset.filter(isPicked=picked)
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
        tag = self.request.query_params.get('tag',None)
        if item is not None:
            queryset = queryset.filter(item_id=item)
        if tag is not None:
            queryset = queryset.filter(tags=tag)
        return queryset

class ItemTagsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemTags.objects.all()
    serializer_class = ItemTagsSerializer

#11
class TradingTagsList(generics.ListCreateAPIView):
    queryset = TradingTags.objects.all()
    serializer_class = TradingTagsSerializer
    def get_queryset(self):
        queryset = TradingTags.objects.all()
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
    def get_queryset(self):
        queryset = ItemOfInventory.objects.all()
        inventory = self.request.query_params.get('inventory',None)
        if inventory is not None:
            queryset = queryset.filter(inventory_id=inventory)
        return queryset.order_by('-created')


class ItemOfInventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemOfInventory.objects.all()
    serializer_class = ItemOfInventorySerializer


#13
class ItemOfBasketList(generics.ListCreateAPIView):
    queryset = ItemOfBasket.objects.all()
    serializer_class = ItemOfBasketSerializer
    def get_queryset(self):
        queryset = ItemOfBasket.objects.all()
        basket = self.request.query_params.get('basket',None)
        if basket is not None:
            queryset = queryset.filter(basket_id=basket)
        return queryset.order_by('-created')
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=isinstance(request.data, list))
        serializer.is_valid(raise_exception=True)
        itemBasket_created = []
        for list_elt in request.data:
            basket = Basket.objects.get(pk=list_elt.get('basket_id'))
            items = Item.objects.get(pk=list_elt.get('items'))
            items.isPicked = True
            items.status = 'I'
            items.save()
            if not ItemOfBasket.objects.filter(basket_id=list_elt.get('basket_id')).filter(items=list_elt.get('items')).exists() :
                item_obj = ItemOfBasket.objects.create(basket_id=basket, items=items)
                itemBasket_created.append(item_obj.id)
        results = ItemOfBasket.objects.filter(id__in=itemBasket_created)
        output_serializer = ItemOfBasketSerializer(results, many=True)
        data = output_serializer.data[:]
        return Response(data)

class ItemOfBasketDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemOfBasket.objects.all()
    serializer_class = ItemOfBasketSerializer


#14
class ImageOfItemList(generics.ListCreateAPIView):
    queryset = ImageOfItem.objects.all()
    serializer_class = ImageOfItemSerializer
    def get_queryset(self):
        queryset = ImageOfItem.objects.all()
        item = self.request.query_params.get('item', None)
        inventory = self.request.query_params.get('inventory', None)
        basket = self.request.query_params.get('basket', None)
        if inventory is not None:
            item_of_inventory_queryset = ItemOfInventory.objects.all()
            item_of_inventory_queryset = item_of_inventory_queryset.filter(inventory_id=inventory)
            item_id_value = item_of_inventory_queryset.values_list('items', flat=True)
            item_id_arr = list(item_id_value)
            queryset = queryset.filter(item_id__in=item_id_arr)
        if basket is not None:
            item_of_basket_queryset = ItemOfBasket.objects.all()
            item_of_basket_queryset = item_of_basket_queryset.filter(basket_id=basket)
            item_id_value = item_of_basket_queryset.values_list('items', flat=True)
            item_id_arr = list(item_id_value)
            queryset = queryset.filter(item_id__in=item_id_arr)
        if item is not None:
            queryset = queryset.filter(item_id=item)
        return queryset.order_by('-created')

class ImageOfItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ImageOfItem.objects.all()
    serializer_class = ImageOfItemSerializer


#15
class ReviewLogList(generics.ListCreateAPIView):
    queryset = ReviewLog.objects.all()
    serializer_class = ReviewLogSerializer
    def get_queryset(self):
        queryset = ReviewLog.objects.all()
        writer = self.request.query_params.get('writer',None)
        trade = self.request.query_params.get('trade',None)
        review = self.request.query_params.get('review',None)
        if writer is not None:
            queryset = queryset.filter(write=writer)
        if trade is not None:
            queryset = queryset.filter(trade_id=trade)
        if review is not None:
            queryset = queryset.filter(review_id=review)
        return queryset.order_by('-created')

class ReviewLogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewLog.objects.all()
    serializer_class = ReviewLogSerializer


#16
class VotingList(generics.ListCreateAPIView):
    queryset = Voting.objects.all()
    serializer_class = VotingSerializer
    def get_queryset(self):
        queryset = Voting.objects.all()
        receiver = self.request.query_params.get('receiver',None)
        if receiver is not None:
            queryset = queryset.filter(receiver=receiver)
        return queryset.order_by('-created')

class VotingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Voting.objects.all()
    serializer_class = VotingSerializer


#17
class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    def get_queryset(self):
        queryset = Message.objects.all()
        owner = self.request.query_params.get('owner',None)
        basket = self.request.query_params.get('basket',None)
        trade = self.request.query_params.get('trade',None)
        if trade is not None:
            basket_queryset = Basket.objects.all()
            basket_queryset = basket_queryset.filter(trade_id=trade)
            basket_id_value = basket_queryset.values_list('id', flat=True)
            basket_id_arr = list(basket_id_value)
            queryset = queryset.filter(basket__in=basket_id_arr)
        if owner is not None:
            queryset = queryset.filter(owner=owner)
        if basket is not None:
            queryset = queryset.filter(basket=basket)
        return queryset.order_by('-created')

class MessageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
