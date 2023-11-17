# Generated by Django 4.1 on 2023-11-17 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=20)),
                ('asset_name', models.CharField(default='', max_length=100)),
                ('position', models.CharField(default='', max_length=100)),
                ('device_sn', models.CharField(default='', max_length=100)),
                ('device_vendor', models.CharField(default='', max_length=100)),
                ('device_type', models.CharField(default='', max_length=100)),
                ('device_working_hours', models.CharField(default='', max_length=100)),
                ('cpu_used', models.FloatField(default=0)),
                ('remain_mem', models.FloatField(default=0)),
                ('remain_harddisk', models.FloatField(default=0)),
                ('network_speed', models.FloatField(default=0)),
                ('os', models.CharField(default='', max_length=100)),
                ('mac', models.CharField(default='', max_length=80)),
                ('update_time', models.CharField(default='', max_length=50)),
                ('productionline_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='AssetService',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('asset_id', models.IntegerField(default=0)),
                ('ip', models.CharField(max_length=20)),
                ('port', models.IntegerField()),
                ('state', models.CharField(default='', max_length=10)),
                ('name', models.CharField(default='', max_length=45)),
                ('product', models.CharField(default='', max_length=45)),
                ('version', models.CharField(default='', max_length=45)),
                ('cpe', models.CharField(default='', max_length=100)),
                ('extrainfo', models.CharField(default='', max_length=60)),
                ('update_time', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JtopoDevices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(default='', max_length=50)),
                ('title', models.CharField(default='', max_length=200)),
                ('imgUrl', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='JtopoFilePath',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topo_id', models.CharField(max_length=100)),
                ('topo_src', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Productionline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('workshop_id', models.IntegerField(default=0)),
                ('shortened', models.CharField(default='', max_length=50)),
                ('asset_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('shortened', models.CharField(default='', max_length=50)),
                ('productionline_number', models.IntegerField(default=0)),
            ],
        ),
    ]
