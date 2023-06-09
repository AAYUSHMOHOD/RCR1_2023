# Generated by Django 4.1.1 on 2023-06-09 12:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='chatGPTLifeLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=1000)),
                ('numUsed', models.IntegerField(default=0)),
                ('lastUsed', models.FloatField(default=1700000000.213593)),
                ('isDepleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='EasyQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('easyquestion_no', models.IntegerField()),
                ('easyquestion', models.CharField(max_length=1000)),
                ('easyanswer', models.IntegerField(default=-1)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_rank', models.IntegerField(default=0, null=True)),
                ('questionIndexList', models.TextField(default='[-1]')),
                ('correctanswers', models.IntegerField(default=0)),
                ('quesno', models.IntegerField(default=1)),
                ('mob_no', models.CharField(max_length=12)),
                ('isFirstTry', models.BooleanField(default=True)),
                ('isTimeOut', models.BooleanField(default=False)),
                ('startTime', models.DateTimeField(null=True)),
                ('tempTime', models.DateTimeField(null=True)),
                ('logoutTime', models.DateTimeField(null=True)),
                ('newlogin', models.BooleanField(default=False)),
                ('category', models.BooleanField(default=True)),
                ('remainingTime', models.IntegerField(default=1800)),
                ('plusmrks', models.IntegerField(default=4)),
                ('minusmrks', models.IntegerField(default=0)),
                ('display_name', models.CharField(default='', max_length=1000, null=True)),
                ('marks', models.IntegerField(default=0)),
                ('accuracy', models.FloatField(default=0)),
                ('cache', models.IntegerField(default=0)),
                ('cacheAnswer', models.IntegerField(default=-1)),
                ('lifeline1_count', models.IntegerField(default=0)),
                ('lifeline1_status', models.BooleanField(default=False)),
                ('lifeline1_using', models.BooleanField(default=False)),
                ('lifeline1_question_id', models.IntegerField(default=0)),
                ('simpleQuestionUsed', models.BooleanField(default=False)),
                ('lifeline2_superstatus', models.BooleanField(default=True)),
                ('lifeline2_timeout', models.BooleanField(default=False)),
                ('lifeline2_status', models.BooleanField(default=False)),
                ('lifeline2_checked', models.BooleanField(default=False)),
                ('lifeline2_secondattempt', models.BooleanField(default=False)),
                ('lifeline3_status', models.BooleanField(default=False)),
                ('lifeline3_used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_no', models.IntegerField()),
                ('question', models.CharField(max_length=1000)),
                ('answer', models.IntegerField(default=-1)),
                ('is_junior', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quetionID', models.IntegerField(default=-1)),
                ('response1', models.CharField(max_length=1000, null=True)),
                ('response2', models.CharField(max_length=1000, null=True)),
                ('isSimpleQuestion', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp_RC.profile')),
            ],
        ),
    ]