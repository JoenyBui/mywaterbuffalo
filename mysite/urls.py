# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls import include, url
from django.contrib import admin

from rest_framework.authtoken import views as restful_view
from rest_framework_jwt.views import obtain_jwt_token

from rest_framework_swagger.views import get_swagger_view

from polls.views import index

from .view import HomeView
from .view import api_root, api_v1_root, api_rest_auth, api_core, schema_view

swagger_view = get_swagger_view(title='Water Buffalo API')


urlpatterns = [
    # url(r'^$', index),
    url(r'^grappelli/', include('grappelli.urls')),

    url(r'^$', HomeView.as_view(), name='home'),

    url(r'api-token-auth/', restful_view.obtain_auth_token, name="api-token"),
    url(r'api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # Apps
    url(r'^math/', include('mathematics.urls')),
    url(r'^friendship/', include('friendship.urls')),

    # API
    url(r'^api/$', api_root, name='index'),
    url(r'^api/v1/$', api_v1_root, name='v1-root'),
    url(r'^api/v1/', include(('mysite.v1', 'v1'), namespace='v1')),
    url(r'^api/rest-auth/$', api_rest_auth, name='rest-auth-root'),
    url(r'^api/rest-auth/', include(('rest_auth.urls', 'rest-auth'), namespace='rest-auth')),
    url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/core/$', api_core, name='core-root'),
    url(r'^api/core/', include(('core.urls', 'core'), namespace='core')),
    url(r'^api/docs/', swagger_view, name='api_docs'),

    # Admin
    url(r'^admin/', admin.site.urls, 'admin'),
]
