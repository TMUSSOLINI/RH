# Generated by Django 4.1.3 on 2022-12-13 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funcionarios', '0004_alter_funcionario_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='imagem',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
