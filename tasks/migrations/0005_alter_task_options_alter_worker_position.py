# Generated by Django 4.1.6 on 2023-02-22 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("tasks", "0004_alter_task_is_completed_alter_task_priority"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task",
            options={"ordering": ["deadline", "priority"]},
        ),
        migrations.AlterField(
            model_name="worker",
            name="position",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="worker_position",
                to="tasks.position",
            ),
        ),
    ]
