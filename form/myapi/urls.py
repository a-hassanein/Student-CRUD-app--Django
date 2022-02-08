from django.urls import path, include
from rest_framework import routers
from .views import notser, StudentList, TrackList, MyuserList , list_student, StudentAPI, GenericStudentAPI, student_details, student_detail, Generic_Student_details

router = routers.DefaultRouter()
router.register(r'Student', StudentList)
router.register(r'Track', TrackList)
router.register(r'User', MyuserList)
# router.register(r'list', student_list)

urlpatterns = [
    # path('', notser, name='notser'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('listt/',list_student ,name = 'studentlist'),
    path('listt2/',StudentAPI.as_view(), name = 'studentlist2'),
    path('listt3/', GenericStudentAPI.as_view(), name='studentlist3'),
    path('details/<id>', student_details.as_view(), name='studentdetails'),
    path('stddetails/<pk>', student_detail, name='studentdetails2'),
    path('gendetails/<id>', Generic_Student_details.as_view(), name='studentdetails3'),
]