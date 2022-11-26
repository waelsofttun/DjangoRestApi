from django.urls import include, path
from rest_framework import routers
from apistage import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'Offers', views.OffersViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/<str:file>', views.resume),
    path('recom/<str:profile>/', views.recomandation),
    path('scr/<str:key>/', views.scraping),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]