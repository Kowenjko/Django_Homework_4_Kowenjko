
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls.conf import include, re_path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('blog.urls')),
    re_path(r'', include('blog.urls'))
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_BASE,
#                           document_root=settings.MEDIA_ROOT)
handler404 = "mysite.views.page_not_found"
