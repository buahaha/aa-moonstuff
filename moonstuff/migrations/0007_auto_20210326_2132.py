# Generated by Django 3.1.2 on 2021-03-26 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eveuniverse', '0004_effect_longer_name'),
        ('moonstuff', '0006_auto_20210311_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledgerentry',
            name='evetype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ledger_entries', to='eveuniverse.evetype'),
        ),
    ]
