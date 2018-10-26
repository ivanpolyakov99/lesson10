from django.urls import path
from django.views.generic import TemplateView

from library.views import index_fbv, IndexCBV


urlpatterns = [
    path('fbv', index_fbv, name='index-fbv'),
    path('cbv', IndexCBV.as_view(), name='index-fbv'),
    path('cbv1', TemplateView.as_view(template_name='index.html'), name='index-fbv'),
]
