# Generated by Django 4.2.2 on 2023-08-03 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_subtitulo_alter_post_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=80),
        ),
    ]
