# Generated by Django 5.0.6 on 2024-06-10 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FacultyRankEvaluations',
            fields=[
                ('rank_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('current_rank', models.CharField(blank=True, max_length=50, null=True)),
                ('kra_one_pts', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('kra_two_pts', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('kra_three_pts', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('kra_four_pts', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('grandtotal_score', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=5, null=True)),
                ('rank_bracket_count', models.IntegerField(blank=True, default=0, null=True)),
                ('new_rank', models.CharField(blank=True, max_length=50, null=True)),
                ('impression', models.CharField(blank=True, max_length=50, null=True)),
                ('auto_rank', models.BooleanField(default=False)),
                ('rank_eval_date', models.DateTimeField()),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ranking', to='accounts.faculty')),
            ],
        ),
    ]
