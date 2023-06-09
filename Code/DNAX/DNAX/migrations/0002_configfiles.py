# Generated by Django 3.1.2 on 2020-11-02 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PAT', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfigFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='ConfigFiles')),
            ],
            options={
                'unique_together': {('file_name',)},
            },
        ),
    ]
