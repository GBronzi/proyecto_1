# Generated by Django 5.1.4 on 2025-01-30 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('especialidad', models.CharField(choices=[('musculacion', 'Musculación'), ('spinning', 'Spinning'), ('yoga', 'Yoga'), ('bailoterapia', 'Bailoterapia'), ('natacion', 'Natación'), ('crossfit', 'Crossfit'), ('entrenamiento funcional', 'Entrenamiento funcional')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Socio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('edad', models.PositiveIntegerField()),
                ('telefono', models.CharField(max_length=20)),
                ('tipo_clase', models.CharField(choices=[('musculacion', 'Musculación'), ('spinning', 'Spinning'), ('yoga', 'Yoga'), ('bailoterapia', 'Bailoterapia'), ('natacion', 'Natación'), ('crossfit', 'Crossfit'), ('pase libre', 'Pase libre')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('duracion', models.CharField(choices=[('00:30:00', '30 minutos'), ('01:00:00', '1 hora'), ('01:30:00', '1 hora y 30 minutos'), ('02:00:00', '2 horas')], default='01:00:00', max_length=8)),
                ('especialidad', models.CharField(choices=[('musculacion', 'Musculación'), ('spinning', 'Spinning'), ('yoga', 'Yoga'), ('bailoterapia', 'Bailoterapia'), ('natacion', 'Natación'), ('crossfit', 'Crossfit'), ('entrenamiento funcional', 'Entrenamiento funcional')], max_length=50)),
                ('horario', models.CharField(choices=[('06:00:00', '06:00 AM'), ('07:00:00', '07:00 AM'), ('08:00:00', '08:00 AM'), ('09:00:00', '09:00 AM'), ('10:00:00', '10:00 AM'), ('11:00:00', '11:00 AM'), ('12:00:00', '12:00 PM'), ('13:00:00', '01:00 PM'), ('14:00:00', '02:00 PM'), ('15:00:00', '03:00 PM'), ('16:00:00', '04:00 PM'), ('17:00:00', '05:00 PM'), ('18:00:00', '06:00 PM'), ('19:00:00', '07:00 PM'), ('20:00:00', '08:00 PM')], default='06:00:00', max_length=8)),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actividades', to='AppCoder.instructor')),
            ],
        ),
    ]
