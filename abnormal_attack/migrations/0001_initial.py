# Generated by Django 4.1 on 2023-11-27 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbnormalHost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=20)),
                ('name', models.CharField(default='', max_length=100)),
                ('errprint', models.CharField(default='', max_length=200)),
                ('time', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AbnormalTraffic',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField(default=0)),
                ('time', models.DateTimeField()),
                ('src_ip', models.CharField(max_length=20)),
                ('dst_ip', models.CharField(max_length=20)),
                ('detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AbnormalUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField(default=0)),
                ('time', models.DateTimeField()),
                ('user_name', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=200)),
                ('src_ip', models.CharField(max_length=20)),
            ],
        ),
    ]
