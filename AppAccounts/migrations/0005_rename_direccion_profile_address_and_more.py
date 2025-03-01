# Generated by Django 5.1.5 on 2025-01-29 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppAccounts', '0004_rename_fecha_de_nacimineto_profile_fecha_de_nacimiento_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='direccion',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='biografia',
            new_name='bio',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='fecha_de_nacimiento',
            new_name='birthday',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='telefono',
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatars/user.png', upload_to='avatars/'),
        ),
    ]
