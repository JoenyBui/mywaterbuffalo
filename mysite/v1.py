from django.conf.urls import include, url

from editor.routers import router as editor_router
from classroom.routers import router as classroom_router

from problem.routers import router as problem_router
from mathematics.routers import router as math_router
from readings.routers import router as reading_router
from topic.routers import router as topic_router
# from core.routers import router as core_router

__author__ = 'jbui'


urlpatterns = [
    # url(r'^core/', include(core_router.urls, namespace='core')),
    url(r'^classroom/', include(classroom_router.urls, namespace='classroom')),
    url(r'^editor/', include(editor_router.urls, namespace='editor')),
    url(r'^problem/', include(problem_router.urls, namespace='problem')),
    url(r'^math/', include(math_router.urls, namespace='math')),
    url(r'^reading/', include(reading_router.urls, namespace='reading')),
    url(r'^topic/', include(topic_router.urls, namespace='topic'))
]
