# Generated by Django 3.2.6 on 2021-08-25 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
                ('keyword', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'content',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'keyword',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KeywordMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'keyword_movie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KeywordMusic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'keyword_music',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KeywordUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'keyword_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='KeywordYoutube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'keyword_youtube',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(blank=True, max_length=150, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=150, null=True)),
                ('scrap', models.IntegerField(blank=True, null=True)),
                ('good', models.IntegerField(blank=True, null=True)),
                ('actor', models.CharField(blank=True, max_length=100, null=True)),
                ('rating', models.CharField(blank=True, max_length=5, null=True)),
                ('director', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'movie',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MovieRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popular', models.IntegerField()),
            ],
            options={
                'db_table': 'movie_rank',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MovieRealtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recent', models.IntegerField()),
            ],
            options={
                'db_table': 'movie_realtime',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MovieScrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'movie_scrap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('url', models.CharField(blank=True, max_length=150, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=150, null=True)),
                ('scrap', models.IntegerField(blank=True, null=True)),
                ('good', models.IntegerField(blank=True, null=True)),
                ('y_id', models.CharField(blank=True, max_length=50, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'music',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MusicRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popular', models.IntegerField()),
            ],
            options={
                'db_table': 'music_rank',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MusicRealtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recent', models.IntegerField()),
            ],
            options={
                'db_table': 'music_realtime',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MusicScrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'music_scrap',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Youtube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('y_id', models.CharField(blank=True, max_length=50, null=True)),
                ('url', models.CharField(blank=True, max_length=150, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('thumbnail', models.CharField(blank=True, max_length=150, null=True)),
                ('scrap', models.IntegerField(blank=True, null=True)),
                ('good', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'youtube',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='YoutubeRank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('popular', models.IntegerField()),
            ],
            options={
                'db_table': 'youtube_rank',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='YoutubeRealtime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recent', models.IntegerField()),
            ],
            options={
                'db_table': 'youtube_realtime',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='YoutubeScrap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'youtube_scrap',
                'managed': False,
            },
        ),
    ]
