# Generated by Django 2.2.12 on 2020-10-30 09:59

from django.db import migrations, models
import django.db.models.deletion
import otree.db.idmap
import otree.db.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='online_coalition_game_alternative_offer_introduction_group', to='otree.Session')),
            ],
            options={
                'db_table': 'Online_Coalition_Game_Alternative_Offer_Introduction_group',
            },
            bases=(models.Model, otree.db.idmap.GroupIDMapMixin),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('resources_AB', otree.db.models.IntegerField(null=True)),
                ('resources_AC', otree.db.models.IntegerField(null=True)),
                ('resources_BC', otree.db.models.IntegerField(null=True)),
                ('resources_ABC', otree.db.models.IntegerField(null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='online_coalition_game_alternative_offer_introduction_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'Online_Coalition_Game_Alternative_Offer_Introduction_subsession',
            },
            bases=(models.Model, otree.db.idmap.SubsessionIDMapMixin),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_role', otree.db.models.StringField(max_length=10000, null=True)),
                ('consent', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], null=True)),
                ('tscore', otree.db.models.IntegerField(null=True)),
                ('score', otree.db.models.IntegerField(null=True)),
                ('position', otree.db.models.StringField(max_length=10000, null=True)),
                ('resources', otree.db.models.IntegerField(null=True)),
                ('practice', otree.db.models.IntegerField(null=True)),
                ('tslider1', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider2', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider3', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider4', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider5', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider6', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider7', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider8', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider9', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider10', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider11', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider12', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider13', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider14', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider15', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider16', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider17', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider18', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider19', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider20', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('tslider21', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider1', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider2', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider3', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider4', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider5', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider6', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider7', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider8', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider9', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider10', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider11', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider12', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider13', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider14', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider15', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider16', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider17', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider18', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider19', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider20', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('slider21', otree.db.models.IntegerField(default=0, null=True, verbose_name=False)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Online_Coalition_Game_Alternative_Offer_Introduction.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='online_coalition_game_alternative_offer_introduction_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='online_coalition_game_alternative_offer_introduction_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Online_Coalition_Game_Alternative_Offer_Introduction.Subsession')),
            ],
            options={
                'db_table': 'Online_Coalition_Game_Alternative_Offer_Introduction_player',
            },
            bases=(models.Model, otree.db.idmap.PlayerIDMapMixin),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Online_Coalition_Game_Alternative_Offer_Introduction.Subsession'),
        ),
    ]
