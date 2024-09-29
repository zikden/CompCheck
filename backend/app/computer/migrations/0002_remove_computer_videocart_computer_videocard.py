# Generated by Django 4.2.9 on 2024-09-29 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0004_alter_components_processor_options_and_more'),
        ('computer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='computer',
            name='videocart',
        ),
        migrations.AddField(
            model_name='computer',
            name='videocard',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='components.components_videocard', verbose_name='videocard'),
            preserve_default=False,
        ),
    ]
