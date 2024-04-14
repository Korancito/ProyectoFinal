# Generated by Django 5.0.3 on 2024-04-12 21:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razonsocial', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=60)),
                ('rut', models.IntegerField()),
                ('giro', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('contacto', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField(null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_costo', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Tienda.categoria')),
            ],
        ),
    ]