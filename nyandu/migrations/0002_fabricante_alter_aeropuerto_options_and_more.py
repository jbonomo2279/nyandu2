# Generated by Django 5.0.4 on 2024-05-10 19:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("nyandu", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fabricante",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        help_text="Nombre del proveedor de aviones", max_length=30
                    ),
                ),
                (
                    "contacto",
                    models.TextField(
                        help_text="Contacto del proveedor de aviones, puede ingresar el nombre del contacto telefono, email u otras redes sociales del mismo"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Fabricantes",
            },
        ),
        migrations.AlterModelOptions(
            name="aeropuerto",
            options={"verbose_name_plural": "Provincias"},
        ),
        migrations.AlterField(
            model_name="aeropuerto",
            name="codigo_iata",
            field=models.CharField(
                help_text="Código IATA del aeropuerto", max_length=3, unique=True
            ),
        ),
        migrations.AlterField(
            model_name="aeropuerto",
            name="nombre",
            field=models.CharField(help_text="Nombre del aeropuerto", max_length=30),
        ),
        migrations.AlterField(
            model_name="provincia",
            name="nombre",
            field=models.CharField(help_text="Nombre de la provincia", max_length=30),
        ),
        migrations.CreateModel(
            name="Modelo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        help_text="Nombre del modelo de avión", max_length=30
                    ),
                ),
                (
                    "fabricante",
                    models.ForeignKey(
                        help_text="Fabricante del modelo de avión",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nyandu.fabricante",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Modelos",
            },
        ),
        migrations.CreateModel(
            name="Avion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "matricula",
                    models.CharField(help_text="Matricula del avión", max_length=30),
                ),
                (
                    "capacidad",
                    models.PositiveSmallIntegerField(
                        help_text="Capacidad de pasajeros del avión"
                    ),
                ),
                (
                    "autonomia",
                    models.PositiveIntegerField(
                        help_text="Autonomía del avión volando en línea recta a velocidad crucero, se expresa en millas"
                    ),
                ),
                (
                    "modelo",
                    models.ForeignKey(
                        help_text="Fabricante del modelo de avión",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="nyandu.modelo",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Aviones",
            },
        ),
    ]
