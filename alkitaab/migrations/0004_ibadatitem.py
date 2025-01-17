# Generated by Django 4.2.11 on 2024-07-01 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('alkitaab', '0003_alter_ibadat_name_scale'),
    ]

    operations = [
        migrations.CreateModel(
            name='IbadatItem',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('point', models.IntegerField(null=True)),
                ('score', models.IntegerField(null=True)),
                ('date', models.DateField(null=True)),
                ('ibadat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alkitaab.ibadat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alkitaab.customuser')),
            ],
        ),
    ]
