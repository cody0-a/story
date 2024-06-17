
from django.contrib import admin
from django.urls import include, path


app_name = 'tell_story'
app_name = 'users'
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('users.urls')),
    path('users/', include('users.urls',namespace='users')),
    path('tell_story/', include('tell_story.urls',namespace='tell_story')),
]
