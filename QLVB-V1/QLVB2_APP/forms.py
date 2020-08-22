from django import forms
from django.contrib.auth.forms import UserCreationForm
from django .contrib.auth.models import User
from QLVB2_APP.models import  themmoi_m, tiendo, thuchien_m, bangcap_m, taisan_m, bctuan_m, duongdan_m
from QLVB2_APP import views
from datetime import datetime, date, timedelta
from django.utils.timezone import datetime

# ...................
class CreateUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username',
                  'email','password1', 'password2' ]



class themmoi_f(forms.ModelForm):
    doidung_name = forms.CharField(widget=forms.Textarea, required=True)
    thuchien_name = forms.ModelChoiceField(queryset=thuchien_m.objects.filter(),required=True)
    ketthuc_name = forms.DateTimeInput()
    tiendo_name = forms.ModelChoiceField(queryset=tiendo.objects.all(), required=True)
    Ghichu_name = forms.CharField(widget=forms.Textarea, required=True)

    class Meta():
        model = themmoi_m
        fields = ("__all__")


# bang bangcap
class bangcap_f(forms.ModelForm):
    hovaten_bc = forms.CharField(widget=forms.Textarea, required=True)
    bangcap_bc = forms.CharField(widget=forms.Textarea, required=True)
    chungchi_bc = forms.CharField(widget=forms.Textarea, required=True)
    Ghichu_bc = forms.CharField(widget=forms.Textarea, required=True)

    class Meta():
        model = bangcap_m
        fields = ("__all__")

class taisan_f(forms.ModelForm):
    tenloai_ts = forms.CharField(max_length=1000)
    maso_ts = forms.CharField(max_length=1000,required=False)
    namduavaosudung_ts = forms.DateField()
    soluong_ts_ss = forms.CharField(max_length=1000,required=False)
    nguyengia_ts_ss = forms.CharField(max_length=1000,required=False)
    soluong_ts_kk = forms.CharField(max_length=1000,required=False)
    nguyengia_ts_kk = forms.CharField(max_length=1000,required=False)
    ghichu_ts = forms.CharField(max_length=1000,required=False)

    class Meta():
        model = taisan_m
        fields = ("__all__")

class bctuan_f(forms.ModelForm):
    # stt_bct = forms.CharField(max_length=1000)
    noidung_bct = forms.CharField(widget=forms.Textarea, required=True)
    ghichu_bct = forms.CharField(widget=forms.Textarea, required=True)

    class Meta():
        model = bctuan_m
        fields = ("__all__")

class uploadform_f(forms.ModelForm):
    tenfile = forms.CharField (max_length=10000, required=False)
    nguoiupload = forms.CharField (max_length=10000, required=False)
    # nguoiupload =
    # ngayup = forms.DateField(null=True)
    # duongdan= forms.FileField()

    class Meta():
        model = duongdan_m
        fields = ("__all__")
