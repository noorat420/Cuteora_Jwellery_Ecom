from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name="home"),
    path('products/',views.productlist,name='products'),
    path('products/<int:prodid>/',views.productdetail,name='productdetail'),
    path('contact/',views.contact,name='contact'),
    path('cart/', views.cart_detail, name='cart'),
    path('cart/add/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('signup/', views.sign_up_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
     path('about/',views.about,name='about'),

]
if settings.DEBUG:  # serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)