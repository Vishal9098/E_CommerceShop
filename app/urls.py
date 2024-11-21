from django.urls import path 
from app import views 
from django.conf import settings 
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views 
from django.contrib.auth.views import LogoutView
from .forms import LoginForm , MyPasswordChangeForm

from django.contrib.auth import views as auth_views
# from .views import CustomerRegistrationView
urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),

    # path('card/', views.show_cart, name='showcart'),


    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),


    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    # path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),


    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),

  


    # path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('accountss/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'),name='logout'),

    # path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=MyPasswordChangeForm), name='passwordchange'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
