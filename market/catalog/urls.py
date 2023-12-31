from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    TagsList,
    ProductDetail,
    LimitedList,
    PopularList,
    SalesList,
    CreateReview,
    Catalog,
    BannersList,
    CategoriesListViewSet
)

app_name = "catalog"

routers = DefaultRouter()
routers.register("categories", CategoriesListViewSet)

urlpatterns = [
    path('catalog/', Catalog.as_view(), name='products_list'),
    path('banners/', BannersList.as_view(), name='banners'),
    path('', include(routers.urls)),
    # path('categories/', CategoriesList.as_view(), name='categories'),
    path('product/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('product/<int:pk>/reviews/', CreateReview.as_view()),
    path('tags/', TagsList.as_view(), name='tags_list'),
    path('products/popular/', PopularList.as_view(), name='popular'),
    path('products/limited/', LimitedList.as_view(), name='limited'),
    path('sales/', SalesList.as_view(), name='sales'),
]
