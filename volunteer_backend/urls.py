from django.conf.urls import url, include
from django.contrib import admin

from graphene_django.views import GraphQLView

from rest_framework import routers
from volunteer_backend.user import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


# from volunteer_backend.user import schema

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),
]