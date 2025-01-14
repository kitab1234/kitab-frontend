# Generated by Django 4.2.11 on 2024-07-01 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alkitaab', '0002_ibadat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ibadat',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=7)),
                ('ibadat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alkitaab.ibadat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alkitaab.customuser')),
            ],
        ),
    ]
