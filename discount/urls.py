
from django.conf.urls import url

from .views import CartDiscountCodeDeleteView, CartDiscountCodeCreateView


urlpatterns = [
    url(r'^discount_code/$', CartDiscountCodeCreateView.as_view(), 
        name='discount_cartdiscountcode_create'),
    url(r'^discount_code/delete/$', CartDiscountCodeDeleteView.as_view(), 
        name='discount_cartdiscountcode_delete'),
    ]

