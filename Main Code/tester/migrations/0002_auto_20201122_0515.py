# Generated by Django 3.1.3 on 2020-11-22 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tester', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ansmcq10',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ansmcq25',
            name='id',
        ),
        migrations.RemoveField(
            model_name='ansqna10',
            name='id',
        ),
        migrations.AlterField(
            model_name='ansmcq10',
            name='test_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tester.mcq10testquestion'),
        ),
        migrations.AlterField(
            model_name='ansmcq25',
            name='test_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tester.mcq25testquestion'),
        ),
        migrations.AlterField(
            model_name='ansqna10',
            name='test_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='tester.questionandansweer10testquestion'),
        ),
    ]
