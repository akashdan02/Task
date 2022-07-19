from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializers
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class StudentAPIView(APIView):

    def get(self, request):
        data = Student.objects.all()
        serializer = StudentSerializers(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetails(APIView):

    def get_object(self, id):
        try:
            return Student.objects.get(id=id)
        except Student.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializers(Student)
        return Response(serializer.data)

    def put(self, request, id):
        student = self.get_object(id)
        serializer = StudentSerializers(Student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        student = self.get_object(id)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def Student_lists(request):
    if request.method == 'GET':
        data = Student.objects.all()
        serializer = StudentSerializers(data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=StudentSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    try:
        student=Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return HttpResponse (status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializers(student)
        return Response(serializer.data)

    elif request.method == 'PUT':

        serializer = StudentSerializers(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
