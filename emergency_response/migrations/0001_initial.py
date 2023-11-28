# Generated by Django 3.2.19 on 2023-11-27 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbnormalWarning',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField(choices=[(0, '异常流量'), (1, '异常用户'), (2, '异常主机')], default=0)),
                ('time', models.DateTimeField()),
                ('ip', models.CharField(max_length=20)),
                ('detail', models.TextField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EmailSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email_recipient', models.CharField(max_length=30)),
                ('email_subject', models.CharField(max_length=100)),
                ('email_addresser_name', models.CharField(max_length=100)),
            ],
        ),
    ]
