# Generated by Django 3.0.3 on 2020-04-08 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatosEquipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_PC', models.CharField(max_length=30)),
                ('Tipo', models.CharField(max_length=30, null=True)),
                ('Marca', models.CharField(max_length=30, null=True)),
                ('Modelo', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DatosUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Usuario', models.CharField(max_length=30, null=True)),
                ('departamento', models.CharField(max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimientos_equipos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Observaciones', models.TextField(blank=True, verbose_name='Observaciones')),
                ('Datos_equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.DatosEquipo')),
            ],
        ),
        migrations.AddField(
            model_name='datosequipo',
            name='Usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datos.DatosUsuario'),
        ),
    ]
