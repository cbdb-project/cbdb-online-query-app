"""cbdbweb URL Configuration

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
from django.conf.urls import url
from django.contrib import admin

from django.views.generic import TemplateView
from backend.views import person_list, person_info, person_year, person_address, person_altname, person_posting

from backend.apis import(
    PersonListViewSet, PersonInfoViewSet, PersonYearViewSet, PersonAddrViewSet, 
    PersonAltNameViewSet, PersonPostViewSet, PersonEntryViewSet, PersonStatusViewSet,
    PersonKinshipViewSet, PersonAssociationViewSet
)
from rest_framework.routers import DefaultRouter
from django.conf.urls import url, include
from rest_framework.documentation import include_docs_urls


router = DefaultRouter()
#router.register(r'personList', PersonListViewSet, basename='api-personList')
router.register(r'personList/(?P<personName>.+)', PersonListViewSet, basename='api-personList')
router.register(r'personInfo/(?P<personId>\d+)', PersonInfoViewSet, basename='api-personInfo')
router.register(r'personYear/(?P<personId>\d+)', PersonYearViewSet, basename='api-personYear')
router.register(r'personAddr/(?P<personId>\d+)', PersonAddrViewSet, basename='api-personAddr')
router.register(r'personAltName/(?P<personId>\d+)', PersonAltNameViewSet, basename='api-personAltName')
router.register(r'personPost/(?P<personId>\d+)', PersonPostViewSet, basename='api-personPost')
router.register(r'personEntry/(?P<personId>\d+)', PersonEntryViewSet, basename='api-personEntry')
router.register(r'personStatus/(?P<personId>\d+)', PersonStatusViewSet, basename='api-personStatus')
router.register(r'personKinship/(?P<personId>\d+)', PersonKinshipViewSet, basename='api-personKinship')
router.register(r'personAssociation/(?P<personId>\d+)', PersonAssociationViewSet, basename='api-personAssociation')


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^api/person_list/(?P<personName>.+)/$', person_list),#获取人物列表
    url(r'^api/biog_base_info/(?P<personId>\d+)/$', person_info),#获取人物详细信息-基本信息
    url(r'^api/biog_bd_year/(?P<personId>\d+)/$', person_year),#获取人物详细信息-生卒年
    url(r'^api/biog_address/(?P<personId>\d+)/(?P<start>\d+)/(?P<list>\d+)/$', person_address),#获取人物详细信息-地址
    url(r'^api/biog_alt_name/(?P<personId>\d+)/(?P<start>\d+)/(?P<list>\d+)/$', person_altname),#获取人物详细信息-别名
    url(r'^api/biog_posting/(?P<personId>\d+)/(?P<start>\d+)/(?P<list>\d+)/$',person_posting),#获取人物详细信息-官职
    #获取人物详细信息-入仕途径
    #获取人物详细信息-入仕途径
    #获取人物详细信息-亲属关系
    #获取人物详细信息-社会关系
    #获取人物详细信息-数据来源
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^api/docs/', include_docs_urls(title='CBDB apis')),
]
