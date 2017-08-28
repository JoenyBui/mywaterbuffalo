from django.conf.urls import url, include

from .viewsets import ProfileDetailViewSets, UserRoleDetailViewSet
# from .routers import router

urlpatterns = [
    # URLs that do not require a session or valid token
    url(r'^profile/$', ProfileDetailViewSets.as_view(), name='core_profile_detail'),
    url(r'^role/$', UserRoleDetailViewSet.as_view(), name='core_role_detail'),
    # url(r'^friendship/%', include(router.urls, namespace='friendship'))
]
