# Generated by Django 2.0.5 on 2018-05-05 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_auto_20180424_0324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='agama',
            field=models.CharField(choices=[('islam', 'ISLAM'), ('kristen', 'KRISTEN'), ('budha', 'BUDHA')], default='null', max_length=20),
        ),
    ]
