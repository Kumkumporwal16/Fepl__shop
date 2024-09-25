from django.urls import path
from .views import CategoryListView, ProductListView, ProductDetailView ,footwear_view,IndexView,Jewellery_view,Electronic_gadgets_view

from .  import views
urlpatterns = [
    path('index', IndexView.as_view(), name='index'),
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', ProductListView.as_view(), name='product_list'),
    path('product/<int:id>/', ProductDetailView.as_view(), name='product_detail'),
    path('footwear/', footwear_view, name='footwear'),
    path('login/',views.login,name='login'),
    path('loginpage/',views.loginpage,name="loginpage"),
    path('register/',views.register,name="register"),
    path('footwear/',views.footwear,name="footwear"),
    path('jewellery/',views.jewellery,name="jewellery"),
    path('Jewellery/', Jewellery_view, name='jewellery'),
    path('trial/',views.trial,name="trial"),
    path('trial/',views.trial_view,name="trial"),
    path('womenwear/', views.Womenwear_view, name='womenwear'),
    path('makeup/',views.makeup,name="makeup"),
    path('MakeupView/',views.MakeupView.as_view(),name="MakeupView"),
    path('product_detail/<int:id>/', views.product_detail, name='product_detail'),
    path('newarrivals/',views.newarrivals,name="newarrivals"),
    path('newarrivals/',views.newarrivals_view,name="newarrivals"),
    path('featuredproduct/',views.featuredproduct,name="featuredproduct"),
    path('electronicgadgets/',views.electronicgadgets,name="electronicgadgets"),
    path('electronicgadgets/',views.Electronic_gadgets_view,name="electronicgadgets"),
    path('register_user/', views.register_user, name='register_user'),
    #path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    #path('cart/', views.cart_detail, name='cart_detail'),
   path('accessories/',views.accessories,name="accessories"),

] 
