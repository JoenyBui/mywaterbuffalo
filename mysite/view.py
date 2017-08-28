from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.schemas import SchemaGenerator
from rest_framework import permissions

from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


@api_view(('GET', ))
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    return Response({
        # "v1": reverse("v1-root", request=request, format=format),
        "core": reverse("core-root", request=request, format=format),
        #"api token auth": reverse("api-token", request=request, format=format),
        # "documents": reverse("docs", request=request, format=format),
        "accounts": reverse("rest-auth-root", request=request, format=format)
    })


@api_view(('GET', ))
@permission_classes((permissions.AllowAny,))
def api_rest_auth(request, format=None):
    return Response({
        "user": reverse("rest-auth:rest_user_details", request=request, format=format),
        "login": reverse("rest-auth:rest_login", request=request, format=format),
        "logout": reverse("rest-auth:rest_logout", request=request, format=format),
        "registration": reverse("rest_register", request=request, format=format),
    })


@api_view(('GET', ))
@permission_classes((permissions.AllowAny,))
def api_core(request, format=None):
    return Response({
        "profile": reverse("core:core_profile_detail", request=request, format=format),
        "role": reverse("core:core_role_detail", request=request, format=format)
    })
