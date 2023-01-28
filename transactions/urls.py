from django.urls import path
from .views import upload_file, ListTransactionView
from transactions import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path("api/", views.upload_file, name='start'),
    path("api/list/", ListTransactionView.as_view(), name='list'),
    path("schema/", SpectacularAPIView.as_view(), name='schema'),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name='schema')),
]