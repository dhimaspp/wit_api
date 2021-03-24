from users_csiswa.models import DataCSiswa, Jurusan, User
from rest_framework import serializers

class DataCSiswaCreateSerializers(serializers.ModelSerializer):
    jurusan = JurusanSerializers(many=True)
    class Meta:
        model = DataCSiswa
        fields = ('id', 'email', 'username', 'first_name','alamat', 'no_telp', 'sekolah_asal', 'nama_ortu', 'foto', 'jurusan')
