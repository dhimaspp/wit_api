from rest_framework import generics, viewsets
from .models import *
from .serializers import *
from django.db.models import Min, Max, Count, Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

class UserCsiswaView(APIView):
    permission_classes = [IsAdminUser]
    http_method_names = ['get', 'head']
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UsersCSiswaSerializers(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        self.http_method_names.append("GET")
        serializer = UsersCSiswaSerializers(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class AdminView(APIView):
    permission_classes = [IsAdminUser]
    http_method_names = ['get', 'head']
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = AdminSerializers(users, many=True)
        return Response(serializer.data)
        
    def post(self, request):
        self.http_method_names.append("GET")
        serializer = AdminSerializers(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            {
                "error": True,
                "error_msg": serializer.error_messages,
            },
            status=status.HTTP_400_BAD_REQUEST
        )

# class CSiswaViewSets(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = UsersCSiswaSerializers
#     queryset = UsersCSiswa.objects.all()

class DataCSiswaListViews(generics.ListCreateAPIView):
    queryset = DataCSiswa.objects.all()
    serializer_class = DataCSiswaSerializers
    

class JurusanViewSets(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JurusanSerializers
    queryset = Jurusan.objects.all()

class JurusanListViews(generics.ListCreateAPIView):
    queryset = Jurusan.objects.all()
    serializer_class = JurusanSerializers

# class AdminListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = AdminSerializers



# class JurusanViewSets(generics.RetrieveUpdateDestroyAPIView):
#     perhitungan_jurusan = Jurusan.objects.annotate(Count('siswa_pemilih'))
#     jurusan_terpilih = Jurusan.objects.



