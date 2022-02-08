from rest_framework import serializers
from app.models import Student, Myuser, Track

class Studentserializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        # fields=['id', 'studentname', 'studentemail']
        fields = '__all__'

class Myuserserializers(serializers.ModelSerializer):
    class Meta:
        model = Myuser
        fields=['id', 'myusername', 'userEmail']

class Trackserializers(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields=['id','trackname']