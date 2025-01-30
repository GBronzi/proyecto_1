# Generated by Django 5.1.4 on 2025-01-13 19:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_instructor_socio_delete_estudiante_delete_profesor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('duracion', models.DurationField(help_text='Duración de la actividad (ejemplo: 01:30:00)')),
                ('horario', models.TimeField(help_text='Hora de inicio de la actividad')),
                ('cupo_maximo', models.IntegerField(help_text='Cantidad máxima de participantes')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='actividades', to='AppCoder.instructor')),
            ],
        ),
    ]
