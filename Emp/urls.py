from django.urls import path
from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'emp', views.EmpViewSet)

urlpatterns = [
    path('index/', views.index, name='index'),
    path('signup/', views.register, name='signup'),
    path('id/', views.prolink, name='prolink'),
    path('id/<myid>', views.displayDet),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('login/', views.login1, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("update/<int:pk>/", views.UpdateEmpAPIView.as_view(), name="update_todo"),

] + static(settings.MEDIA_DIR, document_root=settings.MEDIA_ROOT)
