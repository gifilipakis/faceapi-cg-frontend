# Generated by Django 2.2.2 on 2019-06-19 00:19

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190618_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_arquivo', models.CharField(blank=True, max_length=64, null=True, verbose_name='Nome do arquivo')),
                ('imagem', models.FileField(blank=True, null=True, upload_to=main.models.diretorio_arquivos, verbose_name='Arquivo')),
            ],
        ),
        migrations.DeleteModel(
            name='Imagem',
        ),
        migrations.AlterModelOptions(
            name='emocao',
            options={'verbose_name': 'Emoção', 'verbose_name_plural': 'Emoções'},
        ),
    ]