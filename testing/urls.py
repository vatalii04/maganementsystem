
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('1/', include('blog.urls')),
    path('5/', include('forum.urls')),
]
