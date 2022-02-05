

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('', views.insert_student, name="insert_student"),
    path('delete/<id>', views.delete_student, name='delete'),
    path('list/', views.list_students, name='list'),
    path('update/<id>', views.update_student, name='update'),
    path('form/', views.InsertStudent1.as_view(), name='insert'),
    path('form2/', views.InsertStudent2.as_view(), name='insert2'),
    path('listtrack/', views.TrackList.as_view(), name='track'),

]