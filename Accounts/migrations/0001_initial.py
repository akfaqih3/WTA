# Generated by Django 5.0.6 on 2024-06-20 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('phone', models.CharField(max_length=16)),
                ('address', models.CharField(max_length=16)),
                ('note', models.CharField(blank=True, max_length=64, null=True)),
                ('type', models.CharField(choices=[('customer', 'customer'), ('supplier', 'supplier')], max_length=16)),
            ],
        ),
    ]
