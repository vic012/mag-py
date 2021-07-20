from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api import views

schema_view = get_schema_view(
   openapi.Info(
      title="MagPy-Pedro",
      default_version='v1',
      description="API de verificação e autenticação de versionamento de pacotes",
      terms_of_service="#",
      contact=openapi.Contact(email="henriquevic012@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.SimpleRouter()
router.register(r'projects', views.ProjectViewSet, basename='Projects')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('doc-sw/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('doc-re/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
