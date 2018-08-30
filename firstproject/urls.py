"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from myapp import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'product', views.ProductViewSet)
#router.register(r'post', views.PostViewSet)
router.register(r'event', views.EventViewSet)
router.register(r'album', views.AlbumViewSet)
router.register(r'order', views.OrderViewSet)
router.register(r'member', views.MemberViewSet)
router.register(r'message', views.MessageViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'post/(?P<post_id>\d+)/$', views.PostDetailView.as_view(), name = 'post_detail'),
    url(r'post/(?P<slug>[-\w]+)/$', views.PostDetailView.as_view(), name = 'post_detail_slug'),
    url(r'^posts/$', views.post_list),
    url(r'^posts/(?P<pk>[0-9]+)$', views.post_detail),
    
    # 帳號登入登出
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),     
    # 首頁
    url(r'^$', views.index),
    url(r'^index/$', views.index),    
    # 商品
#    url(r'^listProducts/$', views.listProducts),     
#    url(r'^listProducts_ajax_url/$', views.listProducts_asJson, name='listProducts_ajax_url'),
    url(r'^api/gbl/', include(router.urls)),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)