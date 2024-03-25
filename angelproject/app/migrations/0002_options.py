# Generated by Django 5.0.3 on 2024-03-15 09:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ce', models.TextField()),
                ('pe', models.TextField()),
                ('company_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.company_name')),
            ],
        ),
    ]