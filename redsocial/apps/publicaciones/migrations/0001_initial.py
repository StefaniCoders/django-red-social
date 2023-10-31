# Generated by Django 4.2.6 on 2023-10-31 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'ordering': ['usuario', 'fecha', 'descripcion'],
            },
        ),
        migrations.CreateModel(
            name='PublicacionReaccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('reaccion', models.IntegerField(choices=[(0, 'Me divierte'), (1, 'Me enoja'), (2, 'Me entristese'), (3, 'Me gusta'), (4, 'Me encorazona'), (5, 'No me Gusta')])),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.publicacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'ordering': ['publicacion', 'usuario', 'fecha', 'reaccion'],
            },
        ),
        migrations.CreateModel(
            name='PublicacionFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.IntegerField(choices=[(0, 'FOTO'), (1, 'VIDEO'), (2, 'GIF')])),
                ('media', models.FileField(blank=True, null=True, upload_to='filesPublicaciones/')),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.publicacion')),
            ],
            options={
                'ordering': ['publicacion', 'media'],
            },
        ),
        migrations.CreateModel(
            name='PublicacionComentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField()),
                ('publicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.publicacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.usuario')),
            ],
            options={
                'ordering': ['publicacion', 'usuario', 'fecha', 'descripcion'],
            },
        ),
    ]
