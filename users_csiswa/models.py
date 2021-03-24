from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator


class User(AbstractUser):
    email = models.EmailField(verbose_name='email',
                              max_length=255, unique=True)
    alamat = models.TextField(null=False, blank=False)
    no_telp = models.CharField(null=True, max_length=255)
    sekolah_asal = models.TextField(null=False, blank=False)
    nama_ortu = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='images/')
    # jurusan = models.ManyToManyField(Jurusan, blank=True, null=True)
    REQUIRED_FIELDS = ['username', 'first_name', 'alamat',
                       'no_telp', 'sekolah_asal', 'nama_ortu', 'foto']
    USERNAME_FIELD = 'email'

    def get_username(self):
        return self.email
    # def __str__(self):
        return "{}".format(self.email)


class Jurusan(models.Model):
    id = models.AutoField(primary_key=True)
    nama_jurusan = models.TextField(null=True, blank=True)
    kuantitas = models.IntegerField(
        default=0, validators=[MaxValueValidator(7), MinValueValidator(0)])
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
# class DataCSiswa(models.Model):
#     id = models.AutoField(primary_key=True)
#     user
#     nama = models.TextField(null=False, blank=False)
#     alamat = models.TextField(null=False, blank=False)
#     no_telp = models.IntegerField(null=False, blank=False)
#     sekolah_asal = models.TextField(null=False, blank=False)
#     nama_ortu = models.TextField(null=False, blank=False)
#     foto = models.ImageField(upload_to='images/')
#     jurusan = models.ManyToManyField(Jurusan, blank=True)

# siswa_pemilih = models.ForeignKey(UsersCSiswa, on_delete=models.CASCADE, validators=[MaxValueValidator(7),MinValueValidator(0)],null=True, blank=True)
