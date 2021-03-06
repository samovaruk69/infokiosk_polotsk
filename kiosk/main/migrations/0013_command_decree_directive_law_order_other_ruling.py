# Generated by Django 3.2.3 on 2021-05-30 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_absence_notice_application_for_cylinder_acceptance_application_for_financing_construction_and_instal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Command_doc', models.FileField(upload_to='list_of_normative_documents/')),
                ('times', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Decree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Decree_doc', models.FileField(upload_to='list_of_normative_documents/')),
                ('times', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Directive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Directive_doc', models.FileField(upload_to='list_of_normative_documents/')),
                ('times', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Law',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Law_doc', models.FileField(upload_to='list_of_normative_documents/')),
                ('times', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Order_doc', models.FileField(upload_to='list_of_normative_documents/')),
                ('times', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Other_doc', models.FileField(upload_to='list_of_normative_documents/')),
                ('times', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Ruling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('Ruling_doc', models.FileField(upload_to='list_of_normative_documents/')),
                ('times', models.DateField()),
            ],
        ),
    ]
