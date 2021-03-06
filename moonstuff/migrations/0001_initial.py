# Generated by Django 3.1.2 on 2021-04-18 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('eveonline', '0014_auto_20210105_1413'),
        ('eveuniverse', '0004_effect_longer_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moonstuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('access_moonstuff', 'Allows access to the moonstuff module'), ('access_moon_list', 'Allows access to list of all moons.')),
                'managed': False,
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MaterialCheckSum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checksum', models.CharField(default=None, max_length=255, null=True)),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TrackingCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latest_notification_id', models.BigIntegerField(default=0, null=True)),
                ('last_notification_check', models.DateTimeField(null=True)),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eveonline.evecharacter')),
            ],
            options={
                'default_permissions': ('add',),
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=10, max_digits=11)),
                ('moon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='eveuniverse.evemoon')),
                ('ore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eveuniverse.evetype')),
            ],
            options={
                'default_permissions': ('add',),
            },
        ),
        migrations.CreateModel(
            name='Refinery',
            fields=[
                ('structure_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, null=True)),
                ('observer', models.BooleanField(default=True)),
                ('corp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='refineries', to='eveonline.evecorporationinfo')),
                ('evetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eveuniverse.evetype')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('evetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='eveuniverse.evetype')),
                ('material_evetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_types', to='eveuniverse.evetype')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='LedgerEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character_id', models.IntegerField()),
                ('last_updated', models.DateField()),
                ('quantity', models.BigIntegerField()),
                ('recorded_corporation_id', models.IntegerField()),
                ('evetype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ledger_entries', to='eveuniverse.evetype')),
                ('observer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='moonstuff.refinery')),
            ],
            options={
                'default_permissions': (),
                'unique_together': {('observer', 'last_updated', 'character_id', 'evetype')},
            },
        ),
        migrations.CreateModel(
            name='Extraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('decay_time', models.DateTimeField()),
                ('cancelled', models.BooleanField(default=False)),
                ('jackpot', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=False)),
                ('depleted', models.BooleanField(default=False)),
                ('total_volume', models.BigIntegerField(null=True)),
                ('corp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extractions', to='eveonline.evecorporationinfo')),
                ('moon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extractions', to='eveuniverse.evemoon')),
                ('refinery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='extractions', to='moonstuff.refinery')),
            ],
            options={
                'default_permissions': (),
                'unique_together': {('start_time', 'moon')},
            },
        ),
    ]
