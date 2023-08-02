# Generated by Django 4.2.2 on 2023-08-02 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=100)),
                ('asunto', models.CharField(default='', max_length=150)),
                ('email', models.EmailField(max_length=50)),
                ('comentarios', models.TextField(max_length=400)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
    ]
