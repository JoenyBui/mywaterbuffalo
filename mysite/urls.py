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

from polls.views import index

from .view import api_root, api_core, api_rest_auth

urlpatterns = [
    # url(r'^$', index),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

    url(r'rest-auth/$', api_rest_auth, name='rest-auth-root'),
    url(r'rest-auth/', include('rest_auth.urls', namespace='rest-auth')),
    url(r'rest-auth/registration/', include('rest_auth.registration.urls')),

    url(r'core/$', api_core, name='core-root'),
    url(r'core/', include('core.urls', namespace='core')),

    url(r'^$', api_root, name='index'),
]
