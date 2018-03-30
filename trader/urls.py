from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from trader import views

urlpatterns = [

    url(r'^traders/$', views.TraderList.as_view()),
    url(r'^traders/(?P<pk>[0-9]+)/$', views.TraderDetail.as_view()),

    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),

    url(r'^trading/$', views.TradingList.as_view()),
    url(r'^trading/(?P<pk>[0-9]+)/$', views.TradingDetail.as_view()),

    url(r'^images/$', views.ImageList.as_view()),
    url(r'^images/(?P<pk>[0-9]+)/$', views.ImageDetail.as_view()),

    url(r'^items/$', views.ItemList.as_view()),
    url(r'^items/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),

    url(r'^baskets/$', views.BasketList.as_view()),
    url(r'^baskets/(?P<pk>[0-9]+)/$', views.BasketDetail.as_view()),

    url(r'^reviews/$', views.ReviewList.as_view()),
    url(r'^reviews/(?P<pk>[0-9]+)/$', views.ReviewDetail.as_view()),

    url(r'^tags/$', views.TagList.as_view()),
    url(r'^tags/(?P<pk>[0-9]+)/$', views.TagDetail.as_view()),

    url(r'^inventories/$', views.InventoryList.as_view()),
    url(r'^inventories/(?P<pk>[0-9]+)/$', views.InventoryDetail.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)