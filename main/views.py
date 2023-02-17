from main.models import Student
from main.serializers import StudentSerializer
from rest_framework import generics
from rest_framework.response import Response
from django.forms import model_to_dict

# Create your views here.

# class StudentView(APIView):

#     def get(self, request):
#         lst = Student.objects.all().values()
#         return Response({'Student':list(lst)})

#     def post(self, request):
#         post_new = Student.objects.create(
#             first_name = request.data['first_name'],
#             last_name = request.data['last_name'],
#             age = request.data['age'],
#             gender = request.data['gender']
#         )
#         return Response({'post':model_to_dict(post_new)})

class StudentListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreateView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveView(generics.RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDestroyView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer