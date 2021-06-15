from django.urls import path
from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', views.register, name='signup'),
    path('id/', views.prolink, name='prolink'),
    path('id/<myid>', views.displayDet),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('login/', views.login1, name='login'),
    path('/logout', views.logout, name='logout')
] + static(settings.MEDIA_DIR, document_root=settings.MEDIA_ROOT)
