from django.urls import path, re_path
from . import views

app_name = "storage"

urlpatterns = [
    path('', views.StorageItemListView.as_view(), name='index'),
    re_path(r'^(?P<item>\w+)/(?P<code>[0-9]+)/$',
            views.StorageItemRetrieveView.as_view(), name='detail'),
    re_path(r'^(?P<item>.+)/(?P<code>[0-9]+)/delete/$',
            views.StorageItemDeleteView.as_view(), name='delete'),
    re_path(r'^(?P<item>.+)/(?P<code>[0-9]+)/edit/$',
            views.StorageItemUpdateView.as_view(), name='edit'),
    path('create/', views.StorageItemCreateView.as_view(), name='create')
]
