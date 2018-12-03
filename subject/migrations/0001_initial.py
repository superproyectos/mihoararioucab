# Generated by Django 2.1.3 on 2018-11-30 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('subject_id', models.AutoField(primary_key=True, serialize=False)),
                ('semester', models.CharField(max_length=5)),
                ('nrc', models.CharField(max_length=10)),
                ('teacher', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('monday', models.CharField(max_length=4)),
                ('tuesday', models.CharField(max_length=4)),
                ('wednesday', models.CharField(max_length=4)),
                ('thursday', models.CharField(max_length=4)),
                ('friday', models.CharField(max_length=4)),
                ('saturday', models.CharField(max_length=4)),
                ('sunday', models.CharField(max_length=4)),
            ],
        ),
    ]
