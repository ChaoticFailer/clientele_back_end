# Generated by Django 2.2.5 on 2019-11-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[(1, 'Σε εκκρεμότητα'), (2, 'Σε επισκευή'), (3, 'Ολοκληρωμένες')], default=1, max_length=1),
        ),
    ]