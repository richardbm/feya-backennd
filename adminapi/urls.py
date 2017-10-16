from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from adminapi import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet, base_name='users')
router.register(
    r"(?P<app_name>\w+)/(?P<model_name>\w+)",
    views.GenericViewSet,
    base_name="generic"
)

urlpatterns = [
    url(r'^v1/login/$', views.LoginView.as_view(), name='login'),
    # Rest Router urls
    url(r'^v1/', include(router.urls)),
]
