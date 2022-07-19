from rest_framework import serializers
from .models import Student

class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','address']

        # def create(self,validated_data):
        #     return Student.objects.create(validated_data)
        # def update(self,instance,validated_data):
        #     instance.name=validated_data('name',instance.name)
        #     instance.address=validated_data