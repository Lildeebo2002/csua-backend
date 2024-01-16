# Generated by Django 2.2.28 on 2023-02-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("discordbot", "0005_auto_20210520_2001")]

    operations = [
        migrations.CreateModel(
            name="AniShuffleGame",
            fields=[
                (
                    "message_id",
                    models.BigIntegerField(primary_key=True, serialize=False),
                ),
                ("player_id", models.BigIntegerField()),
                ("state", models.CharField(max_length=16)),
                ("moves", models.IntegerField(default=0)),
                ("start_time", models.DateTimeField(auto_now_add=True)),
                ("shuffle_depth", models.IntegerField(null=True)),
            ],
        )
    ]