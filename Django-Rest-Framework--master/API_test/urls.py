from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url


from blog.urls import router as blog_router


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'api/',include(blog_router.urls))
]
