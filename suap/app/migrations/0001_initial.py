# Generated by Django 4.2.5 on 2023-09-18 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('carga_horaria_total', models.TimeField()),
                ('duracao_meses', models.IntegerField()),
                ('area_saber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.area')),
            ],
        ),
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('area_saber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.area')),
            ],
        ),
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('site', models.CharField(max_length=50)),
                ('telefone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ocupacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoAvaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('periodo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('pai', models.CharField(max_length=50)),
                ('mae', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=14)),
                ('data_nasc', models.DateField()),
                ('email', models.CharField(max_length=50)),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cidade')),
            ],
        ),
        migrations.CreateModel(
            name='Ocorrencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('data', models.DateTimeField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateField()),
                ('data_previsao_terminio', models.DateField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('instituicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicao')),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Frequencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_faltas', models.IntegerField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinaCursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('carga_horaria', models.TimeField()),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.periodo')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='instituicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.instituicao'),
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.curso')),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.disciplina')),
                ('tipo_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipoavaliacao')),
            ],
        ),
    ]