from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Jurusan(models.Model):
    id = models.AutoField(primary_key=True)
    nama_jurusan = models.TextField(null=True, blank=True)
    kuantitas = models.IntegerField(default=0, validators=[MaxValueValidator(7),MinValueValidator(0)])

class DataCSiswa(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    alamat = models.TextField(null=False, blank=False)
    no_telp = models.CharField(null=True)
    sekolah_asal = models.TextField(null=False, blank=False)
    nama_ortu = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='images/')
    jurusan = models.ManyToManyField(Jurusan, blank=True, )
    REQUIRED_FIELDS = ['username', 'first_name', 'alamat', 'no_telp', 'sekolah_asal', 'nama_ortu', 'foto', 'jurusan']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
# class DataCSiswa(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_csiswa = models.ForeignKey(User, on_delete=models.CASCADE)
#     nama = models.TextField(null=False, blank=False)
#     alamat = models.TextField(null=False, blank=False)
#     no_telp = models.IntegerField(null=False, blank=False)
#     sekolah_asal = models.TextField(null=False, blank=False)
#     nama_ortu = models.TextField(null=False, blank=False)
#     foto = models.ImageField(upload_to='images/')
#     jurusan = models.ManyToManyField(Jurusan, blank=True, )


    # siswa_pemilih = models.ForeignKey(UsersCSiswa, on_delete=models.CASCADE, validators=[MaxValueValidator(7),MinValueValidator(0)],null=True, blank=True)
