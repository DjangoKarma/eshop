from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('shop/<str:mc>/<str:sc>/<str:br>/',views.shop),
    path('single_product/<int:id>/',views.singleProduct),
    path('login/',views.loginPage),
    path('logout/',views.logoutPage),
    path('signup/',views.signupPage),
    path('profile/',views.profilePage),
    path("update_profile/",views.updateProfilePage),
    path("add-to-cart/<int:id>/",views.addToCart),
    path("cart/",views.cartPage),
    path("delete-cart/<int:pid>",views.deletecart),
    path("update-cart/<int:pid>/<str:op>/",views.updatecart),
    path("add-to-wishlist/<int:pid>/",views.addToWishlist),
    path("delete-wishlist/<int:pid>/",views.deleteWishlist),
    path("checkout/",views.CheckoutPage),
    path("order/",views.orderPage),
    path("confirmation/",views.ConfirmationPage),
    path("contact/",views.contactPage),
    path("search/",views.searchPage),
    path("forget_username/",views.forgetUsername),
    path("forget_otp/",views.forgetOTP),
    path("forget_password/",views.forgetPassword),
    path("paymentSuccess/<str:rppid>/",views.paymentSuccess),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

