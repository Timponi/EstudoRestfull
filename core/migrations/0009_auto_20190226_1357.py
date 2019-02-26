# Generated by Django 2.1.7 on 2019-02-26 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_pontoturistico_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocIdentificacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='pontoturistico',
            name='doc_identificacao',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.DocIdentificacao'),
        ),
    ]
