# Generated by Django 5.1.5 on 2025-01-27 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='voucher_no',
            field=models.CharField(default='77331289416861', max_length=14, unique=True, verbose_name='Voucher No'),
        ),
    ]
