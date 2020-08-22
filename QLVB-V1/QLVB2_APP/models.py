from django.db import models
from datetime import datetime, date
# Create your models here.


class thuchien_m(models.Model):
    thuchien_name = models.CharField(max_length=264)

    def __str__(self):
        return self.thuchien_name

class tiendo(models.Model):
    tiendo_name = models.CharField(max_length=264)

    def __str__(self):
        return self.tiendo_name

# models congtacchuyenmon
class themmoi_m(models.Model):
    stt_name = models.AutoField(primary_key=True)
    doidung_name = models.CharField(max_length=1000)
    thuchien_name = models.ForeignKey(thuchien_m, on_delete=models.CASCADE)
    batdau_name = models.DateField(auto_now_add=True, blank=True)
    ketthuc_name = models.DateField()
    tiendo_name = models.ForeignKey(tiendo, on_delete=models.CASCADE)
    Ghichu_name = models.CharField(max_length=1000)

    def __str__(self):
        return self.doidung_name
class bangcap_m(models.Model):
    stt_bc = models.AutoField(primary_key=True)
    hovaten_bc = models.CharField(max_length=1000)
    bangcap_bc = models.CharField(max_length=1000)
    chungchi_bc = models.CharField(max_length=1000)
    Ghichu_bc = models.CharField(max_length=1000)

    def __str__(self):
        return self.hovaten_bc

class taisan_m(models.Model):
    stt_ts = models.AutoField(primary_key=True)
    tenloai_ts = models.CharField(max_length=1000)
    maso_ts = models.CharField(max_length=1000)
    namduavaosudung_ts = models.DateField()
    soluong_ts_ss = models.CharField(max_length=1000)
    nguyengia_ts_ss = models.CharField(max_length=1000)
    soluong_ts_kk = models.CharField(max_length=1000)
    nguyengia_ts_kk = models.CharField(max_length=1000)
    ghichu_ts = models.CharField(max_length=1000)

    def __str__(self):
        return self.tenloai_ts

class bctuan_m(models.Model):
    stt_bct = models.AutoField(primary_key=True)
    noidung_bct= models.CharField(max_length=10000)
    ghichu_bct = models.CharField(max_length=10000)

    def __str__(self):
        return self.noidung_bct

# models thong ke su co
class duongdan_m(models.Model):
    nguoiupload = models.CharField(max_length=10000, null=True)
    tenfile = models.CharField (max_length=10000, null=True)
    ngayup = models.DateField(auto_now_add=True, null=True)
    duongdan= models.FileField(upload_to='')

    def __str__(self):
        return self.tenfile
