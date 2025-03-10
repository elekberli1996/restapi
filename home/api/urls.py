
from django.urls import path
from .views import BlogListAPIView,BlogDetailAPIView,BlogDeleteAPIView,BlogUpdateAPIView

urlpatterns = [
   
    path('list/', BlogListAPIView.as_view(),name="api-list" ),
    path('detail/<pk>', BlogDetailAPIView.as_view(),name="api-detail" ),
    path('delete/<pk>', BlogDeleteAPIView.as_view(),name="api-delete" ),
    path('update/<pk>', BlogUpdateAPIView.as_view(),name="api-update" )
]
