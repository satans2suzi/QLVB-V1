from django.contrib import admin
from QLVB2_APP.models import themmoi_m, tiendo, thuchien_m, bangcap_m, taisan_m, bctuan_m, duongdan_m

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('doidung_name',
                    'thuchien_name','batdau_name',
                    'ketthuc_name','Ghichu_name',
                    'tiendo_name', 'stt_name')

class Tiendo_v(admin.ModelAdmin):
    list_display = ('id','tiendo_name')
class bangcap_v(admin.ModelAdmin):
    list_display = ('stt_bc','hovaten_bc','chungchi_bc', 'bangcap_bc','Ghichu_bc')
class taisan_v(admin.ModelAdmin):
    list_display = ('stt_ts','tenloai_ts','maso_ts', 'namduavaosudung_ts','soluong_ts_ss','nguyengia_ts_ss','soluong_ts_kk','nguyengia_ts_kk','ghichu_ts')
class thuchien_v(admin.ModelAdmin):
    list_display = ('id','thuchien_name')
class bctuan_v(admin.ModelAdmin):
    list_display = ('stt_bct','noidung_bct')
class duongdan_V(admin.ModelAdmin):
    list_display = ('duongdan','tenfile', 'ngayup', 'nguoiupload')
# Register your models here.
admin.site.register(themmoi_m, AuthorAdmin)
admin.site.register (tiendo, Tiendo_v)
admin.site.register(thuchien_m, thuchien_v)
admin.site.register(bangcap_m, bangcap_v)
admin.site.register(taisan_m, taisan_v)
admin.site.register(bctuan_m, bctuan_v)
admin.site.register(duongdan_m, duongdan_V)
