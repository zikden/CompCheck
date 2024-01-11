# Generated by Django 4.2.9 on 2024-01-11 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memory_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Memory_type',
                'verbose_name_plural': 'Memory_types',
            },
        ),
        migrations.CreateModel(
            name='ProccesorBrend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Brend',
                'verbose_name_plural': 'Brends',
            },
        ),
        migrations.CreateModel(
            name='ProccesorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'ProccesorModel',
                'verbose_name_plural': 'ProccesorModels',
            },
        ),
        migrations.CreateModel(
            name='Soket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Soket',
                'verbose_name_plural': 'Sokets',
            },
        ),
        migrations.CreateModel(
            name='VideocardBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'VideocardBrand',
                'verbose_name_plural': 'VideocardBrands',
            },
        ),
        migrations.CreateModel(
            name='VideoChipset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'VideoChipset',
                'verbose_name_plural': 'VideoChipsets',
            },
        ),
        migrations.CreateModel(
            name='VideoCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gram', models.IntegerField()),
                ('tdp', models.IntegerField()),
                ('raiting', models.PositiveIntegerField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.videocardbrand')),
                ('videochipset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.videochipset')),
            ],
            options={
                'verbose_name': 'VideoCard',
                'verbose_name_plural': 'VideoCards',
            },
        ),
        migrations.CreateModel(
            name='Proccesor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mfs', models.IntegerField()),
                ('tdp', models.IntegerField()),
                ('raiting', models.PositiveIntegerField()),
                ('brend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.proccesorbrend')),
                ('memory_type', models.ManyToManyField(to='archive.memory_type')),
                ('proccesor_models', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.proccesormodel')),
                ('soket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.soket')),
            ],
            options={
                'verbose_name': 'Proccesor',
                'verbose_name_plural': 'Proccesors',
            },
        ),
    ]
