# Generated by Django 3.2.6 on 2021-08-19 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segmentation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ct',
            name='consolidation',
            field=models.IntegerField(default=0, null=True, verbose_name='Consolidation '),
        ),
        migrations.AddField(
            model_name='ct',
            name='ground_glass',
            field=models.IntegerField(default=0, null=True, verbose_name='Ground glass'),
        ),
        migrations.AlterField(
            model_name='ct',
            name='segmented_image',
            field=models.ImageField(null=True, upload_to='segments/%Y/', verbose_name='Сегментированное изображение'),
        ),
    ]
