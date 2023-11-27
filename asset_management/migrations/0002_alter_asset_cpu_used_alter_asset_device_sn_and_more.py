# Generated by Django 4.1 on 2023-11-27 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='cpu_used',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='device_sn',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='device_type',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='device_vendor',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='device_working_hours',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='mac',
            field=models.CharField(blank=True, default='', max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='name',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='network_speed',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='os',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='position',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='remain_harddisk',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='remain_mem',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='asset',
            name='update_time',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='assetdeviceinfo',
            name='time',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='assetservice',
            name='cpe',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='assetservice',
            name='extrainfo',
            field=models.CharField(blank=True, default='', max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='assetservice',
            name='name',
            field=models.CharField(blank=True, default='', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='assetservice',
            name='product',
            field=models.CharField(blank=True, default='', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='assetservice',
            name='state',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='assetservice',
            name='update_time',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='assetservice',
            name='version',
            field=models.CharField(blank=True, default='', max_length=45, null=True),
        ),
        migrations.AlterField(
            model_name='jtopodevices',
            name='title',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='productionline',
            name='shortened',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='shortened',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]