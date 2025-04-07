# Generated by Django 5.2 on 2025-04-07 22:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amb_nome', models.CharField(max_length=100)),
                ('amb_descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_criado', models.DateField()),
                ('emp_efetivado', models.DateField()),
                ('emp_prazo', models.IntegerField()),
                ('emp_devolvido', models.DateField(blank=True, null=True)),
                ('emp_status', models.IntegerField(choices=[(1, 'Pendente'), (2, 'Efetivado'), (3, 'Devolvido'), (4, 'Cancelado')])),
                ('emp_anotacao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_logradouro', models.CharField(max_length=255)),
                ('end_numero', models.IntegerField()),
                ('end_complemento', models.CharField(blank=True, max_length=255, null=True)),
                ('end_bairro', models.CharField(max_length=100)),
                ('end_cidade', models.CharField(max_length=100)),
                ('end_estado', models.CharField(max_length=100)),
                ('end_pais', models.CharField(max_length=100)),
                ('end_cep', models.CharField(max_length=10)),
                ('end_uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Etiquetagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eti_descricao', models.CharField(max_length=255)),
                ('eti_data_criacao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_descricao', models.CharField(max_length=255)),
                ('inv_data_criacao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Patrimonio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pat_codigo', models.CharField(max_length=20, unique=True)),
                ('pat_nome', models.CharField(max_length=100)),
                ('pat_marca', models.CharField(max_length=100)),
                ('pat_modelo', models.CharField(max_length=100)),
                ('pat_nse', models.CharField(max_length=50, unique=True)),
                ('pat_data_registrado', models.DateField()),
                ('pat_data_aquisicao', models.DateField()),
                ('pat_valor', models.FloatField()),
                ('pat_descricao', models.TextField(blank=True, null=True)),
                ('pat_categoria', models.CharField(max_length=100)),
                ('pat_status', models.CharField(choices=[('ativo', 'Ativo'), ('manutencao', 'Em Manutenção'), ('baixado', 'Baixado')], default='ativo', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pf_nome', models.CharField(max_length=255)),
                ('pf_nascimento', models.DateField()),
                ('pf_cpf', models.CharField(max_length=14, unique=True)),
                ('pf_genero', models.IntegerField(choices=[(1, 'Masculino'), (2, 'Feminino'), (3, 'Outro')])),
            ],
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pj_razao_social', models.CharField(max_length=255)),
                ('pj_nome_fantasia', models.CharField(max_length=255)),
                ('pj_cnpj', models.CharField(max_length=18, unique=True)),
                ('pj_representante', models.CharField(max_length=255)),
                ('pj_data_constituicao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='InventarioPatrimonio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_status', models.IntegerField(choices=[(1, 'Em Estoque'), (2, 'Em Uso'), (3, 'Danificado'), (4, 'Descartado')])),
                ('ip_descricao', models.CharField(max_length=255)),
                ('ip_inv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.inventario')),
                ('ip_pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.patrimonio')),
            ],
        ),
        migrations.CreateModel(
            name='EtiquetagemPatrimonio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ep_eti', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.etiquetagem')),
                ('ep_pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.patrimonio')),
            ],
        ),
        migrations.CreateModel(
            name='AmbientePatrimonio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ap_data_entrada', models.DateField()),
                ('ap_data_saida', models.DateField(blank=True, null=True)),
                ('ap_amb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.ambiente')),
                ('ap_pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.patrimonio')),
            ],
        ),
        migrations.CreateModel(
            name='PatrimonioEmprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pe_emp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.emprestimo')),
                ('pe_pat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.patrimonio')),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pes_tipo', models.IntegerField(choices=[(1, 'Física'), (2, 'Jurídica')])),
                ('pes_telefone', models.CharField(max_length=20)),
                ('pes_email', models.EmailField(max_length=254)),
                ('pes_data_cadastro', models.DateField()),
                ('pes_end', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patrimonio.endereco')),
                ('pes_pf', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patrimonio.pessoafisica')),
                ('pes_pj', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='patrimonio.pessoajuridica')),
            ],
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='emp_pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.pessoa'),
        ),
        migrations.CreateModel(
            name='PessoaAmbiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pa_data_entrada', models.DateField()),
                ('pa_data_saida', models.DateField(blank=True, null=True)),
                ('pa_ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.ambiente')),
                ('pa_pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patrimonio.pessoa')),
            ],
        ),
    ]
