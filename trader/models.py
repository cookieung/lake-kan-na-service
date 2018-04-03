from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

GENDER_CHOICES = (
    ('M', 'male'),
    ('F', 'female'),
)

ITEM_STATUS = (
    ('V', 'visible'),
    ('I', 'invisible'),
)

class Trader(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    lname = models.CharField(max_length=100, blank=True, default='')
    id_number = models.CharField(max_length=13, blank=True, default='')
    gender = models.CharField(choices=GENDER_CHOICES, default='male', max_length=100)
    birthdate = models.CharField(max_length=10, blank=True, default='')
    facebook = models.CharField(max_length=100, blank=True, default='')
    lineid = models.CharField(max_length=100, blank=True, default='')
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class User(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    trader_id = models.ForeignKey(Trader,on_delete=models.CASCADE,)
    username = models.CharField(max_length=100, blank=True, default='')
    password = models.CharField(max_length=100, blank=True, default='')
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)


class Inventory(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class Tag(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    deleted = models.BooleanField(default=False)

class Image(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    url = models.CharField(max_length=100, blank=True, default='')
    deleted = models.BooleanField(default=False)

class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    status = models.CharField(choices=ITEM_STATUS, default='visible', max_length=100)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class ItemTags(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    item_id = models.ForeignKey(Item,on_delete=models.CASCADE,)
    tags = models.ForeignKey(Tag,on_delete=models.CASCADE,)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)


class Trading(models.Model):
    openDate = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,related_name='trading')
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiving')
    executeDate = models.DateTimeField(auto_now_add=False)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('openDate',)

class TradingTags(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    trading_id = models.ForeignKey(Trading,on_delete=models.CASCADE,)
    tags = models.ForeignKey(Tag,on_delete=models.CASCADE,)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class Basket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,)
    trade_id = models.ForeignKey(Trading,on_delete=models.CASCADE,)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class ItemOfBasket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    basket_id = models.ForeignKey(Basket,on_delete=models.CASCADE,)
    items = models.ForeignKey(Item,on_delete=models.CASCADE,)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class ItemOfInventory(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    inventory_id = models.ForeignKey(Inventory,on_delete=models.CASCADE,)
    items = models.ForeignKey(Item,on_delete=models.CASCADE,)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class ImageOfItem(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    item_id = models.ForeignKey(Item,on_delete=models.CASCADE,)
    images = models.ForeignKey(Image,on_delete=models.CASCADE,)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)


class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=100, blank=True, default='')
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class ReviewLog(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(User,on_delete=models.CASCADE,)
    trade_id = models.ForeignKey(Trading,on_delete=models.CASCADE,)
    review_id = models.ForeignKey(Review,on_delete=models.CASCADE,)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class Voting(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    receiver = models.ForeignKey(User,on_delete=models.CASCADE,related_name='vote')
    voter = models.ForeignKey(User,on_delete=models.CASCADE,related_name='voted')
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)