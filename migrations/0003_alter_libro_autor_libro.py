# Generated by Django 3.2.5 on 2022-08-12 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0002_libro_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='autor_libro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.autor'),
        ),
    ]