from django.urls import path
from . import views


urlpatterns = [
    # path("", views.api_home),
    # path("<int:pk>/", views.api_home),
    # path("", views.ProductListCreateAPIView.as_view()),
    # path("<int:pk>/", views.ProductRetrieveUpdateDestroy.as_view()),
    path("<int:pk>/update/", views.ProductRetrieveUpdateDestroy.as_view()),
    path("<int:pk>/delete/", views.ProductRetrieveUpdateDestroy.as_view()),
    path("", views.ProductMixinView.as_view()),
    path("<int:pk>/", views.ProductMixinView.as_view()),
]
