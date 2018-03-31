from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from trader import views

urlpatterns = [

    #1
    url(r'^traders/$', views.TraderList.as_view()),
    url(r'^traders/(?P<pk>[0-9]+)/$', views.TraderDetail.as_view()),

    #2
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    #3
    url(r'^trading/$', views.TradingList.as_view()),
    url(r'^trading/(?P<pk>[0-9]+)/$', views.TradingDetail.as_view()),

    #4
    url(r'^images/$', views.ImageList.as_view()),
    url(r'^images/(?P<pk>[0-9]+)/$', views.ImageDetail.as_view()),

    #5
    url(r'^items/$', views.ItemList.as_view()),
    url(r'^items/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),

    #6
    url(r'^items/tags/$', views.ItemTagsList.as_view()),
    url(r'^items/tags/(?P<pk>[0-9]+)/$', views.ItemTagsDetail.as_view()),

    #7
    url(r'^baskets/$', views.BasketList.as_view()),
    url(r'^baskets/(?P<pk>[0-9]+)/$', views.BasketDetail.as_view()),

    #8
    url(r'^reviews/$', views.ReviewList.as_view()),
    url(r'^reviews/(?P<pk>[0-9]+)/$', views.ReviewDetail.as_view()),

    #9
    url(r'^tags/$', views.TagList.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetail.as_view()),

    #10
    url(r'^inventories/$', views.InventoryList.as_view()),
    url(r'^inventories/(?P<pk>[0-9]+)/$', views.InventoryDetail.as_view()),

    #11
    url(r'^trading/tags/$', views.TradingTagsList.as_view()),
    url(r'^trading/tags/(?P<pk>[0-9]+)/$', views.TradingTagsDetail.as_view()),

    #12
    url(r'^inventories/items/$', views.ItemOfInventoryList.as_view()),
    url(r'^inventories/items/(?P<pk>[0-9]+)/$', views.ItemOfInventoryDetail.as_view()),

    #13
    url(r'^baskets/items/$', views.ItemOfBasketList.as_view()),
    url(r'^baskets/items/(?P<pk>[0-9]+)/$', views.ItemOfBasketDetail.as_view()),

    #14
    url(r'^items/images/$', views.ImageOfItemList.as_view()),
    url(r'^items/images/(?P<pk>[0-9]+)/$', views.ImageOfItemDetail.as_view()),

    #15
    url(r'^users/reviews/$', views.ReviewLogList.as_view()),
    url(r'^users/reviews/(?P<pk>[0-9]+)/$', views.ReviewLogDetail.as_view()),

    #16
    url(r'^voting/$', views.VotingList.as_view()),
    url(r'^voting/(?P<pk>[0-9]+)/$', views.VotingDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)