# Generated by Django 2.2.5 on 2019-11-23 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('1', 'Σε εκκρεμότητα'), ('2', 'Ολοκληρωμένη')], default='1', max_length=1),
        ),
    ]
