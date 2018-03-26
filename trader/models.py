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

class Inventory(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    owner = models.ForeignKey(Trader,on_delete=models.CASCADE,)
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
    inventory_id = models.ForeignKey(Inventory,on_delete=models.CASCADE,)
    status = models.CharField(choices=ITEM_STATUS, default='male', max_length=100)
    tags = models.ForeignKey(Tag,on_delete=models.CASCADE,)
    images = models.ForeignKey(Image,on_delete=models.CASCADE,)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)


class Trading(models.Model):
    openDate = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Trader,on_delete=models.CASCADE,related_name='trading')
    receiver = models.ForeignKey(Trader,on_delete=models.CASCADE,related_name='receiving')
    executeDate = models.DateTimeField(auto_now_add=False)
    tags = models.ForeignKey(Tag,on_delete=models.CASCADE,)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('openDate',)

class Basket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(Trader,on_delete=models.CASCADE,)
    trade_id = models.ForeignKey(Trading,on_delete=models.CASCADE,)
    items = models.ForeignKey(Item,on_delete=models.CASCADE,)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

class Review(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    writer = models.ForeignKey(Trader,on_delete=models.CASCADE,)
    trade_id = models.ForeignKey(Trading,on_delete=models.CASCADE,)
    comment = models.CharField(max_length=100, blank=True, default='')
    rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)