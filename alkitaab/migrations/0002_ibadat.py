# Generated by Django 4.2.11 on 2024-07-01 03:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alkitaab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ibadat',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alkitaab.customuser')),
            ],
        ),
    ]
