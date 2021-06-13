# Generated by Django 3.2.4 on 2021-06-06 11:50

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0007_alter_item_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.AddField(
            model_name='item',
            name='unique_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]