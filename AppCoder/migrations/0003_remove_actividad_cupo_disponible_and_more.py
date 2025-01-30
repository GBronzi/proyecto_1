# Generated by Django 5.1.5 on 2025-01-29 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_actividad_cupo_disponible_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actividad',
            name='cupo_disponible',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='cupo_maximo',
        ),
        migrations.RemoveField(
            model_name='actividad',
            name='instructor',
        ),
        migrations.AddField(
            model_name='actividad',
            name='especialidad',
            field=models.CharField(choices=[('musculacion', 'Musculación'), ('spinning', 'Spinning'), ('yoga', 'Yoga'), ('bailoterapia', 'Bailoterapia'), ('natacion', 'Natación'), ('crossfit', 'Crossfit'), ('entrenamiento funcional', 'Entrenamiento funcional')], default='musculacion', max_length=50),
            preserve_default=False,
        ),
    ]
