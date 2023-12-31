# Generated by Django 4.2.5 on 2023-09-19 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_user_custom_active_remove_user_voted_polls'),
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_like',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='parent_comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user_info',
        ),
        migrations.RemoveField(
            model_name='nonuservote',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='nonuservote',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='poll',
            name='poll_like',
        ),
        migrations.RemoveField(
            model_name='poll_result',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='uservote',
            name='choice',
        ),
        migrations.RemoveField(
            model_name='uservote',
            name='poll',
        ),
        migrations.RemoveField(
            model_name='uservote',
            name='user',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='NonUserVote',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
        migrations.DeleteModel(
            name='Poll_Result',
        ),
        migrations.DeleteModel(
            name='UserVote',
        ),
    ]
