# Generated by Django 3.0.8 on 2020-07-08 00:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bangcap_m',
            fields=[
                ('stt_bc', models.AutoField(primary_key=True, serialize=False)),
                ('hovaten_bc', models.CharField(max_length=1000)),
                ('bangcap_bc', models.CharField(max_length=1000)),
                ('chungchi_bc', models.CharField(max_length=1000)),
                ('Ghichu_bc', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='bctuan_m',
            fields=[
                ('stt_bct', models.AutoField(primary_key=True, serialize=False)),
                ('noidung_bct', models.CharField(max_length=10000)),
                ('ghichu_bct', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='taisan_m',
            fields=[
                ('stt_ts', models.AutoField(primary_key=True, serialize=False)),
                ('tenloai_ts', models.CharField(max_length=1000)),
                ('maso_ts', models.CharField(max_length=1000)),
                ('namduavaosudung_ts', models.DateField()),
                ('soluong_ts_ss', models.CharField(max_length=1000)),
                ('nguyengia_ts_ss', models.CharField(max_length=1000)),
                ('soluong_ts_kk', models.CharField(max_length=1000)),
                ('nguyengia_ts_kk', models.CharField(max_length=1000)),
                ('ghichu_ts', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='thuchien_m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thuchien_name', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='tiendo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiendo_name', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='themmoi_m',
            fields=[
                ('stt_name', models.AutoField(primary_key=True, serialize=False)),
                ('doidung_name', models.CharField(max_length=1000)),
                ('batdau_name', models.DateField(auto_now_add=True)),
                ('ketthuc_name', models.DateField()),
                ('Ghichu_name', models.CharField(max_length=1000)),
                ('thuchien_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QLVB2_APP.thuchien_m')),
                ('tiendo_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='QLVB2_APP.tiendo')),
            ],
        ),
    ]