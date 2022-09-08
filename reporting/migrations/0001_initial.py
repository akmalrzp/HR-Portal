# Generated by Django 4.0 on 2022-09-03 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TempDataLengkap092022',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idpegawai', models.IntegerField(db_column='IDPegawai')),
                ('nip', models.CharField(blank=True, db_column='NIP', max_length=18, null=True)),
                ('nipbaru', models.CharField(blank=True, db_column='NIPBaru', max_length=18, null=True)),
                ('namalengkap', models.CharField(blank=True, db_column='NamaLengkap', max_length=8000, null=True)),
                ('kodekelamin', models.CharField(db_column='KodeKelamin', max_length=1)),
                ('kodegolongan', models.CharField(blank=True, db_column='KodeGolongan', max_length=5, null=True)),
                ('kodegolonganruang', models.CharField(blank=True, db_column='KodeGolonganRuang', max_length=5, null=True)),
                ('jenjangjabatan', models.CharField(blank=True, db_column='JenjangJabatan', max_length=50, null=True)),
                ('jabatan', models.CharField(blank=True, db_column='Jabatan', max_length=255, null=True)),
                ('singkatanjenjang', models.CharField(blank=True, db_column='SingkatanJenjang', max_length=5, null=True)),
                ('pendidikan', models.CharField(blank=True, db_column='Pendidikan', max_length=50, null=True)),
                ('esl1', models.TextField(db_column='Esl1')),
                ('esl2', models.TextField()),
                ('esl3', models.TextField()),
                ('esl4', models.TextField()),
                ('tahunpensiun', models.IntegerField(blank=True, db_column='TahunPensiun', null=True)),
                ('statuspegawai', models.CharField(blank=True, db_column='StatusPegawai', max_length=100, null=True)),
                ('ckp', models.FloatField(db_column='CKP')),
                ('np', models.FloatField(db_column='NP')),
                ('generasi', models.CharField(blank=True, db_column='Generasi', max_length=11, null=True)),
                ('provinsikantor', models.CharField(blank=True, db_column='ProvinsiKantor', max_length=50, null=True)),
                ('kotakantor', models.CharField(blank=True, db_column='KotaKantor', max_length=50, null=True)),
            ],
            options={
                'db_table': 'Temp_Data_lengkap_092022',
                'managed': False,
            },
        ),
    ]
