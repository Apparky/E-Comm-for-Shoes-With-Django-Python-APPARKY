from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('shop/<slug:p_slug>/', views.ProductDetails),
    path('shop/', views.shop, name='shop'),
    path('contactus/', views.contactus, name='contactus'),
    path('submit/', views.submit, name='submit'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug_>/', views.blog_content),
    path('faq/', views.faq, name='faq'),
    path('ourPolicy/', views.policies, name='policy'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
