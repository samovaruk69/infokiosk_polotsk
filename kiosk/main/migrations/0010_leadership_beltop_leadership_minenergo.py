# Generated by Django 3.2.3 on 2021-05-28 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_leadership_vitebsk'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leadership_Beltop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Leadership_Beltop_photo', models.FileField(upload_to='Leadership_Beltop/')),
                ('times', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Leadership_Minenergo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Leadership_Minenergo_photo', models.FileField(upload_to='Leadership_Minenergo/')),
                ('times', models.DateField()),
            ],
        ),
    ]
