from django.urls import path
from . import views


app_name = 'tell_story'
urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.rooms, name='rooms'),
    path('room/<int:room_id>', views.rooms, name='room'),
    path('stories/', views.stories, name='stories'),
    path('story/<int:story_id>', views.stories, name='story'),
    path('add-story/', views.add_story, name='add_story'),
    path('edit-story/<int:story_id>', views.edit_story, name='edit_story'),
    path('delete-story/<int:story_id>', views.delete_story, name='delete_story'),
    path('add-comment/<int:story_id>', views.add_comment, name='add_comment'),
]