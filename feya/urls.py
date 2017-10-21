"""fenixcargo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from accounts import views as accounts_views
from adminapi.views import GenericViewSet, DateContactView

router = routers.DefaultRouter()
router.register(
    r"ministry/datecontact",
    DateContactView,
    base_name="date-contact"
)
router.register(
    r"(?P<app_name>\w+)/(?P<model_name>\w+)",
    GenericViewSet,
    base_name="generic"
)

urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/login/', accounts_views.LoginView.as_view()),
    url(r'^api/profile/', accounts_views.ProfileView.as_view()),
    url(r'^api/signup/', accounts_views.SignupView.as_view()),
    url(r'^api/request-recover-password/', accounts_views.RequestRecoverPassword.as_view()),
    url(r'^api/recover-password/', accounts_views.RecoverPassword.as_view()),

]
from django.conf import settings
from django.views.static import serve

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    ]

