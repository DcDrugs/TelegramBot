# Generated by Django 3.2.4 on 2021-06-03 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profiler',
            options={'verbose_name': 'Profile'},
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Time create')),
                ('profiler', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ugc.profiler', verbose_name='Profile')),
            ],
            options={
                'verbose_name': 'Message',
            },
        ),
    ]
