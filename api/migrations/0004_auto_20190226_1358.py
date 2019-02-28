# Generated by Django 2.1.5 on 2019-02-26 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_evaluationtest_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='api.Choice'),
        ),
        migrations.AlterField(
            model_name='question',
            name='evaluationtest',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='api.EvaluationTest'),
        ),
    ]
