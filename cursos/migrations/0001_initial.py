# Generated by Django 3.2.6 on 2021-08-12 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assunto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('desc_geral', models.TextField()),
                ('criado', models.DateTimeField(auto_now_add=True)),
                ('assunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cursos', to='cursos.assunto')),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criador_curso', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-criado'],
            },
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descricao', models.TextField(blank=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modulos', to='cursos.curso')),
            ],
        ),
    ]
