# Generated by Django 5.0.1 on 2024-02-06 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('controlador', models.CharField(max_length=12)),
                ('llave', models.CharField(max_length=12)),
                ('delete_at', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
