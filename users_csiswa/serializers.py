from users_csiswa.models import DataCSiswa, Jurusan, User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

# class UsersCSiswaSerializers(serializers.ModelSerializer):
#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user
    
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#         validators = [UniqueTogetherValidator(
#             queryset=User.objects.all(),
#             fields=['username', 'email']
#         )]
class JurusanSerializers(serializers.ModelSerializer):
    # siswa_pemilih = UsersCSiswaSerializers(many=True)
    class Meta:
        model = Jurusan
        fields = ('id', 'nama_jurusan', 'kuantitas')
        
class DataCSiswaSerializers(serializers.ModelSerializer):
    jurusan = JurusanSerializers(many=True)
    class Meta:
        model = DataCSiswa
        fields = ('id', 'email', 'username', 'first_name','alamat', 'no_telp', 'sekolah_asal', 'nama_ortu', 'foto', 'jurusan')

class AdminSerializers(serializers.ModelSerializer):
    # def create(self, validated_data):
    #     user = User.objects.create_user(**validated_data)
    #     return user
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_staff')
        # validators = [UniqueTogetherValidator(
        #     queryset=User.objects.all(),
        #     fields=['username', 'email']
        # )]



