from django import forms
from models import *

class CSiswaForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UsersCSiswa
        fields = ('id','email','password','nama','alamat', 'no_telp', 'sekolah_asal', 'nama_ortu', 'foto')