from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/',include('new_app.urls')),
    path('api/blog/',include('blog_manage.urls')),
    path('api/comment/',include('comment_manage.urls')),
    
]
