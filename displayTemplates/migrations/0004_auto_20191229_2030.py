# Generated by Django 3.0.1 on 2019-12-29 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('displayTemplates', '0003_auto_20191229_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='img',
            field=models.ImageField(upload_to='displayTemplates/template_icons'),
        ),
    ]