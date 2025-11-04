###############################################################################################################################################################################
#1 - Generates DB with data that was used to screen whetehr participants met the inclusion/exclusion criteria to participate in the study.
##Imports libraries
import pandas as pd
import os

#Opens the excel file where data from participants are stored.
excel_part_data_path = os.getcwd() + "\Screening_Data\data.xlsx"
df_excel_data_part = pd.read_excel(excel_part_data_path)
##Drops redundant columns (empty columns regarding Q1,Q7,Q14,Q15) in the dataframe df_excel_data_part.
df_excel_data_part.drop(df_excel_data_part.columns[[33, *range(104,108)]], axis=1, inplace=True)

##Change names of columns and sort participants by date (first to complete to last to complete the questionnaires).
##'HorariosMatematicaHistoria',
df_excel_data_part.columns = ['participant', 'Idade', 'Sexo', 'Nacionalidade', 'FreqEnsSup', 'CicloEstudosEnsSup_1', 'CicloEstudosEnsSup_2', 'CicloEstudosEnsSup_3', 'CicloEstudosEnsSup_4','HabAcademicas_1','HabAcademicas_2','HabAcademicas_3','HabAcademicas_4','HabAcademicas_5','HabAcademicas_6', 'Curso', 'SituacaoLaboral', 'SituacaoLaboralTurnos_1','SituacaoLaboralTurnos_2','PresencaDoencasAnter', 'ListaDoencasAnter', 'MedicacaoPsicotropica', 'ListaMedicacaoPsicotropica', 'Fumador', 'NrCigarros', 'ProdutosSessaoTabagica_1', 'ProdutosSessaoTabagica_2', 'ConsomeCafeina', 'QuantidadeDiaCafeina', 'ConsomeAlcool', 'QuantidadeDiaAlcool', 'ConsomeDrogas', 'Viagens', 'Pergunta1', 'Pergunta2', 'Pergunta3', 'Pergunta4', 'Pergunta5', 'Pergunta6', 'Pergunta7', 'Pergunta8', 'Pergunta9', 'Pergunta10', 'Pergunta11', 'Pergunta12', 'Pergunta13', 'Pergunta14', 'Pergunta15', 'Pergunta16', 'MEQscore', 'BSI:1', 'BSI:2', 'BSI:3', 'BSI:4', 'BSI:5', 'BSI:6', 'BSI:7', 'BSI:8', 'BSI:9', 'BSI:10', 'BSI:11', 'BSI:12', 'BSI:13', 'BSI:14', 'BSI:15', 'BSI:16', 'BSI:17', 'BSI:18', 'BSI:19', 'BSI:20' , 'BSI:21', 'BSI:22', 'BSI:23', 'BSI:24', 'BSI:25', 'BSI:26', 'BSI:27', 'BSI:28', 'BSI:29', 'BSI:30', 'BSI:31', 'BSI:32', 'BSI:33', 'BSI:34', 'BSI:35', 'BSI:36', 'BSI:37', 'BSI:38', 'BSI:39' , 'BSI:40', 'BSI:41', 'BSI:42', 'BSI:43', 'BSI:44', 'BSI:45', 'BSI:46', 'BSI:47', 'BSI:48', 'BSI:49', 'BSI:50', 'BSI:51', 'BSI:52', 'BSI:53', 'TIME_start', 'TIME_end', 'TIME_total']
df_excel_data_part.sort_values(by=['TIME_end'], kind='mergesort', inplace=True,ascending=True)
df_excel_data_part.reset_index(drop=True,inplace=True)

##Creates a list with strngs that merge the path of the location of Q1,Q7,Q14,Q15 and the names of the files containing information
##regarding Q1,Q7,Q14,Q15.
path_questions_MEQ = os.getcwd() + "\Screening_Data\experiment_data"
list_of_files_questions_MEQ = os.listdir(path_questions_MEQ)
path_list_of_files_questions_MEQ = []
for i in range(0,len(list_of_files_questions_MEQ)):
    create_str_file = 'Screening_Data/experiment_data/' + list_of_files_questions_MEQ[i]
    path_list_of_files_questions_MEQ.append(create_str_file)

##Opens the files with information about the questions 1,7,14, and 15 of the MEQ.
list_values_QMEQ = []
for i in range(0,len(path_list_of_files_questions_MEQ)):
    temp_hold = pd.read_csv(path_list_of_files_questions_MEQ[i],sep=' ',header=None)
    ##Cleans the files with information about the questions 1,7,14, and 15 of the MEQ. Drops everythng except the answer to each question.
    temp_hold = int(temp_hold.iloc[0,0])
    list_values_QMEQ.append(temp_hold)

##Fills the columns of the dataframe df_excel_data_part regarding the questions 1,7,14, and 15 of the MEQ  with  their answears to the
##questions 1,7,14, and 15 of the MEQ.
for i in range(0,len(df_excel_data_part['Pergunta1'])):
    for j in range(0,len(list_of_files_questions_MEQ)):
        if df_excel_data_part.loc[i,'Pergunta1'] == list_of_files_questions_MEQ[j]:
            df_excel_data_part.loc[i, 'Pergunta1'] = list_values_QMEQ[j]

for i in range(0,len(df_excel_data_part['Pergunta7'])):
    for j in range(0,len(list_of_files_questions_MEQ)):
        if df_excel_data_part.loc[i,'Pergunta7'] == list_of_files_questions_MEQ[j]:
            df_excel_data_part.loc[i, 'Pergunta7'] = list_values_QMEQ[j]

for i in range(0,len(df_excel_data_part['Pergunta14'])):
    for j in range(0,len(list_of_files_questions_MEQ)):
        if df_excel_data_part.loc[i,'Pergunta14'] == list_of_files_questions_MEQ[j]:
            df_excel_data_part.loc[i, 'Pergunta14'] = list_values_QMEQ[j]

for i in range(0,len(df_excel_data_part['Pergunta15'])):
    for j in range(0,len(list_of_files_questions_MEQ)):
        if df_excel_data_part.loc[i,'Pergunta15'] == list_of_files_questions_MEQ[j]:
            df_excel_data_part.loc[i, 'Pergunta15'] = list_values_QMEQ[j]

##Replaces the integer that codes the informations in the dataframe with data from the participants with the correct label.
for i in range(0,len(df_excel_data_part['Sexo'])):
        if df_excel_data_part.loc[i,'Sexo'] == 1:
            df_excel_data_part.loc[i,'Sexo'] = "Masculino"
        elif df_excel_data_part.loc[i,'Sexo'] == 2:
            df_excel_data_part.loc[i,'Sexo'] = "Feminino"
        else:
            df_excel_data_part.loc[i,'Sexo'] = "Outro"

for i in range(0,len(df_excel_data_part['Nacionalidade'])):
        if df_excel_data_part.loc[i,'Nacionalidade'] == 1:
            df_excel_data_part.loc[i,'Nacionalidade'] = "PT"
        else:
            df_excel_data_part.loc[i,'Nacionalidade'] = "Outra"

for i in range(0,len(df_excel_data_part['FreqEnsSup'])):
        if df_excel_data_part.loc[i,'FreqEnsSup'] == 1:
            df_excel_data_part.loc[i,'FreqEnsSup'] = "Sim"
        else :
            df_excel_data_part.loc[i,'FreqEnsSup'] = "Não"

CicloEstudosEnsSup = []
for i in range(0,len(df_excel_data_part['participant'])):
        indexx = 0
        if df_excel_data_part.loc[i,'CicloEstudosEnsSup_1'] == 1:
            aaa = "Licenciatura"
            CicloEstudosEnsSup.append(aaa)
            indexx += 1
        elif df_excel_data_part.loc[i,'CicloEstudosEnsSup_2'] == 1:
            aaa = "Mestrado"
            CicloEstudosEnsSup.append(aaa)
            indexx += 1
        elif df_excel_data_part.loc[i,'CicloEstudosEnsSup_3'] == 1:
            aaa = "Doutoramento"
            CicloEstudosEnsSup.append(aaa)
            indexx += 1
        elif df_excel_data_part.loc[i,'CicloEstudosEnsSup_4'] == 1:
            aaa = "Outro Ciclo"
            CicloEstudosEnsSup.append(aaa)
            indexx +=1
        elif indexx == 0:
            aaa = ""
            CicloEstudosEnsSup.append(aaa)


df_excel_data_part.drop(columns=['CicloEstudosEnsSup_1','CicloEstudosEnsSup_2','CicloEstudosEnsSup_3','CicloEstudosEnsSup_4'],inplace=True)
df_excel_data_part['CicloEstudosEnsSup'] = CicloEstudosEnsSup
TransCol = df_excel_data_part.pop('CicloEstudosEnsSup')
df_excel_data_part.insert(5,"CicloEstudosEnsSup",TransCol)

HabAcademicas = []
for i in range(0,len(df_excel_data_part['participant'])):
        if df_excel_data_part.loc[i,"FreqEnsSup"] == "Não" and df_excel_data_part.loc[i,'HabAcademicas_1'] == 1:
            aaa = "Ensino Obrigatório"
            HabAcademicas.append(aaa)
        elif df_excel_data_part.loc[i, "FreqEnsSup"] == "Não" and df_excel_data_part.loc[i,'HabAcademicas_2'] == 1:
            aaa = "Licenciatura"
            HabAcademicas.append(aaa)
        elif df_excel_data_part.loc[i, "FreqEnsSup"] == "Não" and df_excel_data_part.loc[i,'HabAcademicas_3'] == 1:
            aaa = "Pós-graduação"
            HabAcademicas.append(aaa)
        elif df_excel_data_part.loc[i, "FreqEnsSup"] == "Não" and df_excel_data_part.loc[i,'HabAcademicas_4'] == 1:
            aaa = "Mestrado"
            HabAcademicas.append(aaa)
        elif df_excel_data_part.loc[i, "FreqEnsSup"] == "Não" and df_excel_data_part.loc[i,'HabAcademicas_5'] == 1:
            aaa = "Doutoramento"
            HabAcademicas.append(aaa)
        elif df_excel_data_part.loc[i, "FreqEnsSup"] == "Não" and df_excel_data_part.loc[i,'HabAcademicas_6'] == 1:
            aaa = "Nenhuma das opções anteriores se aplica"
            HabAcademicas.append(aaa)
        elif df_excel_data_part.loc[i, "FreqEnsSup"] == "Sim" and df_excel_data_part.loc[i,'CicloEstudosEnsSup'] == "Licenciatura":
            aaa = "Ensino Obrigatório"
            HabAcademicas.append(aaa)
        elif df_excel_data_part.loc[i, "FreqEnsSup"] == "Sim" and df_excel_data_part.loc[i,'CicloEstudosEnsSup'] == "Mestrado":
            aaa = "Licenciatura"
            HabAcademicas.append(aaa)
        elif df_excel_data_part.loc[i, "FreqEnsSup"] == "Sim" and df_excel_data_part.loc[i,'CicloEstudosEnsSup'] == "Doutoramento":
            aaa = "Mestrado"
            HabAcademicas.append(aaa)
        elif df_excel_data_part.loc[i, "FreqEnsSup"] == "Sim" and df_excel_data_part.loc[i,'CicloEstudosEnsSup'] == "Outro Ciclo":
            aaa = "Outro Ciclo"
            HabAcademicas.append(aaa)

df_excel_data_part.drop(columns=['HabAcademicas_1','HabAcademicas_2','HabAcademicas_3','HabAcademicas_4','HabAcademicas_5','HabAcademicas_6'],inplace=True)
df_excel_data_part['HabAcademicas'] = HabAcademicas
TransCol = df_excel_data_part.pop('HabAcademicas')
df_excel_data_part.insert(6,"HabAcademicas",TransCol)


for i in range(0,len(df_excel_data_part['SituacaoLaboral'])):
        if df_excel_data_part.loc[i,'SituacaoLaboral'] == 1:
            df_excel_data_part.loc[i,'SituacaoLaboral'] = "Sim"
        else:
            df_excel_data_part.loc[i,'SituacaoLaboral'] = "Não"

SituacaoLaboralTurnos = []
for i in range(0,len(df_excel_data_part['participant'])):
        if df_excel_data_part.loc[i,'SituacaoLaboralTurnos_1'] == 1:
            aaa = "Sim"
            SituacaoLaboralTurnos.append(aaa)
        elif df_excel_data_part.loc[i, 'SituacaoLaboralTurnos_1'] == 0:
            aaa = "Não"
            SituacaoLaboralTurnos.append(aaa)
        elif df_excel_data_part.loc[i,'SituacaoLaboralTurnos_2'] == 1 or df_excel_data_part.loc[i,'SituacaoLaboralTurnos_2'] == 0:
            aaa = "Não"
            SituacaoLaboralTurnos.append(aaa)

df_excel_data_part.drop(columns=['SituacaoLaboralTurnos_1','SituacaoLaboralTurnos_2'],inplace=True)
df_excel_data_part['SituacaoLaboralTurnos'] = SituacaoLaboralTurnos
TransCol = df_excel_data_part.pop('SituacaoLaboralTurnos')
df_excel_data_part.insert(9,"SituacaoLaboralTurnos",TransCol)

for i in range(0,len(df_excel_data_part['PresencaDoencasAnter'])):
        if df_excel_data_part.loc[i,'PresencaDoencasAnter'] == 1:
            df_excel_data_part.loc[i,'PresencaDoencasAnter'] = "Sim"
        else:
            df_excel_data_part.loc[i,'PresencaDoencasAnter'] = "Não"

for i in range(0,len(df_excel_data_part['MedicacaoPsicotropica'])):
        if df_excel_data_part.loc[i,'MedicacaoPsicotropica'] == 1:
            df_excel_data_part.loc[i,'MedicacaoPsicotropica'] = "Sim"
        else:
            df_excel_data_part.loc[i,'MedicacaoPsicotropica'] = "Não"

for i in range(0,len(df_excel_data_part['Fumador'])):
        if df_excel_data_part.loc[i,'Fumador'] == 1:
            df_excel_data_part.loc[i,'Fumador'] = "Sou fumador"
        elif df_excel_data_part.loc[i,'Fumador'] == 2:
            df_excel_data_part.loc[i,'Fumador'] = "Deixei de fumar há menos de 3 meses"
        else:
            df_excel_data_part.loc[i,'Fumador'] = "Não sou fumador nem deixei de fumar há menos de 3 meses"

ProdutosSessaoTabagica = []
for i in range(0,len(df_excel_data_part['participant'])):
        if df_excel_data_part.loc[i,'ProdutosSessaoTabagica_1'] == 1:
            aaa = "Sim"
            ProdutosSessaoTabagica.append(aaa)
        elif df_excel_data_part.loc[i,'ProdutosSessaoTabagica_2'] == 1:
            aaa = "Não"
            ProdutosSessaoTabagica.append(aaa)
        elif df_excel_data_part.loc[i,'ProdutosSessaoTabagica_1'] == 0 and df_excel_data_part.loc[i,'ProdutosSessaoTabagica_2'] == 0:
            aaa = None
            ProdutosSessaoTabagica.append(aaa)

df_excel_data_part.drop(columns=['ProdutosSessaoTabagica_1','ProdutosSessaoTabagica_2'],inplace=True)

df_excel_data_part['ProdutosSessaoTabagica'] = ProdutosSessaoTabagica
TransCol = df_excel_data_part.pop('ProdutosSessaoTabagica')
df_excel_data_part.insert(16,"ProdutosSessaoTabagica",TransCol)

for i in range(0,len(df_excel_data_part['ConsomeCafeina'])):
        if df_excel_data_part.loc[i,'ConsomeCafeina'] == 1:
            df_excel_data_part.loc[i,'ConsomeCafeina'] = "Sim"
        else:
            df_excel_data_part.loc[i,'ConsomeCafeina'] = "Não"

for i in range(0,len(df_excel_data_part['ConsomeAlcool'])):
        if df_excel_data_part.loc[i,'ConsomeAlcool'] == 1:
            df_excel_data_part.loc[i,'ConsomeAlcool'] = "Sim"
        else:
            df_excel_data_part.loc[i,'ConsomeAlcool'] = "Não"

for i in range(0,len(df_excel_data_part['ConsomeDrogas'])):
        if df_excel_data_part.loc[i,'ConsomeDrogas'] == 1:
            df_excel_data_part.loc[i,'ConsomeDrogas'] = "Sim"
        else:
            df_excel_data_part.loc[i,'ConsomeDrogas'] = "Não"

for i in range(0,len(df_excel_data_part['Viagens'])):
        if df_excel_data_part.loc[i,'Viagens'] == 1:
            df_excel_data_part.loc[i,'Viagens'] = "Sim"
        else:
            df_excel_data_part.loc[i,'Viagens'] = "Não"

#############Cronotipo
colChronotype = []
for i in range(0,len(df_excel_data_part['MEQscore'])):
    if df_excel_data_part.loc[i,'MEQscore'] < 31:
        temp_hold_chrono = 'Definitivamente Vespertino'
    elif df_excel_data_part.loc[i,'MEQscore'] >=  31 and df_excel_data_part.loc[i,'MEQscore'] <= 42:
        temp_hold_chrono = 'Moderadamente Vespertino'
    elif df_excel_data_part.loc[i,'MEQscore'] >=  43 and df_excel_data_part.loc[i,'MEQscore'] <= 53:
        temp_hold_chrono = 'Intermédio'
    elif df_excel_data_part.loc[i,'MEQscore'] >=  54 and df_excel_data_part.loc[i,'MEQscore'] <= 59:
        temp_hold_chrono = 'Moderadamente Matutino'
    elif df_excel_data_part.loc[i,'MEQscore'] > 59:
        temp_hold_chrono = 'Definitivamente Matutino'
    colChronotype.append(temp_hold_chrono)

df_excel_data_part['Cronotipo'] = colChronotype
TransCol = df_excel_data_part.pop('Cronotipo')
df_excel_data_part.insert(40,"Cronotipo",TransCol)

####Calculo Fatores BSI
#############Somatizacao
FatorSomatizacao = []
for i in range(0,len(df_excel_data_part['participant'])):
    temp_somatizacao = (df_excel_data_part.loc[i,'BSI:2'] + df_excel_data_part.loc[i,'BSI:7'] + df_excel_data_part.loc[i,'BSI:23'] + df_excel_data_part.loc[i,'BSI:29'] + df_excel_data_part.loc[i,'BSI:30'] + df_excel_data_part.loc[i,'BSI:33'] + df_excel_data_part.loc[i,'BSI:37'])/7
    FatorSomatizacao.append(temp_somatizacao)

df_excel_data_part['Somatizacao'] = FatorSomatizacao
TransCol = df_excel_data_part.pop('Somatizacao')
df_excel_data_part.insert(94,"Somatizacao",TransCol)
##############FatorObsessoesCompulsoes
FatorObsessoesCompulsoes = []
for i in range(0,len(df_excel_data_part['participant'])):
    temp_FatorObsessoesCompulsoes = (df_excel_data_part.loc[i,'BSI:5'] + df_excel_data_part.loc[i,'BSI:15'] + df_excel_data_part.loc[i,'BSI:26'] + df_excel_data_part.loc[i,'BSI:27'] + df_excel_data_part.loc[i,'BSI:32'] + df_excel_data_part.loc[i,'BSI:36'])/6
    FatorObsessoesCompulsoes.append(temp_FatorObsessoesCompulsoes)

df_excel_data_part['FatorObsessoesCompulsoes'] = FatorObsessoesCompulsoes
TransCol = df_excel_data_part.pop('FatorObsessoesCompulsoes')
df_excel_data_part.insert(95,"FatorObsessoesCompulsoes",TransCol)

##############FatorSensibilidadeInterpessoal
FatorSensibilidadeInterpessoal = []
for i in range(0,len(df_excel_data_part['participant'])):
    temp_FatorSensibilidadeInterpessoal = (df_excel_data_part.loc[i,'BSI:20'] + df_excel_data_part.loc[i,'BSI:21'] + df_excel_data_part.loc[i,'BSI:22'] + df_excel_data_part.loc[i,'BSI:42'])/4
    FatorSensibilidadeInterpessoal.append(temp_FatorSensibilidadeInterpessoal)

df_excel_data_part['FatorSensibilidadeInterpessoal'] = FatorSensibilidadeInterpessoal
TransCol = df_excel_data_part.pop('FatorSensibilidadeInterpessoal')
df_excel_data_part.insert(96,"FatorSensibilidadeInterpessoal",TransCol)


##############FatorDepressao
FatorDepressao = []
for i in range(0,len(df_excel_data_part['participant'])):
    temp_FatorDepressao = (df_excel_data_part.loc[i,'BSI:9'] + df_excel_data_part.loc[i,'BSI:16'] + df_excel_data_part.loc[i,'BSI:17'] + df_excel_data_part.loc[i,'BSI:18'] + df_excel_data_part.loc[i,'BSI:35'] + df_excel_data_part.loc[i,'BSI:50'])/6
    FatorDepressao.append(temp_FatorDepressao)

df_excel_data_part['FatorDepressao'] = FatorDepressao
TransCol = df_excel_data_part.pop('FatorDepressao')
df_excel_data_part.insert(97,"FatorDepressao",TransCol)

##############FatorAnsiedade
FatorAnsiedade = []
for i in range(0,len(df_excel_data_part['participant'])):
    temp_FatorAnsiedade = (df_excel_data_part.loc[i,'BSI:1'] + df_excel_data_part.loc[i,'BSI:12'] + df_excel_data_part.loc[i,'BSI:19'] + df_excel_data_part.loc[i,'BSI:38'] + df_excel_data_part.loc[i,'BSI:45'] + df_excel_data_part.loc[i,'BSI:49'])/6
    FatorAnsiedade.append(temp_FatorAnsiedade)

df_excel_data_part['FatorAnsiedade'] = FatorAnsiedade
TransCol = df_excel_data_part.pop('FatorAnsiedade')
df_excel_data_part.insert(98,"FatorAnsiedade",TransCol)

##############FatorHostilidade
FatorHostilidade = []
for i in range(0,len(df_excel_data_part['participant'])):
    temp_FatorHostilidade = (df_excel_data_part.loc[i,'BSI:6'] + df_excel_data_part.loc[i,'BSI:13'] + df_excel_data_part.loc[i,'BSI:40'] + df_excel_data_part.loc[i,'BSI:41'] + df_excel_data_part.loc[i,'BSI:46'])/5
    FatorHostilidade.append(temp_FatorHostilidade)

df_excel_data_part['FatorHostilidade'] = FatorHostilidade
TransCol = df_excel_data_part.pop('FatorHostilidade')
df_excel_data_part.insert(99,"FatorHostilidade",TransCol)

##############FatorAnsiedadeFobica
FatorAnsiedadeFobica = []
for i in range(0,len(df_excel_data_part['participant'])):
    temp_FatorAnsiedadeFobica = (df_excel_data_part.loc[i,'BSI:8'] + df_excel_data_part.loc[i,'BSI:28'] + df_excel_data_part.loc[i,'BSI:31'] + df_excel_data_part.loc[i,'BSI:43'] + df_excel_data_part.loc[i,'BSI:47'])/5
    FatorAnsiedadeFobica.append(temp_FatorAnsiedadeFobica)

df_excel_data_part['FatorAnsiedadeFobica'] = FatorAnsiedadeFobica
TransCol = df_excel_data_part.pop('FatorAnsiedadeFobica')
df_excel_data_part.insert(100,"FatorAnsiedadeFobica",TransCol)

##############FatorIdeacaoParanoide
FatorIdeacaoParanoide = []
for i in range(0,len(df_excel_data_part['participant'])):
    temp_FatorIdeacaoParanoide = (df_excel_data_part.loc[i,'BSI:4'] + df_excel_data_part.loc[i,'BSI:10'] + df_excel_data_part.loc[i,'BSI:24'] + df_excel_data_part.loc[i,'BSI:48'] + df_excel_data_part.loc[i,'BSI:51'])/5
    FatorIdeacaoParanoide.append(temp_FatorIdeacaoParanoide)

df_excel_data_part['FatorIdeacaoParanoide'] = FatorIdeacaoParanoide
TransCol = df_excel_data_part.pop('FatorIdeacaoParanoide')
df_excel_data_part.insert(101,"FatorIdeacaoParanoide",TransCol)

##############FatorPsicoticismo
FatorPsicoticismo = []
for i in range(0,len(df_excel_data_part['participant'])):
    temp_FatorPsicoticismo = (df_excel_data_part.loc[i,'BSI:3'] + df_excel_data_part.loc[i,'BSI:14'] + df_excel_data_part.loc[i,'BSI:34'] + df_excel_data_part.loc[i,'BSI:44'] + df_excel_data_part.loc[i,'BSI:53'])/5
    FatorPsicoticismo.append(temp_FatorPsicoticismo)

df_excel_data_part['FatorPsicoticismo'] = FatorPsicoticismo
TransCol = df_excel_data_part.pop('FatorPsicoticismo')
df_excel_data_part.insert(102,"FatorPsicoticismo",TransCol)


##############IGS
IGS = []
for i in range(0,len(df_excel_data_part['participant'])):
    temp_IGS = (df_excel_data_part.loc[i,'BSI:1'] +	df_excel_data_part.loc[i,'BSI:2'] +	df_excel_data_part.loc[i,'BSI:3'] +	df_excel_data_part.loc[i,'BSI:4'] +	df_excel_data_part.loc[i,'BSI:5'] +	df_excel_data_part.loc[i,'BSI:6'] +	df_excel_data_part.loc[i,'BSI:7'] +	df_excel_data_part.loc[i,'BSI:8'] +	df_excel_data_part.loc[i,'BSI:9'] +	df_excel_data_part.loc[i,'BSI:10'] + df_excel_data_part.loc[i,'BSI:11'] + df_excel_data_part.loc[i,'BSI:12'] + df_excel_data_part.loc[i,'BSI:13'] +	df_excel_data_part.loc[i,'BSI:14'] +	df_excel_data_part.loc[i,'BSI:15'] +	df_excel_data_part.loc[i,'BSI:16'] +	df_excel_data_part.loc[i,'BSI:17'] +	df_excel_data_part.loc[i,'BSI:18'] +	df_excel_data_part.loc[i,'BSI:19'] +	df_excel_data_part.loc[i,'BSI:20'] +	df_excel_data_part.loc[i,'BSI:21'] +	df_excel_data_part.loc[i,'BSI:22'] +	df_excel_data_part.loc[i,'BSI:23'] +	df_excel_data_part.loc[i,'BSI:24'] +	df_excel_data_part.loc[i,'BSI:25'] +	df_excel_data_part.loc[i,'BSI:26'] +	df_excel_data_part.loc[i,'BSI:27'] +	df_excel_data_part.loc[i,'BSI:28'] +	df_excel_data_part.loc[i,'BSI:29'] +	df_excel_data_part.loc[i,'BSI:30'] +	df_excel_data_part.loc[i,'BSI:31'] +	df_excel_data_part.loc[i,'BSI:32'] +	df_excel_data_part.loc[i,'BSI:33'] +	df_excel_data_part.loc[i,'BSI:34'] +	df_excel_data_part.loc[i,'BSI:35'] +	df_excel_data_part.loc[i,'BSI:36'] +	df_excel_data_part.loc[i,'BSI:37'] +	df_excel_data_part.loc[i,'BSI:38'] +	df_excel_data_part.loc[i,'BSI:39'] +	df_excel_data_part.loc[i,'BSI:40'] +	df_excel_data_part.loc[i,'BSI:41'] +	df_excel_data_part.loc[i,'BSI:42'] +	df_excel_data_part.loc[i,'BSI:43'] +	df_excel_data_part.loc[i,'BSI:44'] +	df_excel_data_part.loc[i,'BSI:45'] +	df_excel_data_part.loc[i,'BSI:46'] +	df_excel_data_part.loc[i,'BSI:47'] +	df_excel_data_part.loc[i,'BSI:48'] +	df_excel_data_part.loc[i,'BSI:49'] +	df_excel_data_part.loc[i,'BSI:50'] + df_excel_data_part.loc[i,'BSI:51'] + df_excel_data_part.loc[i,'BSI:52'] + df_excel_data_part.loc[i,'BSI:53'])/53
    IGS.append(temp_IGS)

df_excel_data_part['IGS'] = IGS
TransCol = df_excel_data_part.pop('IGS')
df_excel_data_part.insert(103,"IGS",TransCol)

##############TSP
TSP = []
for i in range(0,len(df_excel_data_part['participant'])):
    temp_TSP = 0
    for j in range(41,94):
        if df_excel_data_part.iloc[i,j] != 0:
            temp_TSP += 1
    TSP.append(temp_TSP)

df_excel_data_part['TSP'] = TSP
TransCol = df_excel_data_part.pop('TSP')
df_excel_data_part.insert(104,"TSP",TransCol)

##############ISP
ISP = []
for i in range(0,len(df_excel_data_part['participant'])):
    temp_ISP = 0
    temp_TSP = 0
    for j in range(41,94):
        if df_excel_data_part.iloc[i,j] != 0:
            temp_ISP += df_excel_data_part.iloc[i,j]
            temp_TSP += 1
    if temp_TSP != 0:
        temp_ISP = temp_ISP/temp_TSP
    else:
        temp_ISP = 0
    ISP.append(temp_ISP)

df_excel_data_part['ISP'] = ISP
TransCol = df_excel_data_part.pop('ISP')
df_excel_data_part.insert(105,"ISP",TransCol)

cols_to_round = [
    "Somatizacao",
    "FatorObsessoesCompulsoes",
    "FatorSensibilidadeInterpessoal",
    "FatorDepressao",
    "FatorAnsiedade",
    "FatorHostilidade",
    "FatorAnsiedadeFobica",
    "FatorIdeacaoParanoide",
    "FatorPsicoticismo",
    "IGS",
    "ISP"
]
df_excel_data_part[cols_to_round] = df_excel_data_part[cols_to_round].round(2)

###Grava a DataFrame com os dados dos participantes limpos num excel chamdado BD_Secrrening
df_excel_Screening = df_excel_data_part.copy(deep=True)
df_excel_Screening = df_excel_Screening.rename(columns={"participant": "subject_nr"})
################################################################################################################################################################################
#
#
#
#
#
#
#
#
###############################################################################################################################################################################
#2 - Generates DB with data collected in the activity and sleep diaries.
##Imports libraries
import pandas as pd
import os, datetime, time

########################################################################################################################################
##Sleep Diary

#Opens the excel file where data from participants are stored.
SD_excel_part_data_path = os.getcwd() + "\DiariosSonoAtividade\dataSono.xlsx"
SD_df_excel_data_part = pd.read_excel(SD_excel_part_data_path)

##Drops redundant columns (empty columns regarding the column with the session number) in the dataframe df_excel_data_part.
SD_df_excel_data_part.drop(SD_df_excel_data_part.columns[3:11],axis=1,inplace=True)

##Substitui os nomes das colunas pelos labels corretos
SD_df_excel_data_part.columns = ['participant', 'Subject_Nr', 'Session_Nr', 'Data', 'SD_Q1', 'SD_Q2', 'SD_Q3', 'SD_Q4', 'SD_Q5', 'SD_Q6a',
                               'SD_Q6b', 'SD_Q6c', 'SD_Q6d', 'SD_Q7', 'SD_Q8', 'SD_Q9', 'SD_Q10', 'SD_Q11', 'TIME_start', 'TIME_end','TIME_total']

##Organiza os registos pelo número de participante e número de sessão (por ordem ascendente).
SD_df_excel_data_part.sort_values(by=['Session_Nr'], kind='mergesort', inplace=True,ascending=True)
SD_df_excel_data_part.sort_values(by=['Subject_Nr'], kind='mergesort', inplace=True,ascending=True)
SD_df_excel_data_part.reset_index(drop=True,inplace=True)

##Subsitui valores númericos que codificam um certo label, pelo label correto.
for i in range(0,len(SD_df_excel_data_part['SD_Q6c'])):
        if SD_df_excel_data_part.loc[i,'SD_Q6c'] == 1:
            SD_df_excel_data_part.loc[i,'SD_Q6c'] = "Sim"
        else :
            SD_df_excel_data_part.loc[i,'SD_Q6c'] = "Não"

for i in range(0,len(SD_df_excel_data_part['SD_Q9'])):
        if SD_df_excel_data_part.loc[i,'SD_Q9'] == 1:
            SD_df_excel_data_part.loc[i,'SD_Q9'] = "Muito Pobre"
        elif SD_df_excel_data_part.loc[i,'SD_Q9'] == 2:
            SD_df_excel_data_part.loc[i,'SD_Q9'] = "Pobre"
        elif SD_df_excel_data_part.loc[i,'SD_Q9'] == 3:
            SD_df_excel_data_part.loc[i,'SD_Q9'] = "Aceitável"
        elif SD_df_excel_data_part.loc[i,'SD_Q9'] == 4:
            SD_df_excel_data_part.loc[i,'SD_Q9'] = "Boa"
        else :
            SD_df_excel_data_part.loc[i,'SD_Q9'] = "Muito Boa"

for i in range(0,len(SD_df_excel_data_part['SD_Q10'])):
        if SD_df_excel_data_part.loc[i,'SD_Q10'] == 1:
            SD_df_excel_data_part.loc[i,'SD_Q10'] = "Nada descansado(a)/restabelecido(a)"
        elif SD_df_excel_data_part.loc[i,'SD_Q10'] == 2:
            SD_df_excel_data_part.loc[i,'SD_Q10'] = "Ligeiramente descansado(a)/restabelecido(a)"
        elif SD_df_excel_data_part.loc[i,'SD_Q10'] == 3:
            SD_df_excel_data_part.loc[i,'SD_Q10'] = "Aceitavelmente descansado(a)/restabelecido(a)"
        elif SD_df_excel_data_part.loc[i,'SD_Q10'] == 4:
            SD_df_excel_data_part.loc[i,'SD_Q10'] = "Bem descansado(a)/restabelecido(a)"
        else :
            SD_df_excel_data_part.loc[i,'SD_Q10'] = "Muito bem descansado(a)/restabelecido(a)"

#Calcula e cria as colunas do sleep onset latency (SOL), sleep after final awakening (TASAFA), time awake after initial sleep onset but
#before the final awakening (WASO), Total Sleep Time (TST), duration of sleep episode (DSE), and sleep efficiency (SE).

#Creates column with sleep onset latency (SOL) values
SD_df_excel_data_part['SOL'] = SD_df_excel_data_part['SD_Q3']

#Creates column with time attempting to sleep after final awakening (TASAFA) values
SD_df_excel_data_part['TASAFA'] = SD_df_excel_data_part['SD_Q6b']

#Creates column with time awake after initial sleep onset but before the final awakening (WASO) values
SD_df_excel_data_part['WASO'] = SD_df_excel_data_part['SD_Q5']
#Substitui valores vazios (correspondente a participantes que não responderam à questão) por 0.
for i in range(0,len(SD_df_excel_data_part['WASO'])):
    if pd.isnull(SD_df_excel_data_part.loc[i,'WASO']):
        SD_df_excel_data_part.loc[i,'WASO'] = 0

#Creates column with time Total Sleep Time (TST) values
temp_sleep_time = SD_df_excel_data_part['SD_Q2'].copy(deep=True)
##Cálcula o número de horas que passaram desde o momento em que o participante começou a tentar dormir até ao momento em que se levantou
##e iníciou a sua rotna.
for i in range(0,len(temp_sleep_time)):
    temp_sleep_time[i] = pd.to_datetime(str(temp_sleep_time[i]))
temp_rising_time = SD_df_excel_data_part['SD_Q6a'].copy(deep=True)
for i in range(0,len(temp_rising_time)):
    temp_rising_time[i] = pd.to_datetime(str(temp_rising_time[i]))
temp_diff_ris_sleep = temp_rising_time - temp_sleep_time
##Exclui a informação referente à data e deixa apenas a informação referente à hora e minutos.
for i in range(0,len(temp_diff_ris_sleep)):
    temp_diff_ris_sleep[i] = str(temp_diff_ris_sleep[i])
    aaa = (str(temp_diff_ris_sleep[i]))
    aaa = aaa[-8:-3]
    temp_diff_ris_sleep[i] = aaa
#    temp_diff_ris_sleep[i] = temp_diff_ris_sleep[i][7:12]

temp_TST = []
TST_for_DSE = []
for i in range(0,len(temp_diff_ris_sleep)):
##Converte o formato hh:mm em minutos e subtrai o valor do WASo e do SOL para calcular o TST.
##Volta a converter o TST num forato HHhMM
    aaa = float(temp_diff_ris_sleep[i][0:2])
    aaa = aaa*60
    bbb = float(temp_diff_ris_sleep[i][3:6])
    aaa = aaa + bbb
    aaa = aaa - SD_df_excel_data_part.loc[i,'WASO'] - SD_df_excel_data_part.loc[i,'SOL']
    TST_for_DSE.append(aaa)
    aaa = aaa/60
    aaa = '{0:02.0f}:{1:02.0f}'.format(*divmod(aaa * 60, 60))
    aaa = str(aaa)
    aaa = aaa.replace(":","h")
    temp_TST.append(aaa)
SD_df_excel_data_part['TST'] = temp_TST

#Creates column with time duration of the duration of sleep episode (DSE) values.
# The DSE is calculating by suming the SOL, WASO, TST, and the TASAFA.
temp_DSE = []
DSE_for_SE = []
for i in range(0,len(SD_df_excel_data_part['participant'])):
    aaa = TST_for_DSE[i] + SD_df_excel_data_part.loc[i,'WASO'] + SD_df_excel_data_part.loc[i,'SOL'] + SD_df_excel_data_part.loc[i,'TASAFA']
    DSE_for_SE.append(aaa)
    aaa = aaa/60
    aaa = '{0:02.0f}:{1:02.0f}'.format(*divmod(aaa * 60, 60))
    aaa = str(aaa)
    aaa = aaa.replace(":","h")
    temp_DSE.append(aaa)
SD_df_excel_data_part['DSE'] = temp_DSE


#Creates column with time duration of the sleep efficiency (SE) values.
# The SE is the ratio of total sleep time (TST) to duration of sleep episode (SDE).
temp_SE = []
for i in range(0,len(SD_df_excel_data_part['participant'])):
    aaa = round((TST_for_DSE[i]/DSE_for_SE[i])*100,2)
    temp_SE.append(aaa)
SD_df_excel_data_part['SE'] = temp_SE

twentythree = 82800
twentythree = datetime.time(23,0,0)
one = 3600
one = datetime.time(1,0,0)
seven = 25200
seven = datetime.time(7,0,0)
nine = datetime.time(9,0,0)
TSTsix = 360
TSTnine = 540

SD_df_excel_data_part = SD_df_excel_data_part[['Subject_Nr', 'Session_Nr', 'Data', 'SD_Q1', 'SD_Q2',
       'SD_Q3', 'SD_Q4', 'SD_Q5', 'SD_Q6a', 'SD_Q6b', 'SD_Q6c', 'SD_Q6d',
       'SD_Q7', 'SD_Q8', 'SD_Q9', 'SD_Q10', 'SD_Q11', 'SOL', 'TASAFA', 'WASO', 'TST', 'DSE', 'SE', 'TIME_start', 'TIME_end',
       'TIME_total']]


#####################################################################################################################################
##Activity Diary

#Opens the excel file where data from participants are stored.
AD_excel_part_data_path = os.getcwd() + "\DiariosSonoAtividade\dataAtividade.xlsx"
AD_df_excel_data_part = pd.read_excel(AD_excel_part_data_path)

##Drops redundant columns (empty columns regarding the column with the session number) in the dataframe df_excel_data_part.
AD_df_excel_data_part.drop(AD_df_excel_data_part.columns[3:11],axis=1,inplace=True)

##Substitui os nomes das colunas pelos labels corretos
AD_df_excel_data_part.columns = ["participant","Subject_Nr","Session_Nr","Data","AD_Q1","AD_Q2","AD_Q3","AD_Q4:1","AD_Q4:2","AD_Q4:3",
                                 "AD_Q4:4","AD_Q4:5","AD_Q4:6","AD_Q4:7","AD_Q4:8","AD_Q4:9","AD_Q4:10","AD_Q4:11","AD_Q4:12","AD_Q4:13",
                                 "AD_Q4:14","AD_Q4:15","AD_Q4:16","AD_Q4:17","AD_Q4:18","AD_Q4:19","AD_Q4:20","AD_Q4:21","AD_Q4:22",
                                 "AD_Q4:23","AD_Q4:24","AD_Q5","AD_Q6:1","AD_Q6:2","AD_Q6:3","AD_Q6:4","AD_Q6:5","AD_Q6:6","AD_Q6:7",
                                 "AD_Q6:8","AD_Q6:9","AD_Q6:10","AD_Q6:11","AD_Q6:12","AD_Q6:13","AD_Q6:14","AD_Q6:15","AD_Q6:16",
                                 "AD_Q6:17","AD_Q6:18","AD_Q6:19","AD_Q6:20","AD_Q6:21","AD_Q6:22","AD_Q6:23","AD_Q6:24","AD_Q7",
                                 "SD_Q8","AD_Q9:1","AD_Q9:2","AD_Q9:3","AD_Q9:4","AD_Q9:5","AD_Q9:6","AD_Q9:7","AD_Q9:8","AD_Q9:9",
                                 "AD_Q9:10","AD_Q9:11","AD_Q9:12","AD_Q9:13","AD_Q9:14","AD_Q9:15","AD_Q9:16","AD_Q9:17","AD_Q9:18",
                                 "AD_Q9:19","AD_Q9:20","AD_Q9:21","AD_Q9:22","AD_Q9:23","AD_Q9:24","AD_Q10","AD_Q11:1","AD_Q11:2",
                                 "AD_Q11:3","AD_Q11:4","AD_Q11:5","AD_Q11:6","AD_Q11:7","AD_Q11:8","AD_Q11:9","AD_Q11:10","AD_Q11:11",
                                 "AD_Q11:12","AD_Q11:13","AD_Q11:14","AD_Q11:15","AD_Q11:16","AD_Q11:17","AD_Q11:18","AD_Q11:19",
                                 "AD_Q11:20","AD_Q11:21","AD_Q11:22","AD_Q11:23","AD_Q11:24","AD_Q12","TIME_start","TIME_end",
                                 "TIME_total"]


##Organiza os registos pelo número de participante e número de sessão (por ordem ascendente).
AD_df_excel_data_part.sort_values(by=['Session_Nr'], kind='mergesort', inplace=True,ascending=True)
AD_df_excel_data_part.sort_values(by=['Subject_Nr'], kind='mergesort', inplace=True,ascending=True)
AD_df_excel_data_part.reset_index(drop=True,inplace=True)

##Substitui os valores númericos que codificam horas nas colunas referentes às questões 4,6,9 11 pelos labels corretos (horas
#correspondenes, p. ex., 04h00)
for i in range(0,len(AD_df_excel_data_part['AD_Q4:1'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:1'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:1'] = '00h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:2'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:2'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:2'] = '01h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:3'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:3'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:3'] = '02h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:4'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:4'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:4'] = '03h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:5'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:5'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:5'] = '04h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:6'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:6'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:6'] = '05h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:7'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:7'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:7'] = '06h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:8'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:8'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:8'] = '07h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:9'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:9'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:9'] = '08h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:10'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:10'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:10'] = '09h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:11'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:11'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:11'] = '10h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:12'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:12'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:12'] = '11h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:13'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:13'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:13'] = '12h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:14'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:14'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:14'] = '13h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:15'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:15'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:15'] = '14h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:16'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:16'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:16'] = '15h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:17'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:17'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:17'] = '16h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:18'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:18'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:18'] = '17h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:19'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:19'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:19'] = '18h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:20'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:20'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:20'] = '19h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:21'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:21'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:21'] = '20h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:22'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:22'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:22'] = '21h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:23'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:23'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:23'] = '22h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q4:24'])):
    if AD_df_excel_data_part.loc[i,'AD_Q4:24'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q4:24'] = '23h00'

for i in range(0,len(AD_df_excel_data_part['AD_Q6:1'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:1'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:1'] = '00h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:2'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:2'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:2'] = '01h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:3'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:3'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:3'] = '02h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:4'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:4'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:4'] = '03h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:5'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:5'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:5'] = '04h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:6'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:6'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:6'] = '05h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:7'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:7'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:7'] = '06h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:8'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:8'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:8'] = '07h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:9'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:9'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:9'] = '08h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:10'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:10'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:10'] = '09h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:11'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:11'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:11'] = '10h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:12'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:12'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:12'] = '11h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:13'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:13'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:13'] = '12h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:14'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:14'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:14'] = '13h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:15'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:15'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:15'] = '14h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:16'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:16'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:16'] = '15h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:17'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:17'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:17'] = '16h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:18'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:18'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:18'] = '17h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:19'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:19'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:19'] = '18h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:20'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:20'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:20'] = '19h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:21'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:21'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:21'] = '20h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:22'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:22'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:22'] = '21h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:23'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:23'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:23'] = '22h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q6:24'])):
    if AD_df_excel_data_part.loc[i,'AD_Q6:24'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q6:24'] = '23h00'


for i in range(0,len(AD_df_excel_data_part['AD_Q9:1'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:1'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:1'] = '00h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:2'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:2'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:2'] = '01h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:3'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:3'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:3'] = '02h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:4'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:4'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:4'] = '03h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:5'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:5'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:5'] = '04h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:6'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:6'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:6'] = '05h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:7'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:7'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:7'] = '06h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:8'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:8'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:8'] = '07h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:9'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:9'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:9'] = '08h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:10'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:10'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:10'] = '09h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:11'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:11'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:11'] = '10h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:12'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:12'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:12'] = '11h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:13'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:13'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:13'] = '12h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:14'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:14'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:14'] = '13h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:15'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:15'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:15'] = '14h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:16'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:16'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:16'] = '15h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:17'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:17'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:17'] = '16h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:18'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:18'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:18'] = '17h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:19'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:19'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:19'] = '18h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:20'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:20'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:20'] = '19h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:21'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:21'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:21'] = '20h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:22'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:22'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:22'] = '21h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:23'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:23'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:23'] = '22h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q9:24'])):
    if AD_df_excel_data_part.loc[i,'AD_Q9:24'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q9:24'] = '23h00'


for i in range(0,len(AD_df_excel_data_part['AD_Q11:1'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:1'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:1'] = '00h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:2'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:2'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:2'] = '01h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:3'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:3'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:3'] = '02h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:4'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:4'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:4'] = '03h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:5'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:5'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:5'] = '04h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:6'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:6'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:6'] = '05h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:7'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:7'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:7'] = '06h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:8'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:8'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:8'] = '07h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:9'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:9'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:9'] = '08h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:10'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:10'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:10'] = '09h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:11'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:11'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:11'] = '10h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:12'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:12'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:12'] = '11h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:13'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:13'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:13'] = '12h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:14'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:14'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:14'] = '13h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:15'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:15'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:15'] = '14h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:16'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:16'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:16'] = '15h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:17'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:17'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:17'] = '16h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:18'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:18'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:18'] = '17h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:19'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:19'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:19'] = '18h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:20'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:20'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:20'] = '19h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:21'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:21'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:21'] = '20h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:22'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:22'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:22'] = '21h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:23'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:23'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:23'] = '22h00'
for i in range(0,len(AD_df_excel_data_part['AD_Q11:24'])):
    if AD_df_excel_data_part.loc[i,'AD_Q11:24'] == 1:
        AD_df_excel_data_part.loc[i, 'AD_Q11:24'] = '23h00'


for i in range(0,len(AD_df_excel_data_part['AD_Q7'])):
        if AD_df_excel_data_part.loc[i,'AD_Q7'] == 1:
            AD_df_excel_data_part.loc[i,'AD_Q7'] = "Sim"
        else:
            AD_df_excel_data_part.loc[i, 'AD_Q7'] = "Não"

for i in range(0,len(AD_df_excel_data_part['AD_Q10'])):
        if AD_df_excel_data_part.loc[i,'AD_Q10'] == 1:
            AD_df_excel_data_part.loc[i,'AD_Q10'] = "Sim"
        else:
            AD_df_excel_data_part.loc[i, 'AD_Q10'] = "Não"

##Cria listas com os horários em que os participantes consumiram bebidas alcoólicas (Q4), bebidas cafeinadas (Q6), tomaram medicação
##para dormir (Q9), ou fizeram exercício (Q11) e guarda essas listas em colunas na dataframe 'AD_df_excel_data_part'.
major_list = []
for j in range(0,len(AD_df_excel_data_part['participant'])):
    temp_list = []
    for i in range(7,31):
        if AD_df_excel_data_part.iloc[j,i] != 0:
            temp_list.append(AD_df_excel_data_part.iloc[j,i])
    major_list.append(temp_list)
for i in range(0,len(major_list)):
    if major_list[i] == []:
        major_list[i] = None
AD_df_excel_data_part["AD_Q4"] = major_list

major_list = []
for j in range(0,len(AD_df_excel_data_part['participant'])):
    temp_list = []
    for i in range(32,56):
        if AD_df_excel_data_part.iloc[j,i] != 0:
            temp_list.append(AD_df_excel_data_part.iloc[j,i])
    major_list.append(temp_list)
for i in range(0,len(major_list)):
    if major_list[i] == []:
        major_list[i] = None
AD_df_excel_data_part["AD_Q6"] = major_list

major_list = []
for j in range(0,len(AD_df_excel_data_part['participant'])):
    temp_list = []
    for i in range(58,82):
        if AD_df_excel_data_part.iloc[j,i] != 0:
            temp_list.append(AD_df_excel_data_part.iloc[j,i])
    major_list.append(temp_list)
for i in range(0,len(major_list)):
    if major_list[i] == []:
        major_list[i] = None
AD_df_excel_data_part["AD_Q9"] = major_list

major_list = []
for j in range(0,len(AD_df_excel_data_part['participant'])):
    temp_list = []
    for i in range(83,107):
        if AD_df_excel_data_part.iloc[j,i] != 0:
            temp_list.append(AD_df_excel_data_part.iloc[j,i])
    major_list.append(temp_list)
for i in range(0,len(major_list)):
    if major_list[i] == []:
        major_list[i] = None
AD_df_excel_data_part["AD_Q11"] = major_list

##Elimina colunas que já não são úteis relacionadas com as questões 4, 6, 9 e 11.
AD_df_excel_data_part.drop(AD_df_excel_data_part.columns[83:107],axis=1,inplace=True)
AD_df_excel_data_part.drop(AD_df_excel_data_part.columns[58:82],axis=1,inplace=True)
AD_df_excel_data_part.drop(AD_df_excel_data_part.columns[32:56],axis=1,inplace=True)
AD_df_excel_data_part.drop(AD_df_excel_data_part.columns[7:31],axis=1,inplace=True)


cols_to_clean = ["AD_Q4","AD_Q6", "AD_Q11"]  # columns where [''] appears
for col in cols_to_clean:
    AD_df_excel_data_part[col] = (
        AD_df_excel_data_part[col]
        .astype(str)
        .str.replace(r"[\[\]']", "", regex=True)  # remove [, ], '
        .str.strip()
    )


##Reorganiza a ordem das colunas da DataFrame AD_df_excel_data_part.
AD_df_excel_data_part = AD_df_excel_data_part[['Subject_Nr', 'Session_Nr', 'Data', 'AD_Q1', 'AD_Q2', 'AD_Q3', 'AD_Q4',
                                               'AD_Q5', 'AD_Q6', 'AD_Q7', 'SD_Q8', 'AD_Q9', 'AD_Q10', 'AD_Q11', 'AD_Q12', 'TIME_start',
                                               'TIME_end', 'TIME_total']]

################################################################################################################################################################################
#
#
#
#
#
#
#
#
###############################################################################################################################################################################
#3 - Generates DB with the actigraphy data collected.
##Imports libraries
import pandas as pd
import os, datetime, time, re
from datetime import timedelta, datetime
import glob, shutil

#Opens the csv. file where data from participants are stored.
csv_part_data_path = os.getcwd() + "\Actigraphy"
list_of_files = os.listdir(csv_part_data_path)
pattern = "part5_daysummary"
for i in list_of_files:
    if pattern in i:
        csv_part_data_path = csv_part_data_path + "\\" + i
df_csv_data_part = pd.read_csv(csv_part_data_path, engine = 'python',sep = ',')
df_csv_data_part.sort_values("ID")

#Select relevant columns from the csv produced by GeneActive.
df_csv_data_part = df_csv_data_part[["ID","filename","sleeplog_used","guider","cleaningcode","daysleeper","night_number","calendar_date","weekday",
                                     "nonwear_perc_day_spt","sleeponset_ts","wakeup_ts","dur_day_spt_min","dur_day_min","dur_spt_min",
                                     "dur_spt_wake_IN_min","dur_spt_wake_LIG_min","dur_spt_wake_MOD_min","dur_spt_wake_VIG_min","dur_day_IN_unbt_min",
                                     "dur_day_LIG_unbt_min","dur_day_MOD_unbt_min","dur_day_VIG_unbt_min","dur_spt_sleep_min","sleep_efficiency"]]

#Opens the csv. file where the data from the first night is stored.
csv_part_data_path2 = os.getcwd() + "\Actigraphy"
list_of_files = os.listdir(csv_part_data_path2)
csv_part_data_path2 = csv_part_data_path2 + "\\" + 'part4_nightsummary_sleep_cleaned.csv'
df_csv_data_part2 = pd.read_csv(csv_part_data_path2, engine = 'python',sep = ',')
df_csv_data_part2.sort_values("ID")
df_csv_data_part2 = df_csv_data_part2[df_csv_data_part2['night'] == 1]
df_csv_data_part3 = df_csv_data_part2.copy(deep=True)

df_csv_data_part2 = df_csv_data_part2[["ID","filename","sleeplog_used","guider","cleaningcode","daysleeper","night","calendar_date","weekday",
                                     "nonwear_perc_spt","sleeponset_ts","wakeup_ts"]]
df_csv_data_part2 = df_csv_data_part2.assign(dur_day_spt_min="",dur_day_min="",dur_spt_min="",dur_spt_wake_IN_min="",
                                             dur_spt_wake_LIG_min="",dur_spt_wake_MOD_min="",dur_spt_wake_VIG_min="",
                                             dur_day_IN_unbt_min="",dur_day_LIG_unbt_min="",dur_day_MOD_unbt_min="",
                                             dur_day_VIG_unbt_min="",dur_spt_sleep_min="",sleep_efficiency="")
df_csv_data_part2.rename(columns={'night':'night_number','nonwear_perc_spt':'nonwear_perc_day_spt'},inplace=True)
df_csv_data_part2 = df_csv_data_part2[["ID","filename","sleeplog_used","guider","cleaningcode","daysleeper","night_number","calendar_date","weekday",
                                     "nonwear_perc_day_spt","sleeponset_ts","wakeup_ts","dur_day_spt_min","dur_day_min","dur_spt_min",
                                     "dur_spt_wake_IN_min","dur_spt_wake_LIG_min","dur_spt_wake_MOD_min","dur_spt_wake_VIG_min","dur_day_IN_unbt_min",
                                     "dur_day_LIG_unbt_min","dur_day_MOD_unbt_min","dur_day_VIG_unbt_min","dur_spt_sleep_min","sleep_efficiency"]]
frames = [df_csv_data_part,df_csv_data_part2]
df_csv_data_part = pd.concat(frames)
df_csv_data_part = df_csv_data_part.sort_values(by=['ID','night_number'],ascending=[True,True])
df_csv_data_part.reset_index(drop=True,inplace=True)

pattern2 = "_(.*?)_"
List_actigraph_location = []
for i in range(len(df_csv_data_part["filename"])):
    substring = re.search(pattern2, df_csv_data_part["filename"][i]).group(1)
    List_actigraph_location.append(substring)
LocationAcel = pd.Series(List_actigraph_location)
df_csv_data_part.insert(2,"LocationAcel",LocationAcel)

for i in range(0,len(df_csv_data_part["daysleeper"])):
    if df_csv_data_part.loc[i,"daysleeper"] == 0:
        df_csv_data_part.loc[i,"daysleeper"] = "day sleeper"
    elif df_csv_data_part.loc[i,"daysleeper"] == 1:
        df_csv_data_part.loc[i,"daysleeper"] = "night sleeper"

for i in range(0,len(df_csv_data_part["sleeplog_used"])):
    if df_csv_data_part.loc[i,"sleeplog_used"] == 0:
        df_csv_data_part.loc[i,"sleeplog_used"] = "No"
    elif df_csv_data_part.loc[i,"sleeplog_used"] == 1:
        df_csv_data_part.loc[i,"sleeplog_used"] = "Yes"

for i in range(0,len(df_csv_data_part["cleaningcode"])):
    if df_csv_data_part.loc[i,"cleaningcode"] == 1:
        df_csv_data_part.loc[i,"cleaningcode"] = "1: GGIR sleep log was not used. Thus, HDCZA guider was used. Only Sleep Period Time (SPT) was identified " \
                                                  "(it was not possible to indentify Time in Bed (TIB))."

for i in range(0,len(df_csv_data_part["calendar_date"])):
    if df_csv_data_part.loc[i,"night_number"] == 1:
        x = df_csv_data_part.loc[i,"calendar_date"].split("/")
        y = []
        for j in x:
            y.insert(0,j)
        for j in range(0,len(y)):
            if int(y[j]) < 10:
                y[j] = '0' + y[j]
        y = str(y)
        y = y.replace("[","")
        y = y.replace("]","")
        y = y.replace("'","")
        y = y.replace(" ","")
        y = y.replace(",","-")
        df_csv_data_part.loc[i,"calendar_date"] = y

List_WASO = []
for i in range(0,len(df_csv_data_part)):
    if df_csv_data_part.loc[i,"night_number"] == 1:
        List_WASO.append(round(df_csv_data_part3.loc[i,"WASO"]*60,3))
    else:
        ind = df_csv_data_part.loc[i,"dur_spt_wake_IN_min"] + df_csv_data_part.loc[i,"dur_spt_wake_LIG_min"] + df_csv_data_part.loc[i,"dur_spt_wake_MOD_min"] + df_csv_data_part.loc[i,"dur_spt_wake_VIG_min"]
        List_WASO.append(ind)
row,col = df_csv_data_part.shape
List_WASO = pd.Series(List_WASO)
df_csv_data_part.insert(col-1,"WASO",List_WASO)


List_target_col = ["dur_day_spt_min","dur_day_min","dur_spt_min","dur_spt_sleep_min","dur_spt_wake_IN_min",
                    "dur_spt_wake_LIG_min","dur_spt_wake_MOD_min","dur_spt_wake_VIG_min","dur_day_IN_unbt_min","dur_day_LIG_unbt_min",
                    "dur_day_MOD_unbt_min","dur_day_VIG_unbt_min","WASO"]

for i in List_target_col:
    for l in range(0,len(df_csv_data_part)):
        if df_csv_data_part.loc[l,"night_number"] != 1:
            if df_csv_data_part.loc[l,i] == 0:
                df_csv_data_part.loc[l,i] = timedelta(hours=00, minutes=00, seconds=00)
            else:
                df_csv_data_part.loc[l,i] = timedelta(minutes=df_csv_data_part.loc[l,i])

wakeupminusbedtime = []
for i in range(0,len(df_csv_data_part)):
    if df_csv_data_part.loc[i,"night_number"] == 1:
        aaa = datetime.strptime(df_csv_data_part.loc[i,"sleeponset_ts"], "%H:%M:%S")
        aaa = timedelta(hours=aaa.hour, minutes=aaa.minute, seconds=aaa.second)
        if timedelta(hours=9,minutes=0,seconds=0) <= aaa <= timedelta(hours=23,minutes=59,seconds=59):
            bbb = timedelta(hours=23,minutes=59,seconds=59) - aaa + timedelta(hours=0,minutes=0,seconds=1)
        else:
            bbb = timedelta(hours=00,minutes=0,seconds=0)
        ccc = datetime.strptime(df_csv_data_part.loc[i,"wakeup_ts"], "%H:%M:%S")
        ccc = timedelta(hours=ccc.hour, minutes=ccc.minute, seconds=ccc.second)
        ddd = df_csv_data_part.loc[i,"WASO"]*60
        ddd = timedelta(seconds=ddd)
        if timedelta(hours=9,minutes=0,seconds=0) <= aaa <= timedelta(hours=23,minutes=59,seconds=59):
            df_csv_data_part.loc[i,"dur_spt_sleep_min"] = ccc + bbb - ddd
            wakeupminusbedtime.append(ccc + bbb)
        else:
            df_csv_data_part.loc[i,"dur_spt_sleep_min"] = ccc - aaa - ddd
            wakeupminusbedtime.append(ccc - aaa)
        df_csv_data_part.loc[i,"WASO"] = ddd

#Opens the csv. file where data from participants are stored.
Daily_Logs_df_excel_data_part = SD_df_excel_data_part.copy(deep=True)
Daily_Logs_df_excel_data_part2 = SD_df_excel_data_part.copy(deep=True)

Daily_Logs_df_excel_data_part = Daily_Logs_df_excel_data_part[["SD_Q2","SD_Q7"]]
List_columns_Daily_Logs = ["SD_Q2","SD_Q7"]
for i in List_columns_Daily_Logs:
    for l in range(0,len(Daily_Logs_df_excel_data_part)):
        t = Daily_Logs_df_excel_data_part.loc[l,i]
        Daily_Logs_df_excel_data_part.loc[l,i] = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)
df_csv_data_part.insert(11,"Bedtime",Daily_Logs_df_excel_data_part["SD_Q2"])
df_csv_data_part.insert(14,"Risetime",Daily_Logs_df_excel_data_part["SD_Q7"])

List_columns_sleeponset_wakeup = ["sleeponset_ts","wakeup_ts"]
for i in List_columns_sleeponset_wakeup:
    for l in range(0,len(df_csv_data_part)):
        t = datetime.strptime(df_csv_data_part.loc[l,i], "%H:%M:%S")
        df_csv_data_part.loc[l,i] = timedelta(hours=t.hour, minutes=t.minute, seconds=t.second)

aaa = timedelta(hours=00, minutes=00, seconds=00)
bbb = timedelta(hours=7, minutes=00, seconds=00)
ccc = timedelta(hours=24, minutes=00, seconds=00)

temp_sleep_onset = aaa
temp_Bedtime = aaa
List_SOL = []
df_csv_data_part["Bedtime"] = pd.to_timedelta(df_csv_data_part["Bedtime"], errors="coerce")
df_csv_data_part["Risetime"] = pd.to_timedelta(df_csv_data_part["Risetime"], errors="coerce")
for i in range(0,len(df_csv_data_part)):
    if df_csv_data_part.loc[i,"sleeponset_ts"] < bbb:
        temp_sleep_onset = df_csv_data_part.loc[i,"sleeponset_ts"] + ccc
    else:
        temp_sleep_onset = df_csv_data_part.loc[i,"sleeponset_ts"]
    if df_csv_data_part.loc[i,"Bedtime"] < bbb:
        temp_Bedtime = df_csv_data_part.loc[i, "Bedtime"] + ccc
    else:
        temp_Bedtime = df_csv_data_part.loc[i, "Bedtime"]
    if temp_sleep_onset < temp_Bedtime:
        df_csv_data_part.loc[i, "sleeponset_ts"] = df_csv_data_part.loc[i, "Bedtime"]
    temp_SOL = temp_sleep_onset - temp_Bedtime
    if temp_SOL < aaa:
        temp_SOL = aaa
    List_SOL.append(temp_SOL)
df_csv_data_part.insert(col,"SOL",List_SOL)

for i in range(0,len(df_csv_data_part)):
    if df_csv_data_part.loc[i,"wakeup_ts"] > df_csv_data_part.loc[i,"Risetime"]:
        df_csv_data_part.loc[i,"wakeup_ts"] = df_csv_data_part.loc[i,"Risetime"]

List_TASAFA = []
for i in range(0,len(df_csv_data_part)):
    temp_TASAFA = df_csv_data_part.loc[i, "Risetime"] - df_csv_data_part.loc[i, "wakeup_ts"]
    if temp_TASAFA < aaa:
        temp_TASAFA = aaa
    List_TASAFA.append(temp_TASAFA)
df_csv_data_part.insert(col+3,"TASAFA",List_TASAFA)

List_DSE = []
for i in range(0,len(df_csv_data_part)):
    temp_DSE = df_csv_data_part.loc[i,"SOL"] + df_csv_data_part.loc[i,"dur_spt_sleep_min"] + df_csv_data_part.loc[i,"WASO"] + df_csv_data_part.loc[i,"TASAFA"]
    List_DSE.append(temp_DSE)
df_csv_data_part["DSE"] = List_DSE

List_SEF = []
for i in range(0,len(df_csv_data_part)):
    temp_SEF = round(df_csv_data_part.loc[i,"dur_spt_sleep_min"] / df_csv_data_part.loc[i,"DSE"],3)
    List_SEF.append(temp_SEF)
df_csv_data_part["Sleep Efficiency TST(Act)/DSE(Act)"] = List_SEF

columns_re = ["ID","filename","LocationAcel","sleeplog_used","guider","cleaningcode","daysleeper","night_number","calendar_date",
              "weekday","nonwear_perc_day_spt","Bedtime","sleeponset_ts","wakeup_ts","Risetime","SOL","dur_spt_sleep_min","WASO",
              "TASAFA","DSE","sleep_efficiency","Sleep Efficiency TST(Act)/DSE(Act)","dur_day_spt_min","dur_day_min","dur_spt_min",
              "dur_spt_wake_IN_min","dur_spt_wake_LIG_min","dur_spt_wake_MOD_min","dur_spt_wake_VIG_min","dur_day_IN_unbt_min",
              "dur_day_LIG_unbt_min","dur_day_MOD_unbt_min","dur_day_VIG_unbt_min"]


df_csv_data_part = df_csv_data_part.reindex(columns=columns_re)
col_names = ["ID","filename","LocationAcel","sleeplog_used","guider","cleaningcode","daysleeper","night_number","calendar_date",
              "weekday","nonwear_perc","Bedtime","Sleep Onset","Wakeup Time","Rise Time","SOL","TST","WASO",
              "TASAFA","DSE","Sleep Efficiency GGIR (TST/(Wakeup-Sleep Onset))","Sleep Efficiency TST(Act)/DSE(Act)",
             "Duration Day+Sleep episodes","Duration Day Episode","Duration Sleep Episode (Wakeup-Sleep Onset)",
             "Duration Inactive in Sleep Episode","Duration Light Activity in Sleep Episode",
             "Duration Moderate Activity in Sleep Episode","Duration Vigorous Activity in Sleep Episode",
             "Duration Inactive in Day Episode","Duration Light Activity in Day Episode",
             "Duration Moderate Activity in Day Episode","Duration Vigorous Activity in Day Episode"]

df_csv_data_part.columns = col_names

indexx = 0
for i in range(0,len(df_csv_data_part)):
    if df_csv_data_part.loc[i,"night_number"] == 1:
        df_csv_data_part.loc[i,"Sleep Efficiency GGIR (TST/(Wakeup-Sleep Onset))"] = round(df_csv_data_part.loc[i,"TST"]/wakeupminusbedtime[indexx],3)
        df_csv_data_part.loc[i,"Duration Sleep Episode (Wakeup-Sleep Onset)"] = wakeupminusbedtime[indexx]
        indexx += 1
    else:
        if df_csv_data_part.loc[i,"Sleep Onset"] > bbb:
            temp_sleep_onset = ccc - df_csv_data_part.loc[i,"Sleep Onset"]
            df_csv_data_part.loc[i,"Sleep Efficiency GGIR (TST/(Wakeup-Sleep Onset))"] = round(df_csv_data_part.loc[i,"TST"]/(df_csv_data_part.loc[i,"Wakeup Time"] + temp_sleep_onset),3)
        else:
            df_csv_data_part.loc[i, "Sleep Efficiency GGIR (TST/(Wakeup-Sleep Onset))"] = round(df_csv_data_part.loc[i, "TST"]/(df_csv_data_part.loc[i, "Wakeup Time"] - df_csv_data_part.loc[i,"Sleep Onset"]), 3)

##################################################################################################################
#Create dataframe with Sleep Efficiency indexes
df_sleep_eff_indexes = pd.DataFrame({
    "ID": df_csv_data_part["ID"],
    "Date": df_csv_data_part["calendar_date"],
    "ExpDay": df_csv_data_part["night_number"],
    "SE Sleep Log (TST/DSE)": Daily_Logs_df_excel_data_part2["SE"],
    "SE GGIR (TST/(Wakeup-Sleep Onset))": df_csv_data_part["Sleep Efficiency GGIR (TST/(Wakeup-Sleep Onset))"],
    "SE TST(Act)/DSE(Act)": df_csv_data_part["Sleep Efficiency TST(Act)/DSE(Act)"]
})

EmptyList = []
for i in range(0,len(df_sleep_eff_indexes)):
    EmptyList.append(None)
df_sleep_eff_indexes[""] = EmptyList

# list of time-like columns
time_cols = [
    "Bedtime",
    "Sleep Onset",
    "Wakeup Time",
    "Rise Time",
    "SOL",
    "TST",
    "WASO",
    "TASAFA",
    "DSE",
    "Duration Day+Sleep episodes",
    "Duration Day Episode",
    "Duration Sleep Episode (Wakeup-Sleep Onset)",
    "Duration Inactive in Sleep Episode",
    "Duration Light Activity in Sleep Episode",
    "Duration Moderate Activity in Sleep Episode",
    "Duration Vigorous Activity in Sleep Episode",
    "Duration Inactive in Day Episode",
    "Duration Light Activity in Day Episode",
    "Duration Moderate Activity in Day Episode",
    "Duration Vigorous Activity in Day Episode"
]

# ensure they're timedelta first
df_csv_data_part[time_cols] = df_csv_data_part[time_cols].apply(pd.to_timedelta, errors="coerce")

# convert timedelta → string "HH:MM:SS"
for col in time_cols:
    df_csv_data_part[col] = df_csv_data_part[col].apply(
        lambda x: (
            f"{int(x.total_seconds() // 3600):02d}:"
            f"{int((x.total_seconds() % 3600) // 60):02d}:"
            f"{int(x.total_seconds() % 60):02d}"
        ) if pd.notna(x) else ""
    )


cols_to_round = [
    "nonwear_perc",
    "Sleep Efficiency GGIR (TST/(Wakeup-Sleep Onset))",
    "Sleep Efficiency TST(Act)/DSE(Act)"
]
df_csv_data_part[cols_to_round] = df_csv_data_part[cols_to_round].round(2)

df_Actigraphy = df_csv_data_part.copy(deep=True)
################################################################################################################################################################################
#
#
#
#
#
#
#
#
###############################################################################################################################################################################
#4 - Generates DB with practice session data.
#Importa as bibliotecas que são utilizadas neste script
import re
import pandas as pd
import os

#Guarda o path onde estão guardados os ficheiros com os dados experimentais dos participantes
part_data_path = os.getcwd() + "\data_participants_practice"

#Esta função cria uma lista com os nomes de todos os ficheiros que estão no diretório contido na variável part_data_path.
#No fundo, esta função cria uma lista com os nomes dos ficheiros que contêm os dados experimentais dos participantes.
list_of_files = os.listdir(part_data_path)

#Acrescenta a raíz 'data_participants' à lista que contém os nomes dos ficheiros que contêm os dados dos participantes.
full_path_files = []
for i in range(0,len(list_of_files)):
    create_str_file = 'data_participants_practice/' + list_of_files[i]
    full_path_files.append(create_str_file)

#Cria uma Dataframe com os dados de tod
# os os participantes utilizando o métodos 'read_csv' para criar uma DataFrame para os dados
#de cada participante, e depois unindo estas DataFrames através do método append().
df_total_part = pd.DataFrame()
for i in range(0, len(full_path_files)):
    df = pd.read_csv(full_path_files[i],error_bad_lines=False)
    df_total_part = df_total_part.append(df)

df_total_part.reset_index(inplace=True)

#Substitui dados que deviam estar listados como missing values ('undefined'), por missing values ('Nan')

#Puxa a coluna com o nome da tarefa que foi realizado neste ensaio e número do participante para a primeira e
#segunda coluna respetivamente.
first_column = df_total_part.pop('Task_Name')
second_column = df_total_part.pop('subject_nr')
df_total_part.insert(0, 'Task_Name', first_column)
df_total_part.insert(1, 'subject_nr', second_column)


#Os seguintes 5 blocos de código criam 5 DataFrames distintas.
#Cada uma das DataFrames vai conter a informação referente a cada uma das sete tarefas de memória de trabalho (reading span, symmetry
# span, operation span, binding task e Updating Task) realizadas por todos os participantes.

df_Reading_Span = df_total_part[df_total_part['Task_Name'] == 'Reading Span']
df_Reading_Span = df_Reading_Span.sort_values(by=['subject_nr'], kind='mergesort')

df_WMU_Task = df_total_part[df_total_part['Task_Name'] == 'Working Memory Updating Task']
df_WMU_Task = df_WMU_Task.sort_values(by=['subject_nr'], kind='mergesort')

df_Symmetry_Span = df_total_part[df_total_part['Task_Name'] == 'Symmetry Span']
df_Symmetry_Span = df_Symmetry_Span.sort_values(by=['subject_nr'], kind='mergesort')

df_Binding_Task = df_total_part[df_total_part['Task_Name'] == 'Binding Task']
df_Binding_Task = df_Binding_Task.sort_values(by=['subject_nr'], kind='mergesort')

df_Operation_Span = df_total_part[df_total_part['Task_Name'] == 'Operation Span']
df_Operation_Span = df_Operation_Span.sort_values(by=['subject_nr'], kind='mergesort')

#################################################################################################################

df_raw_scores = pd.DataFrame()

subj_nr = df_total_part["subject_nr"].unique()
df_raw_scores.insert(0,'subject_nr',subj_nr)

##############################################################################################################

Temperature = pd.read_excel(r'C:\Users\fabio\OneDrive\Área de Trabalho\RPubs\Article 3\Temperature\Body_Temperature_Collection.xlsx',sheet_name='TempPractice')

aa = df_raw_scores["subject_nr"].astype("int")

ii = 0
k = 0

for i in Temperature["Subject ID"]:
    if int(i) in aa.values:
        df_raw_scores["Temperature (°C) Practice Sess"] = Temperature["Temperature (°C) Practice Sess"][ii]
    ii += 1
    k =+ 1
########################################################################################################

RawRS = list(df_Reading_Span.groupby(['subject_nr'], sort=True)['score_reading_span'].max() * 20)
df_raw_scores["Reading Span Practice Session"] = RawRS

RawUT = list(df_WMU_Task.groupby(['subject_nr'], sort=True)['WMUExperimentalScore'].max())
df_raw_scores["Updating Task Practice Session"] = RawUT

RawSS = list(df_Symmetry_Span.groupby(['subject_nr'], sort=True)['score_symmetry_span'].max() * 20)
df_raw_scores["Symmetry Span Practice Session"] = RawSS

RawBT = list(df_Binding_Task.groupby(['subject_nr'], sort=True)['BindingRawScore'].max())
df_raw_scores["Binding Task Practice Session"] = RawBT

RawOS = list(df_Operation_Span.groupby(['subject_nr'], sort=True)['score_operation_span'].max() * 20)
df_raw_scores["Operation Span Practice Session"] = RawOS

avg_RS_list = []
avg_UT_list = []
avg_SS_list = []
avg_BT_list = []
avg_OS_list = []
for i in range(0,len(df_raw_scores)):
    temp_avg_RS = df_raw_scores.loc[i,"Reading Span Practice Session"]
    avg_RS_list.append(temp_avg_RS)
    temp_avg_UT = df_raw_scores.loc[i,"Updating Task Practice Session"]
    avg_UT_list.append(temp_avg_UT)
    temp_avg_SS = df_raw_scores.loc[i,"Symmetry Span Practice Session"]
    avg_SS_list.append(temp_avg_SS)
    temp_avg_BT = df_raw_scores.loc[i,"Binding Task Practice Session"]
    avg_BT_list.append(temp_avg_BT)
    temp_avg_OS = df_raw_scores.loc[i,"Operation Span Practice Session"]
    avg_OS_list.append(temp_avg_OS)

for i in range(0,len(avg_RS_list)):
    avg_RS_list[i] = round(avg_RS_list[i]/20,2)
for i in range(0,len(avg_UT_list)):
    avg_UT_list[i] = round(avg_UT_list[i]/36,2)
for i in range(0,len(avg_SS_list)):
    avg_SS_list[i] = round(avg_SS_list[i]/20,2)
for i in range(0,len(avg_BT_list)):
    avg_BT_list[i] = round(avg_BT_list[i]/12,2)
for i in range(0,len(avg_OS_list)):
    avg_OS_list[i] = round(avg_OS_list[i]/20,2)

counterRS = 0
counterUT = 0
counterSS = 0
counterBT = 0
counterOS = 0

df_incl_exc = pd.DataFrame()
df_incl_exc["Subject Nr"] = subj_nr
########################################################################################################################################
######Criação da DataFrame com os valores normalizados obtidos por cada participante em cada uma das provas em que realizaram (e com os
#####dados socio-demografcos).
df_normalized_scores = df_raw_scores.copy(deep=True)

df_normalized_scores["Reading Span Practice Session"] = df_normalized_scores["Reading Span Practice Session"]/20
df_normalized_scores["Updating Task Practice Session"] = df_normalized_scores["Updating Task Practice Session"] / 36
df_normalized_scores["Symmetry Span Practice Session"] = df_normalized_scores["Symmetry Span Practice Session"] / 20
df_normalized_scores["Binding Task Practice Session"] = df_normalized_scores["Binding Task Practice Session"] / 12
df_normalized_scores["Operation Span Practice Session"] = df_normalized_scores["Operation Span Practice Session"] / 20

########################################################################################################
#Os próximos 5 blocos de código selecionam as colunas com informação relevante de cada WM task e guardam estas colunas em DataFrames
#que só contêm informação relacionada com a mesma tarefa. Para além disso, estes nestes 5 blocos de código, são realizadas algumas
#conversões no formato dos dados (e.g., string to float) e são alterados os nomes de algumas colunas de forma a ficarem mais percétiveis.
#'selSNr',
df_Reading_Span = df_Reading_Span[
    ['subject_nr',  'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName', 'acc', 'avg_rt',
     'BlockChoice', 'correct', 'correct_response', 'Frase', 'height', 'letter', 'List_Prev_Letter',
     'List_responses_memory', 'live_row', 'logfile', 'response_average_time_memory', 'response_memory',
     'response_processing', 'response_time_memory', 'response_time_processing', 'response_total_time_memory',
     'RP_part_process_time', 'score_practice', 'score_reading_span', 'score_subblock_2', 'score_subblock_3', 'score_subblock_4',
     'score_subblock_5', 'score_subblock_6', 'Tipo', 'total_correct',
     'total_response_time', 'total_responses', 'width']]
df_Reading_Span[['acc', 'avg_rt']] = df_Reading_Span[['acc', 'avg_rt']].replace(',', '.')
df_Reading_Span = df_Reading_Span.astype(
    {'acc': 'float64', 'avg_rt': 'float64', 'correct_response': 'str', 'response_processing': 'str'})
example_b = df_Reading_Span["response_processing"].iloc[2]
df_Reading_Span = df_Reading_Span.replace(example_b, '')
#df_Reading_Span_1 = df_Reading_Span_1.sort_values(by=['selSNr'], kind='mergesort')
#df_Reading_Span_1 = df_Reading_Span_1.sort_values(by=['subject_nr'], kind='mergesort')
df_Reading_Span.columns = ['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco',
                             'SubTaskName','acc_Practice_Sess','avg_rt_Practice_Sess','BlockChoice_Practice_Sess','correct_Practice_Sess','correct_response_Practice_Sess',
                             'Frase_Practice_Sess','height_Practice_Sess','letter_Practice_Sess','List_Prev_Letter_Practice_Sess','List_responses_memory_Practice_Sess',
                             'live_row_Practice_Sess','logfile_Practice_Sess','response_average_time_memory_Practice_Sess','response_memory_Practice_Sess',
                             'response_processing_Practice_Sess','response_time_memory_Practice_Sess','response_time_processing_Practice_Sess',
                             'response_total_time_memory_Practice_Sess','RP_part_process_time_Practice_Sess','score_practice_Practice_Sess',
                             'score_reading_span_Practice_Sess','score_subblock_2_Practice_Sess','score_subblock_3_Practice_Sess','score_subblock_4_Practice_Sess',
                             'score_subblock_5_Practice_Sess','score_subblock_6_Practice_Sess','Tipo_Practice_Sess','total_correct_Practice_Sess',
                             'total_response_time_Practice_Sess','total_responses_Practice_Sess','width_Practice_Sess']

############################################################################################
############################################################################################
#'toUpdate1_1', 'toUpdate1_2', 'toUpdate1_3', 'toUpdate2_1', 'toUpdate2_2','toUpdate2_3','correct_response1', 'correct_response2', 'correct_response3',
#'selSNr',
df_WMU_Task = df_WMU_Task[
    ['subject_nr',  'CB_ref', 'practice', 'TrialNumber', 'correct1', 'correct2', 'correct3', 'digit1', 'digit2', 'digit3', 'height',
     'Index_List', 'live_row', 'logfile', 'response1', 'response2', 'response3', 'response_time1', 'responseavgRT',
     'total_correct_trial', 'TotalRtBlock',  'WMUExperimentalScore', 'WMUPracticeScore', 'width']]
df_WMU_Task = df_WMU_Task.rename(columns={'response_time1': 'response_time'})

for i in range(0, len(df_WMU_Task['responseavgRT'])):
    if df_WMU_Task['responseavgRT'].iloc[i] == 0:
        df_WMU_Task['responseavgRT'].iloc[i] = ''
df_WMU_Task.columns = ['subject_nr','CB_ref','practice','TrialNumber','correct1_Practice_Sess',
                         'correct2_Practice_Sess','correct3_Practice_Sess','digit1_Practice_Sess','digit2_Practice_Sess','digit3_Practice_Sess','height_Practice_Sess',
                         'Index_List_Practice_Sess','live_row_Practice_Sess','logfile_Practice_Sess','response1_Practice_Sess','response2_Practice_Sess','response3_Practice_Sess',
                         'response_time1_Practice_Sess','responseavgRT_Practice_Sess','total_correct_trial_Practice_Sess','TotalRtBlock_Practice_Sess',
                         'WMUExperimentalScore_Practice_Sess','WMUPracticeScore_Practice_Sess','width_Practice_Sess']


############################################################################################
#'selSNr',
df_Symmetry_Span = df_Symmetry_Span[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName',
     'aggregated_score_memory', 'average_response_time_processing', 'average_total_time_memory', 'correct',
     'correct_response', 'countDys', 'countSym', 'height', 'LeftHalfPos', 'List_SS_button', 'List_SS_Pos', 'live_row',
     'logfile', 'maxDys', 'maxSym', 'pressed_buttons', 'response_memory', 'response_processing', 'response_time_memory',
     'response_time_processing', 'response_total_time_memory', 'response_total_time_memory_full_task', 'RightHalfPos',
     'SP_part_process_time', 'SS_practice_score', 'score_symmetry_span', 'score_subblock_2', 'score_subblock_3',
     'score_subblock_4', 'score_subblock_5', 'score_subblock_6', 'SymType',
     'total_correct_processing', 'total_response_time_processing', 'width']]
df_Symmetry_Span = df_Symmetry_Span.astype({'correct_response': 'str', 'response_processing': 'str'})
example_d = df_Symmetry_Span["response_processing"].iloc[2]
df_Symmetry_Span = df_Symmetry_Span.replace(example_d, '')
#df_Symmetry_Span_1 = df_Symmetry_Span_1.sort_values(by=['selSNr'], kind='mergesort')
#df_Symmetry_Span_1 = df_Symmetry_Span_1.sort_values(by=['subject_nr'], kind='mergesort')
df_Symmetry_Span.columns = ['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco',
                              'SubTaskName','aggregated_score_memory_Practice_Sess','average_response_time_processing_Practice_Sess',
                              'average_total_time_memory_Practice_Sess','correct_Practice_Sess','correct_response_Practice_Sess','countDys_Practice_Sess',
                              'countSym_Practice_Sess','height_Practice_Sess','LeftHalfPos_Practice_Sess','List_SS_button_Practice_Sess','List_SS_Pos_Practice_Sess',
                              'live_row_Practice_Sess','logfile_Practice_Sess','maxDys_Practice_Sess','maxSym_Practice_Sess','pressed_buttons_Practice_Sess',
                              'response_memory_Practice_Sess','response_processing_Practice_Sess','response_time_memory_Practice_Sess',
                              'response_time_processing_Practice_Sess','response_total_time_memory_Practice_Sess',
                              'response_total_time_memory_full_task_Practice_Sess','RightHalfPos_Practice_Sess','SP_part_process_time_Practice_Sess',
                              'SS_practice_score_Practice_Sess','score_symmetry_span_Practice_Sess','score_subblock_2_Practice_Sess','score_subblock_3_Practice_Sess',
                              'score_subblock_4_Practice_Sess','score_subblock_5_Practice_Sess','score_subblock_6_Practice_Sess','SymType_Practice_Sess',
                              'total_correct_processing_Practice_Sess','total_response_time_processing_Practice_Sess','width_Practice_Sess']

############################################################################################
############################################################################################
#'Probe', 'Target',
#'selSNr',
df_Binding_Task = df_Binding_Task[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'acc', 'average_response_time',
     'BindingRawScore', 'correct', 'correct_response', 'counter', 'Delay', 'eightsec_accuracy', 'FalseAlarms', 'height',
     'Hits', 'live_row', 'logfile', 'match_1s_accuracy', 'match_1s_avg_rt', 'match_8s_accuracy', 'match_8s_avg_rt',
     'mismatch_1s_accuracy', 'mismatch_1s_avg_rt', 'mismatch_8s_accuracy', 'mismatch_8s_avg_rt', 'NNonResponses',
     'Omissions', 'onesec_accuracy', 'QuinetteAccuracyScore', 'QuinetteProcessingScore', 'response',
     'response_time', 'ResponsesGiven', 'total_correct', 'total_match_1s_rt', 'total_match_8s_rt',
     'total_mismatch_1s_rt', 'total_mismatch_8s_rt', 'total_response_time', 'total_responses', 'width']]
df_Binding_Task[['acc', 'average_response_time']] = df_Binding_Task[['acc', 'average_response_time']].replace(',', '.')
df_Binding_Task = df_Binding_Task.astype(
    {'acc': 'float64', 'average_response_time': 'float64', 'correct_response': 'str', 'response': 'str'})
#df_Binding_Task_1 = df_Binding_Task_1.sort_values(by=['selSNr'], kind='mergesort')
#df_Binding_Task_1 = df_Binding_Task_1.sort_values(by=['subject_nr'], kind='mergesort')
df_Binding_Task.columns = ['subject_nr','CB_ref','practice','TrialNumber','acc_Practice_Sess',
                             'average_response_time_Practice_Sess','BindingRawScore_Practice_Sess','correct_Practice_Sess','correct_response_Practice_Sess',
                             'counter_Practice_Sess','Delay_Practice_Sess','eightsec_accuracy_Practice_Sess','FalseAlarms_Practice_Sess','height_Practice_Sess','Hits_Practice_Sess',
                             'live_row_Practice_Sess','logfile_Practice_Sess','match_1s_accuracy_Practice_Sess','match_1s_avg_rt_Practice_Sess','match_8s_accuracy_Practice_Sess',
                             'match_8s_avg_rt_Practice_Sess','mismatch_1s_accuracy_Practice_Sess','mismatch_1s_avg_rt_Practice_Sess','mismatch_8s_accuracy_Practice_Sess',
                             'mismatch_8s_avg_rt_Practice_Sess','NNonResponses_Practice_Sess','Omissions_Practice_Sess','onesec_accuracy_Practice_Sess',
                             'QuinetteAccuracyScore_Practice_Sess','QuinetteProcessingScore_Practice_Sess','response_Practice_Sess','response_time_Practice_Sess',
                             'ResponsesGiven_Practice_Sess','total_correct_Practice_Sess','total_match_1s_rt_Practice_Sess','total_match_8s_rt_Practice_Sess',
                             'total_mismatch_1s_rt_Practice_Sess','total_mismatch_8s_rt_Practice_Sess','total_response_time_Practice_Sess','total_responses_Practice_Sess',
                             'width_Practice_Sess']

############################################################################################
############################################################################################
#'selSNr',
df_Operation_Span = df_Operation_Span[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName', 'acc', 'avg_rt',
     'BlockChoice', 'correct', 'correct_response', 'height', 'letter', 'List_Prev_Letter', 'List_responses_memory',
     'live_row', 'logfile', 'response_average_time_memory', 'response_memory', 'response_processing',
     'response_time_memory', 'response_time_processing', 'response_total_time_memory', 'OP_part_process_time',
     'score_practice', 'score_operation_span', 'score_subblock_2', 'score_subblock_3', 'score_subblock_4', 'score_subblock_5',
     'score_subblock_6', 'Tipo', 'total_correct', 'total_response_time',
     'total_responses', 'width']]
df_Operation_Span[['acc', 'avg_rt']] = df_Operation_Span[['acc', 'avg_rt']].replace(',', '.')
df_Operation_Span = df_Operation_Span.astype(
    {'acc': 'float64', 'avg_rt': 'float64', 'correct_response': 'str', 'response_processing': 'str'})
example_c = df_Operation_Span["response_processing"].iloc[2]
df_Operation_Span = df_Operation_Span.replace(example_c, '')
#df_Operation_Span_1 = df_Operation_Span_1.sort_values(by=['selSNr'], kind='mergesort')
#df_Operation_Span_1 = df_Operation_Span_1.sort_values(by=['subject_nr'], kind='mergesort')
df_Operation_Span.columns = ['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco',
                               'SubTaskName','acc_Practice_Sess','avg_rt_Practice_Sess','BlockChoice_Practice_Sess','correct_Practice_Sess',
                               'correct_response_Practice_Sess','height_Practice_Sess','letter_Practice_Sess','List_Prev_Letter_Practice_Sess',
                               'List_responses_memory_Practice_Sess','live_row_Practice_Sess','logfile_Practice_Sess','response_average_time_memory_Practice_Sess',
                               'response_memory_Practice_Sess','response_processing_Practice_Sess','response_time_memory_Practice_Sess',
                               'response_time_processing_Practice_Sess','response_total_time_memory_Practice_Sess','OP_part_process_time_Practice_Sess',
                               'score_practice_Practice_Sess','score_operation_span_Practice_Sess','score_subblock_2_Practice_Sess','score_subblock_3_Practice_Sess',
                               'score_subblock_4_Practice_Sess','score_subblock_5_Practice_Sess','score_subblock_6_Practice_Sess','Tipo_Practice_Sess',
                               'total_correct_Practice_Sess','total_response_time_Practice_Sess','total_responses_Practice_Sess','width_Practice_Sess']

####################################################################################################################################################################

df_Processing_Times = pd.DataFrame()
RS_avgPT = df_Reading_Span["response_time_processing_Practice_Sess"][2:].mean()
RS_sdPT = df_Reading_Span["response_time_processing_Practice_Sess"][2:].std()

SS_avgPT = df_Symmetry_Span["response_time_processing_Practice_Sess"][2:].mean()
SS_sdPT = df_Symmetry_Span["response_time_processing_Practice_Sess"][2:].std()

OS_avgPT = df_Operation_Span["response_time_processing_Practice_Sess"][2:].mean()
OS_sdPT = df_Operation_Span["response_time_processing_Practice_Sess"][2:].std()


RS_PT_F = RS_avgPT + (RS_sdPT*2.5)
SS_PT_F = SS_avgPT + (SS_sdPT*2.5)
OS_PT_F = OS_avgPT + (OS_sdPT*2.5)
df_Processing_Times["Reading Span"] = [RS_PT_F]
df_Processing_Times["Operation Span"] = [OS_PT_F]
df_Processing_Times["Symmetry Span"] = [SS_PT_F]

pattern = "subject-(.*?).csv"
Subj_Nr =  str(re.search(pattern,list_of_files[0]).group(1))
Str_File_Name = 'BD_Practice_Sessions.xlsx'

cols_to_round = [
    "Reading Span Practice Session",
    "Updating Task Practice Session",
    "Symmetry Span Practice Session",
    "Binding Task Practice Session",
    "Operation Span Practice Session",
]

df_normalized_scores[cols_to_round] = (
    df_normalized_scores[cols_to_round]
    .apply(pd.to_numeric, errors="coerce")  # converts text to numbers safely
    .round(2)  # rounds to 2 decimal places
)

df_normalized_scores["subject_nr"] = pd.to_numeric(df_normalized_scores["subject_nr"], errors="coerce")
df_normalized_scores = df_normalized_scores.sort_values(by="subject_nr").reset_index(drop=True)

df_raw_scores["subject_nr"] = pd.to_numeric(df_raw_scores["subject_nr"], errors="coerce")
df_raw_scores = df_raw_scores.sort_values(by="subject_nr").reset_index(drop=True)

df_incl_exc = df_incl_exc.sort_values(by="Subject Nr")
df_raw_scores_pract = df_raw_scores.sort_values(by="subject_nr")
df_normalized_scores_pract = df_normalized_scores.sort_values(by="subject_nr")

################################################################################################################################################################################
#
#
#
#
#
#
#
#
###############################################################################################################################################################################
#5 - Generates DB with experimental session data.
#Importa as bibliotecas que são utilizadas neste script
import pandas as pd
import os

#Guarda o path onde estão guardados os ficheiros com os dados experimentais dos participantes
part_data_path = os.getcwd() + "\data_participants_experimental"

#Esta função cria uma lista com os nomes de todos os ficheiros que estão no diretório contido na variável part_data_path.
#No fundo, esta função cria uma lista com os nomes dos ficheiros que contêm os dados experimentais dos participantes.
list_of_files = os.listdir(part_data_path)

#Acrescenta a raíz 'data_participants' à lista que contém os nomes dos ficheiros que contêm os dados dos participantes.
full_path_files = []
for i in range(0,len(list_of_files)):
    create_str_file = 'data_participants_experimental/' + list_of_files[i]
    full_path_files.append(create_str_file)

#Cria uma Dataframe com os dados de tod
# os os participantes utilizando o métodos 'read_csv' para criar uma DataFrame para os dados
#de cada participante, e depois unindo estas DataFrames através do método append().
df_total_part = pd.DataFrame()
for i in range(0, len(full_path_files)):
    df = pd.read_csv(full_path_files[i],error_bad_lines=False)
    df_total_part = df_total_part.append(df)

#Substitui dados que deviam estar listados como missing values ('undefined'), por missing values ('Nan')
df_total_part = df_total_part.replace('undefined','Nan')

#Puxa a coluna com o nome da tarefa que foi realizado neste ensaio e número do participante para a primeira e
#segunda coluna respetivamente.
first_column = df_total_part.pop('Task_Name')
second_column = df_total_part.pop('subject_nr')
df_total_part.insert(0, 'Task_Name', first_column)
df_total_part.insert(1, 'subject_nr', second_column)

#Os seguintes 5 blocos de código criam 5 DataFrames distintas.
#Cada uma das DataFrames vai conter a informação referente a cada uma das sete tarefas de memória de trabalho (reading span, symmetry
# span, operation span, binding task e Updating Task) realizadas por todos os participantes.
df_Reading_Span = df_total_part[df_total_part['Task_Name'] == 'Reading Span']
df_Reading_Span = df_Reading_Span.sort_values(by=['selSNr'], kind='mergesort')
df_Reading_Span = df_Reading_Span.sort_values(by=['subject_nr'], kind='mergesort')
df_Reading_Span_1 = df_Reading_Span.query('selSNr == 1 and 1 <= subject_nr <= 5 or selSNr == 4 and 6 <= subject_nr <= 10 or selSNr == 3 and 11 <= subject_nr <= 15 or selSNr == 2 and 16 <= subject_nr <= 20 or selSNr == 1 and subject_nr == 21 or selSNr == 4 and subject_nr == 22 or selSNr == 3 and subject_nr == 23 or selSNr == 2 and subject_nr == 24 or selSNr == 1 and subject_nr == 25 or selSNr == 4 and subject_nr == 26 or selSNr == 3 and subject_nr == 27  or selSNr == 2 and subject_nr == 28')
df_Reading_Span_1 = df_Reading_Span_1.reset_index(drop=True)
df_Reading_Span_2 = df_Reading_Span.query('selSNr == 2 and 1 <= subject_nr <= 5 or selSNr == 1 and 6 <= subject_nr <= 10 or selSNr == 4 and 11 <= subject_nr <= 15 or selSNr == 3 and 16 <= subject_nr <= 20 or selSNr == 2 and subject_nr == 21 or selSNr == 1 and subject_nr == 22 or selSNr == 4 and subject_nr == 23 or selSNr == 3 and subject_nr == 24 or selSNr == 2 and subject_nr == 25 or selSNr == 1 and subject_nr == 26  or selSNr == 4 and subject_nr == 27  or selSNr == 3 and subject_nr == 28')
df_Reading_Span_2 = df_Reading_Span_2.reset_index(drop=True)
df_Reading_Span_3 = df_Reading_Span.query('selSNr == 3 and 1 <= subject_nr <= 5 or selSNr == 2 and 6 <= subject_nr <= 10 or selSNr == 1 and 11 <= subject_nr <= 15 or selSNr == 4 and 16 <= subject_nr <= 20 or selSNr == 3 and subject_nr == 21 or selSNr == 2 and subject_nr == 22 or selSNr == 1 and subject_nr == 23 or selSNr == 4 and subject_nr == 24 or selSNr == 3 and subject_nr == 25 or selSNr == 2 and subject_nr == 26  or selSNr == 1 and subject_nr == 27  or selSNr == 4 and subject_nr == 28')
df_Reading_Span_3 = df_Reading_Span_3.reset_index(drop=True)
df_Reading_Span_4 = df_Reading_Span.query('selSNr == 4 and 1 <= subject_nr <= 5 or selSNr == 3 and 6 <= subject_nr <= 10 or selSNr == 2 and 11 <= subject_nr <= 15 or selSNr == 1 and 16 <= subject_nr <= 20 or selSNr == 4 and subject_nr == 21 or selSNr == 3 and subject_nr == 22 or selSNr == 2 and subject_nr == 23 or selSNr == 1 and subject_nr == 24 or selSNr == 4 and subject_nr == 25 or selSNr == 3 and subject_nr == 26  or selSNr == 2 and subject_nr == 27  or selSNr == 1 and subject_nr == 28')
df_Reading_Span_4 = df_Reading_Span_4.reset_index(drop=True)

df_WMU_Task = df_total_part[df_total_part['Task_Name'] == 'Working Memory Updating Task']
df_WMU_Task = df_WMU_Task.sort_values(by=['selSNr'], kind='mergesort')
df_WMU_Task = df_WMU_Task.sort_values(by=['subject_nr'], kind='mergesort')
df_WMU_Task_1 = df_WMU_Task.query('selSNr == 1 and 1 <= subject_nr <= 5 or selSNr == 4 and 6 <= subject_nr <= 10 or selSNr == 3 and 11 <= subject_nr <= 15 or selSNr == 2 and 16 <= subject_nr <= 20 or selSNr == 1 and subject_nr == 21 or selSNr == 4 and subject_nr == 22 or selSNr == 3 and subject_nr == 23 or selSNr == 2 and subject_nr == 24 or selSNr == 1 and subject_nr == 25 or selSNr == 4 and subject_nr == 26  or selSNr == 3 and subject_nr == 27  or selSNr == 2 and subject_nr == 28')
df_WMU_Task_1 = df_WMU_Task_1.reset_index(drop=True)
df_WMU_Task_2 = df_WMU_Task.query('selSNr == 2 and 1 <= subject_nr <= 5 or selSNr == 1 and 6 <= subject_nr <= 10 or selSNr == 4 and 11 <= subject_nr <= 15 or selSNr == 3 and 16 <= subject_nr <= 20 or selSNr == 2 and subject_nr == 21 or selSNr == 1 and subject_nr == 22 or selSNr == 4 and subject_nr == 23 or selSNr == 3 and subject_nr == 24 or selSNr == 2 and subject_nr == 25 or selSNr == 1 and subject_nr == 26  or selSNr == 4 and subject_nr == 27  or selSNr == 3 and subject_nr == 28')
df_WMU_Task_2 = df_WMU_Task_2.reset_index(drop=True)
df_WMU_Task_3 = df_WMU_Task.query('selSNr == 3 and 1 <= subject_nr <= 5 or selSNr == 2 and 6 <= subject_nr <= 10 or selSNr == 1 and 11 <= subject_nr <= 15 or selSNr == 4 and 16 <= subject_nr <= 20 or selSNr == 3 and subject_nr == 21 or selSNr == 2 and subject_nr == 22 or selSNr == 1 and subject_nr == 23 or selSNr == 4 and subject_nr == 24 or selSNr == 3 and subject_nr == 25 or selSNr == 2 and subject_nr == 26  or selSNr == 1 and subject_nr == 27  or selSNr == 4 and subject_nr == 28')
df_WMU_Task_3 = df_WMU_Task_3.reset_index(drop=True)
df_WMU_Task_4 = df_WMU_Task.query('selSNr == 4 and 1 <= subject_nr <= 5 or selSNr == 3 and 6 <= subject_nr <= 10 or selSNr == 2 and 11 <= subject_nr <= 15 or selSNr == 1 and 16 <= subject_nr <= 20 or selSNr == 4 and subject_nr == 21 or selSNr == 3 and subject_nr == 22 or selSNr == 2 and subject_nr == 23 or selSNr == 1 and subject_nr == 24 or selSNr == 4 and subject_nr == 25 or selSNr == 3 and subject_nr == 26  or selSNr == 2 and subject_nr == 27  or selSNr == 1 and subject_nr == 28')
df_WMU_Task_4 = df_WMU_Task_4.reset_index(drop=True)

df_Symmetry_Span = df_total_part[df_total_part['Task_Name'] == 'Symmetry Span']
df_Symmetry_Span = df_Symmetry_Span.sort_values(by=['selSNr'], kind='mergesort')
df_Symmetry_Span = df_Symmetry_Span.sort_values(by=['subject_nr'], kind='mergesort')
df_Symmetry_Span_1 = df_Symmetry_Span.query('selSNr == 1 and 1 <= subject_nr <= 5 or selSNr == 4 and 6 <= subject_nr <= 10 or selSNr == 3 and 11 <= subject_nr <= 15 or selSNr == 2 and 16 <= subject_nr <= 20 or selSNr == 1 and subject_nr == 21 or selSNr == 4 and subject_nr == 22 or selSNr == 3 and subject_nr == 23 or selSNr == 2 and subject_nr == 24 or selSNr == 1 and subject_nr == 25 or selSNr == 4 and subject_nr == 26 or selSNr == 3 and subject_nr == 27  or selSNr == 2 and subject_nr == 28')
df_Symmetry_Span_1 = df_Symmetry_Span_1.reset_index(drop=True)
df_Symmetry_Span_2 = df_Symmetry_Span.query('selSNr == 2 and 1 <= subject_nr <= 5 or selSNr == 1 and 6 <= subject_nr <= 10 or selSNr == 4 and 11 <= subject_nr <= 15 or selSNr == 3 and 16 <= subject_nr <= 20 or selSNr == 2 and subject_nr == 21 or selSNr == 1 and subject_nr == 22 or selSNr == 4 and subject_nr == 23 or selSNr == 3 and subject_nr == 24 or selSNr == 2 and subject_nr == 25 or selSNr == 1 and subject_nr == 26 or selSNr == 4 and subject_nr == 27  or selSNr == 3 and subject_nr == 28')
df_Symmetry_Span_2 = df_Symmetry_Span_2.reset_index(drop=True)
df_Symmetry_Span_3 = df_Symmetry_Span.query('selSNr == 3 and 1 <= subject_nr <= 5 or selSNr == 2 and 6 <= subject_nr <= 10 or selSNr == 1 and 11 <= subject_nr <= 15 or selSNr == 4 and 16 <= subject_nr <= 20 or selSNr == 3 and subject_nr == 21 or selSNr == 2 and subject_nr == 22 or selSNr == 1 and subject_nr == 23 or selSNr == 4 and subject_nr == 24 or selSNr == 3 and subject_nr == 25 or selSNr == 2 and subject_nr == 26 or selSNr == 1 and subject_nr == 27  or selSNr == 4 and subject_nr == 28')
df_Symmetry_Span_3 = df_Symmetry_Span_3.reset_index(drop=True)
df_Symmetry_Span_4 = df_Symmetry_Span.query('selSNr == 4 and 1 <= subject_nr <= 5 or selSNr == 3 and 6 <= subject_nr <= 10 or selSNr == 2 and 11 <= subject_nr <= 15 or selSNr == 1 and 16 <= subject_nr <= 20 or selSNr == 4 and subject_nr == 21 or selSNr == 3 and subject_nr == 22 or selSNr == 2 and subject_nr == 23 or selSNr == 1 and subject_nr == 24 or selSNr == 4 and subject_nr == 25 or selSNr == 3 and subject_nr == 26 or selSNr == 2 and subject_nr == 27  or selSNr == 1 and subject_nr == 28')
df_Symmetry_Span_4 = df_Symmetry_Span_4.reset_index(drop=True)

df_Binding_Task = df_total_part[df_total_part['Task_Name'] == 'Binding Task']
df_Binding_Task = df_Binding_Task.sort_values(by=['selSNr'], kind='mergesort')
df_Binding_Task = df_Binding_Task.sort_values(by=['subject_nr'], kind='mergesort')
df_Binding_Task_1 = df_Binding_Task.query('selSNr == 1 and 1 <= subject_nr <= 5 or selSNr == 4 and 6 <= subject_nr <= 10 or selSNr == 3 and 11 <= subject_nr <= 15 or selSNr == 2 and 16 <= subject_nr <= 20 or selSNr == 1 and subject_nr == 21 or selSNr == 4 and subject_nr == 22 or selSNr == 3 and subject_nr == 23 or selSNr == 2 and subject_nr == 24 or selSNr == 1 and subject_nr == 25 or selSNr == 4 and subject_nr == 26 or selSNr == 3 and subject_nr == 27  or selSNr == 2 and subject_nr == 28')
df_Binding_Task_1 = df_Binding_Task_1.reset_index(drop=True)
df_Binding_Task_2 = df_Binding_Task.query('selSNr == 2 and 1 <= subject_nr <= 5 or selSNr == 1 and 6 <= subject_nr <= 10 or selSNr == 4 and 11 <= subject_nr <= 15 or selSNr == 3 and 16 <= subject_nr <= 20 or selSNr == 2 and subject_nr == 21 or selSNr == 1 and subject_nr == 22 or selSNr == 4 and subject_nr == 23 or selSNr == 3 and subject_nr == 24 or selSNr == 2 and subject_nr == 25 or selSNr == 1 and subject_nr == 26 or selSNr == 4 and subject_nr == 27  or selSNr == 3 and subject_nr == 28')
df_Binding_Task_2 = df_Binding_Task_2.reset_index(drop=True)
df_Binding_Task_3 = df_Binding_Task.query('selSNr == 3 and 1 <= subject_nr <= 5 or selSNr == 2 and 6 <= subject_nr <= 10 or selSNr == 1 and 11 <= subject_nr <= 15 or selSNr == 4 and 16 <= subject_nr <= 20 or selSNr == 3 and subject_nr == 21 or selSNr == 2 and subject_nr == 22 or selSNr == 1 and subject_nr == 23 or selSNr == 4 and subject_nr == 24 or selSNr == 3 and subject_nr == 25 or selSNr == 2 and subject_nr == 26 or selSNr == 1 and subject_nr == 27  or selSNr == 4 and subject_nr == 28')
df_Binding_Task_3 = df_Binding_Task_3.reset_index(drop=True)
df_Binding_Task_4 = df_Binding_Task.query('selSNr == 4 and 1 <= subject_nr <= 5 or selSNr == 3 and 6 <= subject_nr <= 10 or selSNr == 2 and 11 <= subject_nr <= 15 or selSNr == 1 and 16 <= subject_nr <= 20 or selSNr == 4 and subject_nr == 21 or selSNr == 3 and subject_nr == 22 or selSNr == 2 and subject_nr == 23 or selSNr == 1 and subject_nr == 24 or selSNr == 4 and subject_nr == 25 or selSNr == 3 and subject_nr == 26 or selSNr == 2 and subject_nr == 27  or selSNr == 1 and subject_nr == 28')
df_Binding_Task_4 = df_Binding_Task_4.reset_index(drop=True)

df_Operation_Span = df_total_part[df_total_part['Task_Name'] == 'Operation Span']
df_Operation_Span = df_Operation_Span.sort_values(by=['selSNr'], kind='mergesort')
df_Operation_Span = df_Operation_Span.sort_values(by=['subject_nr'], kind='mergesort')
df_Operation_Span_1 = df_Operation_Span.query('selSNr == 1 and 1 <= subject_nr <= 5 or selSNr == 4 and 6 <= subject_nr <= 10 or selSNr == 3 and 11 <= subject_nr <= 15 or selSNr == 2 and 16 <= subject_nr <= 20 or selSNr == 1 and subject_nr == 21 or selSNr == 4 and subject_nr == 22 or selSNr == 3 and subject_nr == 23 or selSNr == 2 and subject_nr == 24 or selSNr == 1 and subject_nr == 25 or selSNr == 4 and subject_nr == 26 or selSNr == 3 and subject_nr == 27  or selSNr == 2 and subject_nr == 28')
df_Operation_Span_1 = df_Operation_Span_1.reset_index(drop=True)
df_Operation_Span_2 = df_Operation_Span.query('selSNr == 2 and 1 <= subject_nr <= 5 or selSNr == 1 and 6 <= subject_nr <= 10 or selSNr == 4 and 11 <= subject_nr <= 15 or selSNr == 3 and 16 <= subject_nr <= 20 or selSNr == 2 and subject_nr == 21 or selSNr == 1 and subject_nr == 22 or selSNr == 4 and subject_nr == 23 or selSNr == 3 and subject_nr == 24 or selSNr == 2 and subject_nr == 25 or selSNr == 1 and subject_nr == 26 or selSNr == 4 and subject_nr == 27  or selSNr == 3 and subject_nr == 28')
df_Operation_Span_2 = df_Operation_Span_2.reset_index(drop=True)
df_Operation_Span_3 = df_Operation_Span.query('selSNr == 3 and 1 <= subject_nr <= 5 or selSNr == 2 and 6 <= subject_nr <= 10 or selSNr == 1 and 11 <= subject_nr <= 15 or selSNr == 4 and 16 <= subject_nr <= 20 or selSNr == 3 and subject_nr == 21 or selSNr == 2 and subject_nr == 22 or selSNr == 1 and subject_nr == 23 or selSNr == 4 and subject_nr == 24 or selSNr == 3 and subject_nr == 25 or selSNr == 2 and subject_nr == 26 or selSNr == 1 and subject_nr == 27  or selSNr == 4 and subject_nr == 28')
df_Operation_Span_3 = df_Operation_Span_3.reset_index(drop=True)
df_Operation_Span_4 = df_Operation_Span.query('selSNr == 4 and 1 <= subject_nr <= 5 or selSNr == 3 and 6 <= subject_nr <= 10 or selSNr == 2 and 11 <= subject_nr <= 15 or selSNr == 1 and 16 <= subject_nr <= 20 or selSNr == 4 and subject_nr == 21 or selSNr == 3 and subject_nr == 22 or selSNr == 2 and subject_nr == 23 or selSNr == 1 and subject_nr == 24 or selSNr == 4 and subject_nr == 25 or selSNr == 3 and subject_nr == 26 or selSNr == 2 and subject_nr == 27  or selSNr == 1 and subject_nr == 28')
df_Operation_Span_4 = df_Operation_Span_4.reset_index(drop=True)

df_raw_scores = pd.DataFrame()

subj_nr = df_total_part["subject_nr"].unique()
df_raw_scores.insert(0,'subject_nr',subj_nr)
########################################################################################################

Temperature = pd.read_excel(r'C:\Users\fabio\OneDrive\Área de Trabalho\RPubs\Article 3\Temperature\Body_Temperature_Collection.xlsx',sheet_name='TempExperimental')
Temperature.drop(columns="Subject ID", inplace=True)

df_raw_scores["Temperature (°C) Sess 09h00"] = list(Temperature["Temperature (°C) Sess 09h00"])
df_raw_scores["Temperature (°C) Sess 13h00"] = list(Temperature["Temperature (°C) Sess 13h00"])
df_raw_scores["Temperature (°C) Sess 17h00"] = list(Temperature["Temperature (°C) Sess 17h00"])
df_raw_scores["Temperature (°C) Sess 21h00"] = list(Temperature["Temperature (°C) Sess 21h00"])

#######################################################################################################

RawRS1 = list(df_Reading_Span_1.groupby(['subject_nr'], sort=True)['score_reading_span'].max() * 20)
df_raw_scores["Reading Span Session 09h00"] = RawRS1

RawRS2 = list(df_Reading_Span_2.groupby(['subject_nr'], sort=True)['score_reading_span'].max() * 20)
df_raw_scores["Reading Span Session 13h00"] = RawRS2

RawRS3 = list(df_Reading_Span_3.groupby(['subject_nr'], sort=True)['score_reading_span'].max() * 20)
df_raw_scores["Reading Span Session 17h00"] = RawRS3

RawRS4 = list(df_Reading_Span_4.groupby(['subject_nr'], sort=True)['score_reading_span'].max() * 20)
df_raw_scores["Reading Span Session 21h00"] = RawRS4

########################################################################################################

RawUT1 = list(df_WMU_Task_1.groupby(['subject_nr'], sort=True)['WMUExperimentalScore'].max())
df_raw_scores["Updating Task Session 09h00"] = RawUT1

RawUT2 = list(df_WMU_Task_2.groupby(['subject_nr'], sort=True)['WMUExperimentalScore'].max())
df_raw_scores["Updating Task Session 13h00"] = RawUT2

RawUT3 = list(df_WMU_Task_3.groupby(['subject_nr'], sort=True)['WMUExperimentalScore'].max())
df_raw_scores["Updating Task Session 17h00"] = RawUT3

RawUT4 = list(df_WMU_Task_4.groupby(['subject_nr'], sort=True)['WMUExperimentalScore'].max())
df_raw_scores["Updating Task Session 21h00"] = RawUT4

########################################################################################################

RawSS1 = list(df_Symmetry_Span_1.groupby(['subject_nr'], sort=True)['score_symmetry_span'].max() * 20)
df_raw_scores["Symmetry Span Session 09h00"] = RawSS1

RawSS2 = list(df_Symmetry_Span_2.groupby(['subject_nr'], sort=True)['score_symmetry_span'].max() * 20)
df_raw_scores["Symmetry Span Session 13h00"] = RawSS2

RawSS3 = list(df_Symmetry_Span_3.groupby(['subject_nr'], sort=True)['score_symmetry_span'].max() * 20)
df_raw_scores["Symmetry Span Session 17h00"] = RawSS3

RawSS4 = list(df_Symmetry_Span_4.groupby(['subject_nr'], sort=True)['score_symmetry_span'].max() * 20)
df_raw_scores["Symmetry Span Session 21h00"] = RawSS4

########################################################################################################
RawBT1 = list(df_Binding_Task_1.groupby(['subject_nr'], sort=True)['BindingRawScore'].max())
df_raw_scores["Binding Task Session 09h00"] = RawBT1

RawBT2 = list(df_Binding_Task_2.groupby(['subject_nr'], sort=True)['BindingRawScore'].max())
df_raw_scores["Binding Task Session 13h00"] = RawBT2

RawBT3 = list(df_Binding_Task_3.groupby(['subject_nr'], sort=True)['BindingRawScore'].max())
df_raw_scores["Binding Task Session 17h00"] = RawBT3

RawBT4 = list(df_Binding_Task_4.groupby(['subject_nr'], sort=True)['BindingRawScore'].max())
df_raw_scores["Binding Task Session 21h00"] = RawBT4

########################################################################################################
RawOS1 = list(df_Operation_Span_1.groupby(['subject_nr'], sort=True)['score_operation_span'].max() * 20)
df_raw_scores["Operation Span Session 09h00"] = RawOS1

RawOS2 = list(df_Operation_Span_2.groupby(['subject_nr'], sort=True)['score_operation_span'].max() * 20)
df_raw_scores["Operation Span Session 13h00"] = RawOS2

RawOS3 = list(df_Operation_Span_3.groupby(['subject_nr'], sort=True)['score_operation_span'].max() * 20)
df_raw_scores["Operation Span Session 17h00"] = RawOS3

RawOS4 = list(df_Operation_Span_4.groupby(['subject_nr'], sort=True)['score_operation_span'].max() * 20)
df_raw_scores["Operation Span Session 21h00"] = RawOS4

list_counterbalancing = []
for i in range(0,len(df_raw_scores)):
    if 1 <= df_raw_scores.loc[i,'subject_nr'] <= 5 or df_raw_scores.loc[i,'subject_nr'] == 21 or df_raw_scores.loc[i,'subject_nr'] == 25:
        aaa = '09h00,13h00,17h00,21h00'
        list_counterbalancing.append(aaa)
    elif 6 <= df_raw_scores.loc[i,'subject_nr'] <= 10 or df_raw_scores.loc[i,'subject_nr'] == 22 or df_raw_scores.loc[i,'subject_nr'] == 26:
        aaa = '13h00,17h00,21h00,09h00'
        list_counterbalancing.append(aaa)
    elif 11 <= df_raw_scores.loc[i,'subject_nr'] <= 15 or df_raw_scores.loc[i,'subject_nr'] == 23  or df_raw_scores.loc[i,'subject_nr'] == 27:
        aaa = '17h00,21h00,09h00,13h00'
        list_counterbalancing.append(aaa)
    elif 16 <= df_raw_scores.loc[i,'subject_nr'] <= 20 or df_raw_scores.loc[i,'subject_nr'] == 24  or df_raw_scores.loc[i,'subject_nr'] == 28:
        aaa = '21h00,09h00,13h00,17h00'
        list_counterbalancing.append(aaa)

df_raw_scores.insert(1, 'Counterbalancing', list_counterbalancing)

#print(df_raw_scores.to_string())
avg_RS_list = []
avg_UT_list = []
avg_SS_list = []
avg_BT_list = []
avg_OS_list = []
for i in range(0,len(df_raw_scores)):
    temp_avg_RS = (df_raw_scores.loc[i,"Reading Span Session 09h00"] + df_raw_scores.loc[i,"Reading Span Session 13h00"] + df_raw_scores.loc[i,"Reading Span Session 17h00"] + df_raw_scores.loc[i,"Reading Span Session 21h00"]) / 4
    avg_RS_list.append(temp_avg_RS)
    temp_avg_UT = (df_raw_scores.loc[i,"Updating Task Session 09h00"] + df_raw_scores.loc[i,"Updating Task Session 13h00"] + df_raw_scores.loc[i,"Updating Task Session 17h00"] + df_raw_scores.loc[i,"Updating Task Session 21h00"]) / 4
    avg_UT_list.append(temp_avg_UT)
    temp_avg_SS = (df_raw_scores.loc[i,"Symmetry Span Session 09h00"] + df_raw_scores.loc[i,"Symmetry Span Session 13h00"] + df_raw_scores.loc[i,"Symmetry Span Session 17h00"] + df_raw_scores.loc[i,"Symmetry Span Session 21h00"]) / 4
    avg_SS_list.append(temp_avg_SS)
    temp_avg_BT = (df_raw_scores.loc[i,"Binding Task Session 09h00"] + df_raw_scores.loc[i,"Binding Task Session 13h00"] + df_raw_scores.loc[i,"Binding Task Session 17h00"] + df_raw_scores.loc[i,"Binding Task Session 21h00"]) / 4
    avg_BT_list.append(temp_avg_BT)
    temp_avg_OS = (df_raw_scores.loc[i,"Operation Span Session 09h00"] + df_raw_scores.loc[i,"Operation Span Session 13h00"] + df_raw_scores.loc[i,"Operation Span Session 17h00"] + df_raw_scores.loc[i,"Operation Span Session 21h00"]) / 4
    avg_OS_list.append(temp_avg_OS)

for i in range(0,len(avg_RS_list)):
    avg_RS_list[i] = round(avg_RS_list[i]/20,2)
for i in range(0,len(avg_UT_list)):
    avg_UT_list[i] = round(avg_UT_list[i]/36,2)
for i in range(0,len(avg_SS_list)):
    avg_SS_list[i] = round(avg_SS_list[i]/20,2)
for i in range(0,len(avg_BT_list)):
    avg_BT_list[i] = round(avg_BT_list[i]/12,2)
for i in range(0,len(avg_OS_list)):
    avg_OS_list[i] = round(avg_OS_list[i]/20,2)

df_incl_exc = pd.DataFrame()
df_incl_exc["Subject Nr"] = subj_nr


########################################################################################################################################
######Criação da DataFrame com os valores normalizados obtidos por cada participante em cada uma das provas em que realizaram (e com os
#####dados socio-demografcos).
df_normalized_scores = df_raw_scores.copy(deep=True)

df_normalized_scores["Reading Span Session 09h00"] = df_normalized_scores["Reading Span Session 09h00"]/20
df_normalized_scores["Reading Span Session 13h00"] = df_normalized_scores["Reading Span Session 13h00"]/20
df_normalized_scores["Reading Span Session 17h00"] = df_normalized_scores["Reading Span Session 17h00"]/20
df_normalized_scores["Reading Span Session 21h00"] = df_normalized_scores["Reading Span Session 21h00"]/20
df_normalized_scores["Updating Task Session 09h00"] = df_normalized_scores["Updating Task Session 09h00"] / 36
df_normalized_scores["Updating Task Session 13h00"] = df_normalized_scores["Updating Task Session 13h00"] / 36
df_normalized_scores["Updating Task Session 17h00"] = df_normalized_scores["Updating Task Session 17h00"] / 36
df_normalized_scores["Updating Task Session 21h00"] = df_normalized_scores["Updating Task Session 21h00"] / 36
df_normalized_scores["Symmetry Span Session 09h00"] = df_normalized_scores["Symmetry Span Session 09h00"] / 20
df_normalized_scores["Symmetry Span Session 13h00"] = df_normalized_scores["Symmetry Span Session 13h00"] / 20
df_normalized_scores["Symmetry Span Session 17h00"] = df_normalized_scores["Symmetry Span Session 17h00"] / 20
df_normalized_scores["Symmetry Span Session 21h00"] = df_normalized_scores["Symmetry Span Session 21h00"] / 20
df_normalized_scores["Binding Task Session 09h00"] = df_normalized_scores["Binding Task Session 09h00"] / 12
df_normalized_scores["Binding Task Session 13h00"] = df_normalized_scores["Binding Task Session 13h00"] / 12
df_normalized_scores["Binding Task Session 17h00"] = df_normalized_scores["Binding Task Session 17h00"] / 12
df_normalized_scores["Binding Task Session 21h00"] = df_normalized_scores["Binding Task Session 21h00"] / 12
df_normalized_scores["Operation Span Session 09h00"] = df_normalized_scores["Operation Span Session 09h00"] / 20
df_normalized_scores["Operation Span Session 13h00"] = df_normalized_scores["Operation Span Session 13h00"] / 20
df_normalized_scores["Operation Span Session 17h00"] = df_normalized_scores["Operation Span Session 17h00"] / 20
df_normalized_scores["Operation Span Session 21h00"] = df_normalized_scores["Operation Span Session 21h00"] / 20

#print(df_normalized_scores.to_string())
########################################################################################################
#Os próximos 5 blocos de código selecionam as colunas com informação relevante de cada WM task e guardam estas colunas em DataFrames
#que só contêm informação relacionada com a mesma tarefa. Para além disso, estes nestes 5 blocos de código, são realizadas algumas
#conversões no formato dos dados (e.g., string to float) e são alterados os nomes de algumas colunas de forma a ficarem mais percétiveis.
#'selSNr',
df_Reading_Span_1 = df_Reading_Span_1[
    ['subject_nr',  'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName', 'acc', 'avg_rt',
     'BlockChoice', 'correct', 'correct_response', 'Frase', 'height', 'letter', 'List_Prev_Letter',
     'List_responses_memory', 'live_row', 'logfile', 'response_average_time_memory', 'response_memory',
     'response_processing', 'response_time_memory', 'response_time_processing', 'response_total_time_memory',
     'RP_part_process_time', 'score_practice', 'score_reading_span', 'score_subblock_2', 'score_subblock_3', 'score_subblock_4',
     'score_subblock_5', 'score_subblock_6', 'Tipo', 'total_correct',
     'total_response_time', 'total_responses', 'width']]
df_Reading_Span_1[['acc', 'avg_rt']] = df_Reading_Span_1[['acc', 'avg_rt']].replace(',', '.')
df_Reading_Span_1 = df_Reading_Span_1.astype(
    {'acc': 'float64', 'avg_rt': 'float64', 'correct_response': 'str', 'response_processing': 'str'})
example_b = df_Reading_Span_1["response_processing"].iloc[2]
df_Reading_Span_1 = df_Reading_Span_1.replace(example_b, '')
#df_Reading_Span_1 = df_Reading_Span_1.sort_values(by=['selSNr'], kind='mergesort')
#df_Reading_Span_1 = df_Reading_Span_1.sort_values(by=['subject_nr'], kind='mergesort')
df_Reading_Span_1.columns = ['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco',
                             'SubTaskName','acc_Sess09h00','avg_rt_Sess09h00','BlockChoice_Sess09h00','correct_Sess09h00','correct_response_Sess09h00',
                             'Frase_Sess09h00','height_Sess09h00','letter_Sess09h00','List_Prev_Letter_Sess09h00','List_responses_memory_Sess09h00',
                             'live_row_Sess09h00','logfile_Sess09h00','response_average_time_memory_Sess09h00','response_memory_Sess09h00',
                             'response_processing_Sess09h00','response_time_memory_Sess09h00','response_time_processing_Sess09h00',
                             'response_total_time_memory_Sess09h00','RP_part_process_time_Sess09h00','score_practice_Sess09h00',
                             'score_reading_span_Sess09h00','score_subblock_2_Sess09h00','score_subblock_3_Sess09h00','score_subblock_4_Sess09h00',
                             'score_subblock_5_Sess09h00','score_subblock_6_Sess09h00','Tipo_Sess09h00','total_correct_Sess09h00',
                             'total_response_time_Sess09h00','total_responses_Sess09h00','width_Sess09h00']
#'selSNr',
df_Reading_Span_2 = df_Reading_Span_2[
    ['subject_nr',  'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName', 'acc', 'avg_rt',
     'BlockChoice', 'correct', 'correct_response', 'Frase', 'height', 'letter', 'List_Prev_Letter',
     'List_responses_memory', 'live_row', 'logfile', 'response_average_time_memory', 'response_memory',
     'response_processing', 'response_time_memory', 'response_time_processing', 'response_total_time_memory',
     'RP_part_process_time', 'score_practice', 'score_reading_span', 'score_subblock_2', 'score_subblock_3', 'score_subblock_4',
     'score_subblock_5', 'score_subblock_6', 'Tipo', 'total_correct',
     'total_response_time', 'total_responses', 'width']]
df_Reading_Span_2[['acc', 'avg_rt']] = df_Reading_Span_2[['acc', 'avg_rt']].replace(',', '.')
df_Reading_Span_2 = df_Reading_Span_2.astype(
    {'acc': 'float64', 'avg_rt': 'float64', 'correct_response': 'str', 'response_processing': 'str'})
example_b = df_Reading_Span_2["response_processing"].iloc[2]
df_Reading_Span_2 = df_Reading_Span_2.replace(example_b, '')
df_Reading_Span_2.drop(['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco','SubTaskName'],axis=1,inplace=True)
#df_Reading_Span_2 = df_Reading_Span_2.sort_values(by=['selSNr'], kind='mergesort')
#df_Reading_Span_2 = df_Reading_Span_2.sort_values(by=['subject_nr'], kind='mergesort')
df_Reading_Span_2.columns = ['acc_Sess13h00','avg_rt_Sess13h00','BlockChoice_Sess13h00','correct_Sess13h00','correct_response_Sess13h00',
                             'Frase_Sess13h00','height_Sess13h00','letter_Sess13h00','List_Prev_Letter_Sess13h00','List_responses_memory_Sess13h00',
                             'live_row_Sess13h00','logfile_Sess13h00','response_average_time_memory_Sess13h00','response_memory_Sess13h00',
                             'response_processing_Sess13h00','response_time_memory_Sess13h00','response_time_processing_Sess13h00',
                             'response_total_time_memory_Sess13h00','RP_part_process_time_Sess13h00','score_practice_Sess13h00',
                             'score_reading_span_Sess13h00','score_subblock_2_Sess13h00','score_subblock_3_Sess13h00','score_subblock_4_Sess13h00',
                             'score_subblock_5_Sess13h00','score_subblock_6_Sess13h00','Tipo_Sess13h00','total_correct_Sess13h00',
                             'total_response_time_Sess13h00','total_responses_Sess13h00','width_Sess13h00']

#'selSNr',
df_Reading_Span_3 = df_Reading_Span_3[
    ['subject_nr',  'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName', 'acc', 'avg_rt',
     'BlockChoice', 'correct', 'correct_response', 'Frase', 'height', 'letter', 'List_Prev_Letter',
     'List_responses_memory', 'live_row', 'logfile', 'response_average_time_memory', 'response_memory',
     'response_processing', 'response_time_memory', 'response_time_processing', 'response_total_time_memory',
     'RP_part_process_time', 'score_practice', 'score_reading_span', 'score_subblock_2', 'score_subblock_3', 'score_subblock_4',
     'score_subblock_5', 'score_subblock_6', 'Tipo', 'total_correct',
     'total_response_time', 'total_responses', 'width']]
df_Reading_Span_3[['acc', 'avg_rt']] = df_Reading_Span_3[['acc', 'avg_rt']].replace(',', '.')
df_Reading_Span_3 = df_Reading_Span_3.astype(
    {'acc': 'float64', 'avg_rt': 'float64', 'correct_response': 'str', 'response_processing': 'str'})
example_b = df_Reading_Span_3["response_processing"].iloc[2]
df_Reading_Span_3 = df_Reading_Span_3.replace(example_b, '')
#df_Reading_Span_3 = df_Reading_Span_3.sort_values(by=['selSNr'], kind='mergesort')
#df_Reading_Span_3 = df_Reading_Span_3.sort_values(by=['subject_nr'], kind='mergesort')
df_Reading_Span_3.drop(['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco','SubTaskName'],axis=1,inplace=True)
df_Reading_Span_3.columns = ['acc_Sess17h00','avg_rt_Sess17h00','BlockChoice_Sess17h00','correct_Sess17h00','correct_response_Sess17h00',
                             'Frase_Sess17h00','height_Sess17h00','letter_Sess17h00','List_Prev_Letter_Sess17h00','List_responses_memory_Sess17h00',
                             'live_row_Sess17h00','logfile_Sess17h00','response_average_time_memory_Sess17h00','response_memory_Sess17h00',
                             'response_processing_Sess17h00','response_time_memory_Sess17h00','response_time_processing_Sess17h00',
                             'response_total_time_memory_Sess17h00','RP_part_process_time_Sess17h00','score_practice_Sess17h00',
                             'score_reading_span_Sess17h00','score_subblock_2_Sess17h00','score_subblock_3_Sess17h00','score_subblock_4_Sess17h00',
                             'score_subblock_5_Sess17h00','score_subblock_6_Sess17h00','Tipo_Sess17h00','total_correct_Sess17h00',
                             'total_response_time_Sess17h00','total_responses_Sess17h00','width_Sess17h00']
#'selSNr',
df_Reading_Span_4 = df_Reading_Span_4[
    ['subject_nr',  'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName', 'acc', 'avg_rt',
     'BlockChoice', 'correct', 'correct_response', 'Frase', 'height', 'letter', 'List_Prev_Letter',
     'List_responses_memory', 'live_row', 'logfile', 'response_average_time_memory', 'response_memory',
     'response_processing', 'response_time_memory', 'response_time_processing', 'response_total_time_memory',
     'RP_part_process_time', 'score_practice', 'score_reading_span', 'score_subblock_2', 'score_subblock_3', 'score_subblock_4',
     'score_subblock_5', 'score_subblock_6', 'Tipo', 'total_correct',
     'total_response_time', 'total_responses', 'width']]
df_Reading_Span_4[['acc', 'avg_rt']] = df_Reading_Span_4[['acc', 'avg_rt']].replace(',', '.')
df_Reading_Span_4 = df_Reading_Span_4.astype(
    {'acc': 'float64', 'avg_rt': 'float64', 'correct_response': 'str', 'response_processing': 'str'})
example_b = df_Reading_Span_4["response_processing"].iloc[2]
df_Reading_Span_4 = df_Reading_Span_4.replace(example_b, '')
#df_Reading_Span_4 = df_Reading_Span_4.sort_values(by=['selSNr'], kind='mergesort')
#df_Reading_Span_4 = df_Reading_Span_4.sort_values(by=['subject_nr'], kind='mergesort')
df_Reading_Span_4.drop(['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco','SubTaskName'],axis=1,inplace=True)
df_Reading_Span_4.columns = ['acc_Sess21h00','avg_rt_Sess21h00','BlockChoice_Sess21h00','correct_Sess21h00','correct_response_Sess21h00',
                             'Frase_Sess21h00','height_Sess21h00','letter_Sess21h00','List_Prev_Letter_Sess21h00','List_responses_memory_Sess21h00',
                             'live_row_Sess21h00','logfile_Sess21h00','response_average_time_memory_Sess21h00','response_memory_Sess21h00',
                             'response_processing_Sess21h00','response_time_memory_Sess21h00','response_time_processing_Sess21h00',
                             'response_total_time_memory_Sess21h00','RP_part_process_time_Sess21h00','score_practice_Sess21h00',
                             'score_reading_span_Sess21h00','score_subblock_2_Sess21h00','score_subblock_3_Sess21h00','score_subblock_4_Sess21h00',
                             'score_subblock_5_Sess21h00','score_subblock_6_Sess21h00','Tipo_Sess21h00','total_correct_Sess21h00',
                             'total_response_time_Sess21h00','total_responses_Sess21h00','width_Sess21h00']

#'selSNr',

#print(df_Reading_Span_2.to_string())
df_Reading_Span_Final = pd.concat([df_Reading_Span_1,df_Reading_Span_2,df_Reading_Span_3,df_Reading_Span_4],axis=1)

df_Reading_Span_Final = df_Reading_Span_Final[['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco','SubTaskName','acc_Sess09h00',
                                                   'acc_Sess13h00','acc_Sess17h00','acc_Sess21h00','avg_rt_Sess09h00','avg_rt_Sess13h00','avg_rt_Sess17h00','avg_rt_Sess21h00',
                                                   'BlockChoice_Sess09h00','BlockChoice_Sess13h00','BlockChoice_Sess17h00','BlockChoice_Sess21h00','correct_Sess09h00',
                                                   'correct_Sess13h00','correct_Sess17h00','correct_Sess21h00','correct_response_Sess09h00','correct_response_Sess13h00',
                                                   'correct_response_Sess17h00','correct_response_Sess21h00','Frase_Sess09h00','Frase_Sess13h00','Frase_Sess17h00','Frase_Sess21h00',
                                                   'height_Sess09h00','height_Sess13h00','height_Sess17h00','height_Sess21h00','letter_Sess09h00','letter_Sess13h00','letter_Sess17h00',
                                                   'letter_Sess21h00','List_Prev_Letter_Sess09h00','List_Prev_Letter_Sess13h00','List_Prev_Letter_Sess17h00',
                                                   'List_Prev_Letter_Sess21h00','List_responses_memory_Sess09h00','List_responses_memory_Sess13h00',
                                                   'List_responses_memory_Sess17h00','List_responses_memory_Sess21h00','live_row_Sess09h00','live_row_Sess13h00',
                                                   'live_row_Sess17h00','live_row_Sess21h00','logfile_Sess09h00','logfile_Sess13h00','logfile_Sess17h00','logfile_Sess21h00',
                                                   'response_average_time_memory_Sess09h00','response_average_time_memory_Sess13h00','response_average_time_memory_Sess17h00',
                                                   'response_average_time_memory_Sess21h00','response_memory_Sess09h00','response_memory_Sess13h00','response_memory_Sess17h00',
                                                   'response_memory_Sess21h00','response_processing_Sess09h00','response_processing_Sess13h00','response_processing_Sess17h00',
                                                   'response_processing_Sess21h00','response_time_memory_Sess09h00','response_time_memory_Sess13h00',
                                                   'response_time_memory_Sess17h00','response_time_memory_Sess21h00','response_time_processing_Sess09h00',
                                                   'response_time_processing_Sess13h00','response_time_processing_Sess17h00','response_time_processing_Sess21h00',
                                                   'response_total_time_memory_Sess09h00','response_total_time_memory_Sess13h00','response_total_time_memory_Sess17h00',
                                                   'response_total_time_memory_Sess21h00','RP_part_process_time_Sess09h00','RP_part_process_time_Sess13h00',
                                                   'RP_part_process_time_Sess17h00','RP_part_process_time_Sess21h00','score_practice_Sess09h00',
                                                   'score_practice_Sess13h00','score_practice_Sess17h00','score_practice_Sess21h00','score_reading_span_Sess09h00',
                                                   'score_reading_span_Sess13h00','score_reading_span_Sess17h00','score_reading_span_Sess21h00','score_subblock_2_Sess09h00',
                                                   'score_subblock_2_Sess13h00','score_subblock_2_Sess17h00','score_subblock_2_Sess21h00','score_subblock_3_Sess09h00',
                                                   'score_subblock_3_Sess13h00','score_subblock_3_Sess17h00','score_subblock_3_Sess21h00','score_subblock_4_Sess09h00',
                                                   'score_subblock_4_Sess13h00','score_subblock_4_Sess17h00','score_subblock_4_Sess21h00','score_subblock_5_Sess09h00',
                                                   'score_subblock_5_Sess13h00','score_subblock_5_Sess17h00','score_subblock_5_Sess21h00','score_subblock_6_Sess09h00',
                                                   'score_subblock_6_Sess13h00','score_subblock_6_Sess17h00','score_subblock_6_Sess21h00','Tipo_Sess09h00','Tipo_Sess13h00',
                                                   'Tipo_Sess17h00','Tipo_Sess21h00','total_correct_Sess09h00','total_correct_Sess13h00','total_correct_Sess17h00',
                                                   'total_correct_Sess21h00','total_response_time_Sess09h00','total_response_time_Sess13h00','total_response_time_Sess17h00',
                                                   'total_response_time_Sess21h00','total_responses_Sess09h00','total_responses_Sess13h00','total_responses_Sess17h00',
                                                   'total_responses_Sess21h00','width_Sess09h00','width_Sess13h00','width_Sess17h00','width_Sess21h00']]

############################################################################################
############################################################################################
#'toUpdate1_1', 'toUpdate1_2', 'toUpdate1_3', 'toUpdate2_1', 'toUpdate2_2','toUpdate2_3','correct_response1', 'correct_response2', 'correct_response3',
#'selSNr',
df_WMU_Task_1 = df_WMU_Task_1[
    ['subject_nr',  'CB_ref', 'practice', 'TrialNumber', 'correct1', 'correct2', 'correct3', 'digit1', 'digit2', 'digit3', 'height',
     'Index_List', 'live_row', 'logfile', 'response1', 'response2', 'response3', 'response_time1', 'responseavgRT',
     'total_correct_trial', 'TotalRtBlock',  'WMUExperimentalScore', 'WMUPracticeScore', 'width']]
df_WMU_Task_1 = df_WMU_Task_1.rename(columns={'response_time1': 'response_time'})
#df_WMU_Task_1 = df_WMU_Task_1.sort_values(by=['selSNr'], kind='mergesort')
#df_WMU_Task_1 = df_WMU_Task_1.sort_values(by=['subject_nr'], kind='mergesort')
for i in range(0, len(df_WMU_Task_1['responseavgRT'])):
    if df_WMU_Task_1['responseavgRT'].iloc[i] == 0:
        df_WMU_Task_1['responseavgRT'].iloc[i] = ''
df_WMU_Task_1.columns = ['subject_nr','CB_ref','practice','TrialNumber','correct1_Sess09h00',
                         'correct2_Sess09h00','correct3_Sess09h00','digit1_Sess09h00','digit2_Sess09h00','digit3_Sess09h00','height_Sess09h00',
                         'Index_List_Sess09h00','live_row_Sess09h00','logfile_Sess09h00','response1_Sess09h00','response2_Sess09h00','response3_Sess09h00',
                         'response_time1_Sess09h00','responseavgRT_Sess09h00','total_correct_trial_Sess09h00','TotalRtBlock_Sess09h00',
                         'WMUExperimentalScore_Sess09h00','WMUPracticeScore_Sess09h00','width_Sess09h00']

#WMU_cast_lis = ['toUpdate1_1', 'toUpdate1_2', 'toUpdate1_3', 'toUpdate2_1', 'toUpdate2_2', 'toUpdate2_3']
#for i in WMU_cast_lis:
#    for j in range(0, len(df_WMU_Task[i])):
#        if df_WMU_Task[i].iloc[j] > 0:
#            df_WMU_Task[i].iloc[j] = '+' + str(int(df_WMU_Task[i].iloc[j]))
#        else:
#            df_WMU_Task[i].iloc[j] = str(int(df_WMU_Task[i].iloc[j]))

#'selSNr',
df_WMU_Task_2 = df_WMU_Task_2[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'correct1', 'correct2', 'correct3', 'digit1', 'digit2', 'digit3', 'height',
     'Index_List', 'live_row', 'logfile', 'response1', 'response2', 'response3', 'response_time1', 'responseavgRT',
     'total_correct_trial', 'TotalRtBlock',  'WMUExperimentalScore', 'WMUPracticeScore', 'width']]
df_WMU_Task_2 = df_WMU_Task_2.rename(columns={'response_time1': 'response_time'})
#df_WMU_Task_2 = df_WMU_Task_2.sort_values(by=['selSNr'], kind='mergesort')
#df_WMU_Task_2 = df_WMU_Task_2.sort_values(by=['subject_nr'], kind='mergesort')
for i in range(0, len(df_WMU_Task_2['responseavgRT'])):
    if df_WMU_Task_2['responseavgRT'].iloc[i] == 0:
        df_WMU_Task_2['responseavgRT'].iloc[i] = ''
df_WMU_Task_2.drop(['subject_nr','CB_ref','practice','TrialNumber'],axis=1,inplace=True)
df_WMU_Task_2.columns = ['correct1_Sess13h00','correct2_Sess13h00','correct3_Sess13h00','digit1_Sess13h00','digit2_Sess13h00','digit3_Sess13h00','height_Sess13h00',
                         'Index_List_Sess13h00','live_row_Sess13h00','logfile_Sess13h00','response1_Sess13h00','response2_Sess13h00','response3_Sess13h00',
                         'response_time1_Sess13h00','responseavgRT_Sess13h00','total_correct_trial_Sess13h00','TotalRtBlock_Sess13h00',
                         'WMUExperimentalScore_Sess13h00','WMUPracticeScore_Sess13h00','width_Sess13h00']
#WMU_cast_lis = ['toUpdate1_1', 'toUpdate1_2', 'toUpdate1_3', 'toUpdate2_1', 'toUpdate2_2', 'toUpdate2_3']
#for i in WMU_cast_lis:
#    for j in range(0, len(df_WMU_Task[i])):
#        if df_WMU_Task[i].iloc[j] > 0:
#            df_WMU_Task[i].iloc[j] = '+' + str(int(df_WMU_Task[i].iloc[j]))
#        else:
#            df_WMU_Task[i].iloc[j] = str(int(df_WMU_Task[i].iloc[j]))

#'selSNr',
df_WMU_Task_3 = df_WMU_Task_3[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'correct1', 'correct2', 'correct3', 'digit1', 'digit2', 'digit3', 'height',
     'Index_List', 'live_row', 'logfile', 'response1', 'response2', 'response3', 'response_time1', 'responseavgRT',
     'total_correct_trial', 'TotalRtBlock',  'WMUExperimentalScore', 'WMUPracticeScore', 'width']]
df_WMU_Task_3 = df_WMU_Task_3.rename(columns={'response_time1': 'response_time'})
#df_WMU_Task_3 = df_WMU_Task_3.sort_values(by=['selSNr'], kind='mergesort')
#df_WMU_Task_3 = df_WMU_Task_3.sort_values(by=['subject_nr'], kind='mergesort')
for i in range(0, len(df_WMU_Task_3['responseavgRT'])):
    if df_WMU_Task_3['responseavgRT'].iloc[i] == 0:
        df_WMU_Task_3['responseavgRT'].iloc[i] = ''
df_WMU_Task_3.drop(['subject_nr','CB_ref','practice','TrialNumber'],axis=1,inplace=True)
df_WMU_Task_3.columns = ['correct1_Sess17h00','correct2_Sess17h00','correct3_Sess17h00','digit1_Sess17h00','digit2_Sess17h00','digit3_Sess17h00','height_Sess17h00',
                         'Index_List_Sess17h00','live_row_Sess17h00','logfile_Sess17h00','response1_Sess17h00','response2_Sess17h00','response3_Sess17h00',
                         'response_time1_Sess17h00','responseavgRT_Sess17h00','total_correct_trial_Sess17h00','TotalRtBlock_Sess17h00',
                         'WMUExperimentalScore_Sess17h00','WMUPracticeScore_Sess17h00','width_Sess17h00']
#WMU_cast_lis = ['toUpdate1_1', 'toUpdate1_2', 'toUpdate1_3', 'toUpdate2_1', 'toUpdate2_2', 'toUpdate2_3']
#for i in WMU_cast_lis:
#    for j in range(0, len(df_WMU_Task[i])):
#        if df_WMU_Task[i].iloc[j] > 0:
#            df_WMU_Task[i].iloc[j] = '+' + str(int(df_WMU_Task[i].iloc[j]))
#        else:
#            df_WMU_Task[i].iloc[j] = str(int(df_WMU_Task[i].iloc[j]))

#'selSNr',
df_WMU_Task_4 = df_WMU_Task_4[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'correct1', 'correct2', 'correct3', 'digit1', 'digit2', 'digit3', 'height',
     'Index_List', 'live_row', 'logfile', 'response1', 'response2', 'response3', 'response_time1', 'responseavgRT',
     'total_correct_trial', 'TotalRtBlock',  'WMUExperimentalScore', 'WMUPracticeScore', 'width']]
df_WMU_Task_4 = df_WMU_Task_4.rename(columns={'response_time1': 'response_time'})
#df_WMU_Task_4 = df_WMU_Task_4.sort_values(by=['selSNr'], kind='mergesort')
#df_WMU_Task_4 = df_WMU_Task_4.sort_values(by=['subject_nr'], kind='mergesort')
for i in range(0, len(df_WMU_Task_4['responseavgRT'])):
    if df_WMU_Task_4['responseavgRT'].iloc[i] == 0:
        df_WMU_Task_4['responseavgRT'].iloc[i] = ''
df_WMU_Task_4.drop(['subject_nr','CB_ref','practice','TrialNumber'],axis=1,inplace=True)
df_WMU_Task_4.columns = ['correct1_Sess21h00','correct2_Sess21h00','correct3_Sess21h00','digit1_Sess21h00','digit2_Sess21h00','digit3_Sess21h00','height_Sess21h00',
                         'Index_List_Sess21h00','live_row_Sess21h00','logfile_Sess21h00','response1_Sess21h00','response2_Sess21h00','response3_Sess21h00',
                         'response_time1_Sess21h00','responseavgRT_Sess21h00','total_correct_trial_Sess21h00','TotalRtBlock_Sess21h00',
                         'WMUExperimentalScore_Sess21h00','WMUPracticeScore_Sess21h00','width_Sess21h00']
#WMU_cast_lis = ['toUpdate1_1', 'toUpdate1_2', 'toUpdate1_3', 'toUpdate2_1', 'toUpdate2_2', 'toUpdate2_3']
#for i in WMU_cast_lis:
#    for j in range(0, len(df_WMU_Task[i])):
#        if df_WMU_Task[i].iloc[j] > 0:
#            df_WMU_Task[i].iloc[j] = '+' + str(int(df_WMU_Task[i].iloc[j]))
#        else:
#            df_WMU_Task[i].iloc[j] = str(int(df_WMU_Task[i].iloc[j]))

df_WMU_Task_Final = pd.concat([df_WMU_Task_1,df_WMU_Task_2,df_WMU_Task_3,df_WMU_Task_4],axis=1)

df_WMU_Task_Final = df_WMU_Task_Final[['subject_nr','CB_ref','practice','TrialNumber','correct1_Sess09h00','correct1_Sess13h00',
                                       'correct1_Sess17h00','correct1_Sess21h00','correct2_Sess09h00','correct2_Sess13h00','correct2_Sess17h00',
                                       'correct2_Sess21h00','correct3_Sess09h00','correct3_Sess13h00','correct3_Sess17h00','correct3_Sess21h00',
                                       'digit1_Sess09h00','digit1_Sess13h00','digit1_Sess17h00','digit1_Sess21h00','digit2_Sess09h00','digit2_Sess13h00',
                                       'digit2_Sess17h00','digit2_Sess21h00','digit3_Sess09h00','digit3_Sess13h00','digit3_Sess17h00','digit3_Sess21h00',
                                       'height_Sess09h00','height_Sess13h00','height_Sess17h00','height_Sess21h00','Index_List_Sess09h00',
                                       'Index_List_Sess13h00','Index_List_Sess17h00','Index_List_Sess21h00','live_row_Sess09h00','live_row_Sess13h00',
                                       'live_row_Sess17h00','live_row_Sess21h00','logfile_Sess09h00','logfile_Sess13h00','logfile_Sess17h00','logfile_Sess21h00',
                                       'response1_Sess09h00','response1_Sess13h00','response1_Sess17h00','response1_Sess21h00','response2_Sess09h00','response2_Sess13h00',
                                       'response2_Sess17h00','response2_Sess21h00','response3_Sess09h00','response3_Sess13h00','response3_Sess17h00','response3_Sess21h00',
                                       'response_time1_Sess09h00','response_time1_Sess13h00','response_time1_Sess17h00','response_time1_Sess21h00',
                                       'responseavgRT_Sess09h00','responseavgRT_Sess13h00','responseavgRT_Sess17h00','responseavgRT_Sess21h00',
                                       'total_correct_trial_Sess09h00','total_correct_trial_Sess13h00','total_correct_trial_Sess17h00','total_correct_trial_Sess21h00',
                                       'TotalRtBlock_Sess09h00','TotalRtBlock_Sess13h00','TotalRtBlock_Sess17h00','TotalRtBlock_Sess21h00',
                                       'WMUExperimentalScore_Sess09h00', 'WMUExperimentalScore_Sess13h00','WMUExperimentalScore_Sess17h00', 'WMUExperimentalScore_Sess21h00',
                                       'WMUPracticeScore_Sess09h00','WMUPracticeScore_Sess13h00','WMUPracticeScore_Sess17h00','WMUPracticeScore_Sess21h00',
                                       'width_Sess09h00','width_Sess13h00','width_Sess17h00','width_Sess21h00']]
############################################################################################
############################################################################################
#'selSNr',
df_Symmetry_Span_1 = df_Symmetry_Span_1[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName',
     'aggregated_score_memory', 'average_response_time_processing', 'average_total_time_memory', 'correct',
     'correct_response', 'countDys', 'countSym', 'height', 'LeftHalfPos', 'List_SS_button', 'List_SS_Pos', 'live_row',
     'logfile', 'maxDys', 'maxSym', 'pressed_buttons', 'response_memory', 'response_processing', 'response_time_memory',
     'response_time_processing', 'response_total_time_memory', 'response_total_time_memory_full_task', 'RightHalfPos',
     'SP_part_process_time', 'SS_practice_score', 'score_symmetry_span', 'score_subblock_2', 'score_subblock_3',
     'score_subblock_4', 'score_subblock_5', 'score_subblock_6', 'SymType',
     'total_correct_processing', 'total_response_time_processing', 'width']]
df_Symmetry_Span_1 = df_Symmetry_Span_1.astype({'correct_response': 'str', 'response_processing': 'str'})
example_d = df_Symmetry_Span_1["response_processing"].iloc[2]
df_Symmetry_Span_1 = df_Symmetry_Span_1.replace(example_d, '')
#df_Symmetry_Span_1 = df_Symmetry_Span_1.sort_values(by=['selSNr'], kind='mergesort')
#df_Symmetry_Span_1 = df_Symmetry_Span_1.sort_values(by=['subject_nr'], kind='mergesort')
df_Symmetry_Span_1.columns = ['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco',
                              'SubTaskName','aggregated_score_memory_Sess09h00','average_response_time_processing_Sess09h00',
                              'average_total_time_memory_Sess09h00','correct_Sess09h00','correct_response_Sess09h00','countDys_Sess09h00',
                              'countSym_Sess09h00','height_Sess09h00','LeftHalfPos_Sess09h00','List_SS_button_Sess09h00','List_SS_Pos_Sess09h00',
                              'live_row_Sess09h00','logfile_Sess09h00','maxDys_Sess09h00','maxSym_Sess09h00','pressed_buttons_Sess09h00',
                              'response_memory_Sess09h00','response_processing_Sess09h00','response_time_memory_Sess09h00',
                              'response_time_processing_Sess09h00','response_total_time_memory_Sess09h00',
                              'response_total_time_memory_full_task_Sess09h00','RightHalfPos_Sess09h00','SP_part_process_time_Sess09h00',
                              'SS_practice_score_Sess09h00','score_symmetry_span_Sess09h00','score_subblock_2_Sess09h00','score_subblock_3_Sess09h00',
                              'score_subblock_4_Sess09h00','score_subblock_5_Sess09h00','score_subblock_6_Sess09h00','SymType_Sess09h00',
                              'total_correct_processing_Sess09h00','total_response_time_processing_Sess09h00','width_Sess09h00']

#'selSNr',
df_Symmetry_Span_2 = df_Symmetry_Span_2[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName',
     'aggregated_score_memory', 'average_response_time_processing', 'average_total_time_memory', 'correct',
     'correct_response', 'countDys', 'countSym', 'height', 'LeftHalfPos', 'List_SS_button', 'List_SS_Pos', 'live_row',
     'logfile', 'maxDys', 'maxSym', 'pressed_buttons', 'response_memory', 'response_processing', 'response_time_memory',
     'response_time_processing', 'response_total_time_memory', 'response_total_time_memory_full_task', 'RightHalfPos',
     'SP_part_process_time', 'SS_practice_score', 'score_symmetry_span', 'score_subblock_2', 'score_subblock_3',
     'score_subblock_4', 'score_subblock_5', 'score_subblock_6', 'SymType',
     'total_correct_processing', 'total_response_time_processing', 'width']]
df_Symmetry_Span_2 = df_Symmetry_Span_2.astype({'correct_response': 'str', 'response_processing': 'str'})
example_d = df_Symmetry_Span_2["response_processing"].iloc[2]
df_Symmetry_Span_2 = df_Symmetry_Span_2.replace(example_d, '')
#df_Symmetry_Span_2 = df_Symmetry_Span_2.sort_values(by=['selSNr'], kind='mergesort')
#df_Symmetry_Span_2 = df_Symmetry_Span_2.sort_values(by=['subject_nr'], kind='mergesort')
df_Symmetry_Span_2.drop(['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco','SubTaskName'],axis=1,inplace=True)
df_Symmetry_Span_2.columns = ['aggregated_score_memory_Sess13h00','average_response_time_processing_Sess13h00',
                              'average_total_time_memory_Sess13h00','correct_Sess13h00','correct_response_Sess13h00','countDys_Sess13h00',
                              'countSym_Sess13h00','height_Sess13h00','LeftHalfPos_Sess13h00','List_SS_button_Sess13h00','List_SS_Pos_Sess13h00',
                              'live_row_Sess13h00','logfile_Sess13h00','maxDys_Sess13h00','maxSym_Sess13h00','pressed_buttons_Sess13h00',
                              'response_memory_Sess13h00','response_processing_Sess13h00','response_time_memory_Sess13h00',
                              'response_time_processing_Sess13h00','response_total_time_memory_Sess13h00',
                              'response_total_time_memory_full_task_Sess13h00','RightHalfPos_Sess13h00','SP_part_process_time_Sess13h00',
                              'SS_practice_score_Sess13h00','score_symmetry_span_Sess13h00','score_subblock_2_Sess13h00','score_subblock_3_Sess13h00',
                              'score_subblock_4_Sess13h00','score_subblock_5_Sess13h00','score_subblock_6_Sess13h00','SymType_Sess13h00',
                              'total_correct_processing_Sess13h00','total_response_time_processing_Sess13h00','width_Sess13h00']

#'selSNr',
df_Symmetry_Span_3 = df_Symmetry_Span_3[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName',
     'aggregated_score_memory', 'average_response_time_processing', 'average_total_time_memory', 'correct',
     'correct_response', 'countDys', 'countSym', 'height', 'LeftHalfPos', 'List_SS_button', 'List_SS_Pos', 'live_row',
     'logfile', 'maxDys', 'maxSym', 'pressed_buttons', 'response_memory', 'response_processing', 'response_time_memory',
     'response_time_processing', 'response_total_time_memory', 'response_total_time_memory_full_task', 'RightHalfPos',
     'SP_part_process_time', 'SS_practice_score', 'score_symmetry_span', 'score_subblock_2', 'score_subblock_3',
     'score_subblock_4', 'score_subblock_5', 'score_subblock_6', 'SymType',
     'total_correct_processing', 'total_response_time_processing', 'width']]
df_Symmetry_Span_3 = df_Symmetry_Span_3.astype({'correct_response': 'str', 'response_processing': 'str'})
example_d = df_Symmetry_Span_3["response_processing"].iloc[2]
df_Symmetry_Span_3 = df_Symmetry_Span_3.replace(example_d, '')
#df_Symmetry_Span_3 = df_Symmetry_Span_3.sort_values(by=['selSNr'], kind='mergesort')
#df_Symmetry_Span_3 = df_Symmetry_Span_3.sort_values(by=['subject_nr'], kind='mergesort')
df_Symmetry_Span_3.drop(['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco','SubTaskName'],axis=1,inplace=True)
df_Symmetry_Span_3.columns = ['aggregated_score_memory_Sess17h00','average_response_time_processing_Sess17h00',
                              'average_total_time_memory_Sess17h00','correct_Sess17h00','correct_response_Sess17h00','countDys_Sess17h00',
                              'countSym_Sess17h00','height_Sess17h00','LeftHalfPos_Sess17h00','List_SS_button_Sess17h00','List_SS_Pos_Sess17h00',
                              'live_row_Sess17h00','logfile_Sess17h00','maxDys_Sess17h00','maxSym_Sess17h00','pressed_buttons_Sess17h00',
                              'response_memory_Sess17h00','response_processing_Sess17h00','response_time_memory_Sess17h00',
                              'response_time_processing_Sess17h00','response_total_time_memory_Sess17h00',
                              'response_total_time_memory_full_task_Sess17h00','RightHalfPos_Sess17h00','SP_part_process_time_Sess17h00',
                              'SS_practice_score_Sess17h00','score_symmetry_span_Sess17h00','score_subblock_2_Sess17h00','score_subblock_3_Sess17h00',
                              'score_subblock_4_Sess17h00','score_subblock_5_Sess17h00','score_subblock_6_Sess17h00','SymType_Sess17h00',
                              'total_correct_processing_Sess17h00','total_response_time_processing_Sess17h00','width_Sess17h00']

#'selSNr',
df_Symmetry_Span_4 = df_Symmetry_Span_4[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName',
     'aggregated_score_memory', 'average_response_time_processing', 'average_total_time_memory', 'correct',
     'correct_response', 'countDys', 'countSym', 'height', 'LeftHalfPos', 'List_SS_button', 'List_SS_Pos', 'live_row',
     'logfile', 'maxDys', 'maxSym', 'pressed_buttons', 'response_memory', 'response_processing', 'response_time_memory',
     'response_time_processing', 'response_total_time_memory', 'response_total_time_memory_full_task', 'RightHalfPos',
     'SP_part_process_time', 'SS_practice_score', 'score_symmetry_span', 'score_subblock_2', 'score_subblock_3',
     'score_subblock_4', 'score_subblock_5', 'score_subblock_6', 'SymType',
     'total_correct_processing', 'total_response_time_processing', 'width']]
df_Symmetry_Span_4 = df_Symmetry_Span_4.astype({'correct_response': 'str', 'response_processing': 'str'})
example_d = df_Symmetry_Span_4["response_processing"].iloc[2]
df_Symmetry_Span_4 = df_Symmetry_Span_4.replace(example_d, '')
#df_Symmetry_Span_4 = df_Symmetry_Span_4.sort_values(by=['selSNr'], kind='mergesort')
#df_Symmetry_Span_4 = df_Symmetry_Span_4.sort_values(by=['subject_nr'], kind='mergesort')
df_Symmetry_Span_4.drop(['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco','SubTaskName'],axis=1,inplace=True)
df_Symmetry_Span_4.columns = ['aggregated_score_memory_Sess21h00','average_response_time_processing_Sess21h00',
                              'average_total_time_memory_Sess21h00','correct_Sess21h00','correct_response_Sess21h00','countDys_Sess21h00',
                              'countSym_Sess21h00','height_Sess21h00','LeftHalfPos_Sess21h00','List_SS_button_Sess21h00','List_SS_Pos_Sess21h00',
                              'live_row_Sess21h00','logfile_Sess21h00','maxDys_Sess21h00','maxSym_Sess21h00','pressed_buttons_Sess21h00',
                              'response_memory_Sess21h00','response_processing_Sess21h00','response_time_memory_Sess21h00',
                              'response_time_processing_Sess21h00','response_total_time_memory_Sess21h00',
                              'response_total_time_memory_full_task_Sess21h00','RightHalfPos_Sess21h00','SP_part_process_time_Sess21h00',
                              'SS_practice_score_Sess21h00','score_symmetry_span_Sess21h00','score_subblock_2_Sess21h00','score_subblock_3_Sess21h00',
                              'score_subblock_4_Sess21h00','score_subblock_5_Sess21h00','score_subblock_6_Sess21h00','SymType_Sess21h00',
                              'total_correct_processing_Sess21h00','total_response_time_processing_Sess21h00','width_Sess21h00']

df_Symmetry_Span_Final = pd.concat([df_Symmetry_Span_1,df_Symmetry_Span_2,df_Symmetry_Span_3,df_Symmetry_Span_4],axis=1)

df_Symmetry_Span_Final = df_Symmetry_Span_Final[['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco','SubTaskName',
                                                 'aggregated_score_memory_Sess09h00','aggregated_score_memory_Sess13h00',
                                                 'aggregated_score_memory_Sess17h00','aggregated_score_memory_Sess21h00',
                                                 'average_response_time_processing_Sess09h00','average_response_time_processing_Sess13h00',
                                                 'average_response_time_processing_Sess17h00','average_response_time_processing_Sess21h00',
                                                 'average_total_time_memory_Sess09h00','average_total_time_memory_Sess13h00',
                                                 'average_total_time_memory_Sess17h00','average_total_time_memory_Sess21h00',
                                                 'correct_Sess09h00','correct_Sess13h00','correct_Sess17h00','correct_Sess21h00',
                                                 'correct_response_Sess09h00','correct_response_Sess13h00','correct_response_Sess17h00',
                                                 'correct_response_Sess21h00','countDys_Sess09h00','countDys_Sess13h00','countDys_Sess17h00','countDys_Sess21h00',
                                                 'countSym_Sess09h00','countSym_Sess13h00','countSym_Sess17h00','countSym_Sess21h00','height_Sess09h00','height_Sess13h00','height_Sess17h00','height_Sess21h00',
                                                 'LeftHalfPos_Sess09h00','LeftHalfPos_Sess13h00','LeftHalfPos_Sess17h00','LeftHalfPos_Sess21h00',
                                                 'List_SS_button_Sess09h00','List_SS_button_Sess13h00','List_SS_button_Sess17h00','List_SS_button_Sess21h00',
                                                 'List_SS_Pos_Sess09h00','List_SS_Pos_Sess13h00','List_SS_Pos_Sess17h00','List_SS_Pos_Sess21h00','live_row_Sess09h00',
                                                 'live_row_Sess13h00','live_row_Sess17h00','live_row_Sess21h00','logfile_Sess09h00','logfile_Sess13h00','logfile_Sess17h00',
                                                 'logfile_Sess21h00','maxDys_Sess09h00','maxDys_Sess13h00','maxDys_Sess17h00','maxDys_Sess21h00','maxSym_Sess09h00',
                                                 'maxSym_Sess13h00','maxSym_Sess17h00','maxSym_Sess21h00','pressed_buttons_Sess09h00','pressed_buttons_Sess13h00',
                                                 'pressed_buttons_Sess17h00','pressed_buttons_Sess21h00','response_memory_Sess09h00',
                                                 'response_memory_Sess13h00','response_memory_Sess17h00','response_memory_Sess21h00',
                                                 'response_processing_Sess09h00','response_processing_Sess13h00','response_processing_Sess17h00',
                                                 'response_processing_Sess21h00','response_time_memory_Sess09h00','response_time_memory_Sess13h00','response_time_memory_Sess17h00',
                                                 'response_time_memory_Sess21h00','response_time_processing_Sess09h00','response_time_processing_Sess13h00',
                                                 'response_time_processing_Sess17h00','response_time_processing_Sess21h00','response_total_time_memory_Sess09h00',
                                                 'response_total_time_memory_Sess13h00','response_total_time_memory_Sess17h00','response_total_time_memory_Sess21h00',
                                                 'response_total_time_memory_full_task_Sess09h00','response_total_time_memory_full_task_Sess13h00',
                                                 'response_total_time_memory_full_task_Sess17h00','response_total_time_memory_full_task_Sess21h00',
                                                 'RightHalfPos_Sess09h00','RightHalfPos_Sess13h00','RightHalfPos_Sess17h00','RightHalfPos_Sess21h00',
                                                 'SP_part_process_time_Sess09h00','SP_part_process_time_Sess13h00','SP_part_process_time_Sess17h00',
                                                 'SP_part_process_time_Sess21h00','SS_practice_score_Sess09h00','SS_practice_score_Sess13h00','SS_practice_score_Sess17h00',
                                                 'SS_practice_score_Sess21h00','score_symmetry_span_Sess09h00','score_symmetry_span_Sess13h00',
                                                 'score_symmetry_span_Sess17h00','score_symmetry_span_Sess21h00','score_subblock_2_Sess09h00','score_subblock_2_Sess13h00',
                                                 'score_subblock_2_Sess17h00','score_subblock_2_Sess21h00','score_subblock_3_Sess09h00','score_subblock_3_Sess13h00',
                                                 'score_subblock_3_Sess17h00','score_subblock_3_Sess21h00','score_subblock_4_Sess09h00','score_subblock_4_Sess13h00',
                                                 'score_subblock_4_Sess17h00','score_subblock_4_Sess21h00','score_subblock_5_Sess09h00','score_subblock_5_Sess13h00',
                                                 'score_subblock_5_Sess17h00','score_subblock_5_Sess21h00','score_subblock_6_Sess09h00','score_subblock_6_Sess13h00',
                                                 'score_subblock_6_Sess17h00','score_subblock_6_Sess21h00','SymType_Sess09h00','SymType_Sess13h00','SymType_Sess17h00',
                                                 'SymType_Sess21h00','total_correct_processing_Sess09h00','total_correct_processing_Sess13h00','total_correct_processing_Sess17h00',
                                                 'total_correct_processing_Sess21h00','total_response_time_processing_Sess09h00','total_response_time_processing_Sess13h00',
                                                 'total_response_time_processing_Sess17h00','total_response_time_processing_Sess21h00','width_Sess09h00','width_Sess13h00',
                                                 'width_Sess17h00','width_Sess21h00']]

############################################################################################
############################################################################################
#'Probe', 'Target',
#'selSNr',
df_Binding_Task_1 = df_Binding_Task_1[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'acc', 'average_response_time',
     'BindingRawScore', 'correct', 'correct_response', 'counter', 'Delay', 'eightsec_accuracy', 'FalseAlarms', 'height',
     'Hits', 'live_row', 'logfile', 'match_1s_accuracy', 'match_1s_avg_rt', 'match_8s_accuracy', 'match_8s_avg_rt',
     'mismatch_1s_accuracy', 'mismatch_1s_avg_rt', 'mismatch_8s_accuracy', 'mismatch_8s_avg_rt', 'NNonResponses',
     'Omissions', 'onesec_accuracy', 'QuinetteAccuracyScore', 'QuinetteProcessingScore', 'response',
     'response_time', 'ResponsesGiven', 'total_correct', 'total_match_1s_rt', 'total_match_8s_rt',
     'total_mismatch_1s_rt', 'total_mismatch_8s_rt', 'total_response_time', 'total_responses', 'width']]
df_Binding_Task_1[['acc', 'average_response_time']] = df_Binding_Task_1[['acc', 'average_response_time']].replace(',', '.')
df_Binding_Task_1 = df_Binding_Task_1.astype(
    {'acc': 'float64', 'average_response_time': 'float64', 'correct_response': 'str', 'response': 'str'})
#df_Binding_Task_1 = df_Binding_Task_1.sort_values(by=['selSNr'], kind='mergesort')
#df_Binding_Task_1 = df_Binding_Task_1.sort_values(by=['subject_nr'], kind='mergesort')
df_Binding_Task_1.columns = ['subject_nr','CB_ref','practice','TrialNumber','acc_Sess09h00',
                             'average_response_time_Sess09h00','BindingRawScore_Sess09h00','correct_Sess09h00','correct_response_Sess09h00',
                             'counter_Sess09h00','Delay_Sess09h00','eightsec_accuracy_Sess09h00','FalseAlarms_Sess09h00','height_Sess09h00','Hits_Sess09h00',
                             'live_row_Sess09h00','logfile_Sess09h00','match_1s_accuracy_Sess09h00','match_1s_avg_rt_Sess09h00','match_8s_accuracy_Sess09h00',
                             'match_8s_avg_rt_Sess09h00','mismatch_1s_accuracy_Sess09h00','mismatch_1s_avg_rt_Sess09h00','mismatch_8s_accuracy_Sess09h00',
                             'mismatch_8s_avg_rt_Sess09h00','NNonResponses_Sess09h00','Omissions_Sess09h00','onesec_accuracy_Sess09h00',
                             'QuinetteAccuracyScore_Sess09h00','QuinetteProcessingScore_Sess09h00','response_Sess09h00','response_time_Sess09h00',
                             'ResponsesGiven_Sess09h00','total_correct_Sess09h00','total_match_1s_rt_Sess09h00','total_match_8s_rt_Sess09h00',
                             'total_mismatch_1s_rt_Sess09h00','total_mismatch_8s_rt_Sess09h00','total_response_time_Sess09h00','total_responses_Sess09h00',
                             'width_Sess09h00']

#'selSNr',
df_Binding_Task_2 = df_Binding_Task_2[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'acc', 'average_response_time',
     'BindingRawScore', 'correct', 'correct_response', 'counter', 'Delay', 'eightsec_accuracy', 'FalseAlarms', 'height',
     'Hits', 'live_row', 'logfile', 'match_1s_accuracy', 'match_1s_avg_rt', 'match_8s_accuracy', 'match_8s_avg_rt',
     'mismatch_1s_accuracy', 'mismatch_1s_avg_rt', 'mismatch_8s_accuracy', 'mismatch_8s_avg_rt', 'NNonResponses',
     'Omissions', 'onesec_accuracy', 'QuinetteAccuracyScore', 'QuinetteProcessingScore', 'response',
     'response_time', 'ResponsesGiven', 'total_correct', 'total_match_1s_rt', 'total_match_8s_rt',
     'total_mismatch_1s_rt', 'total_mismatch_8s_rt', 'total_response_time', 'total_responses', 'width']]
df_Binding_Task_2[['acc', 'average_response_time']] = df_Binding_Task_2[['acc', 'average_response_time']].replace(',', '.')
df_Binding_Task_2 = df_Binding_Task_2.astype(
    {'acc': 'float64', 'average_response_time': 'float64', 'correct_response': 'str', 'response': 'str'})
#df_Binding_Task_2 = df_Binding_Task_2.sort_values(by=['selSNr'], kind='mergesort')
#df_Binding_Task_2 = df_Binding_Task_2.sort_values(by=['subject_nr'], kind='mergesort')
df_Binding_Task_2.drop(['subject_nr','CB_ref','practice','TrialNumber'],axis=1,inplace=True)
df_Binding_Task_2.columns = ['acc_Sess13h00','average_response_time_Sess13h00','BindingRawScore_Sess13h00','correct_Sess13h00','correct_response_Sess13h00',
                             'counter_Sess13h00','Delay_Sess13h00','eightsec_accuracy_Sess13h00','FalseAlarms_Sess13h00','height_Sess13h00','Hits_Sess13h00',
                             'live_row_Sess13h00','logfile_Sess13h00','match_1s_accuracy_Sess13h00','match_1s_avg_rt_Sess13h00','match_8s_accuracy_Sess13h00',
                             'match_8s_avg_rt_Sess13h00','mismatch_1s_accuracy_Sess13h00','mismatch_1s_avg_rt_Sess13h00','mismatch_8s_accuracy_Sess13h00',
                             'mismatch_8s_avg_rt_Sess13h00','NNonResponses_Sess13h00','Omissions_Sess13h00','onesec_accuracy_Sess13h00',
                             'QuinetteAccuracyScore_Sess13h00','QuinetteProcessingScore_Sess13h00','response_Sess13h00','response_time_Sess13h00',
                             'ResponsesGiven_Sess13h00','total_correct_Sess13h00','total_match_1s_rt_Sess13h00','total_match_8s_rt_Sess13h00',
                             'total_mismatch_1s_rt_Sess13h00','total_mismatch_8s_rt_Sess13h00','total_response_time_Sess13h00','total_responses_Sess13h00',
                             'width_Sess13h00']

#'selSNr',
df_Binding_Task_3 = df_Binding_Task_3[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'acc', 'average_response_time',
     'BindingRawScore', 'correct', 'correct_response', 'counter', 'Delay', 'eightsec_accuracy', 'FalseAlarms', 'height',
     'Hits', 'live_row', 'logfile', 'match_1s_accuracy', 'match_1s_avg_rt', 'match_8s_accuracy', 'match_8s_avg_rt',
     'mismatch_1s_accuracy', 'mismatch_1s_avg_rt', 'mismatch_8s_accuracy', 'mismatch_8s_avg_rt', 'NNonResponses',
     'Omissions', 'onesec_accuracy', 'QuinetteAccuracyScore', 'QuinetteProcessingScore', 'response',
     'response_time', 'ResponsesGiven', 'total_correct', 'total_match_1s_rt', 'total_match_8s_rt',
     'total_mismatch_1s_rt', 'total_mismatch_8s_rt', 'total_response_time', 'total_responses', 'width']]
df_Binding_Task_3[['acc', 'average_response_time']] = df_Binding_Task_3[['acc', 'average_response_time']].replace(',', '.')
df_Binding_Task_3 = df_Binding_Task_3.astype(
    {'acc': 'float64', 'average_response_time': 'float64', 'correct_response': 'str', 'response': 'str'})
#df_Binding_Task_3 = df_Binding_Task_3.sort_values(by=['selSNr'], kind='mergesort')
#df_Binding_Task_3 = df_Binding_Task_3.sort_values(by=['subject_nr'], kind='mergesort')
df_Binding_Task_3.drop(['subject_nr','CB_ref','practice','TrialNumber'],axis=1,inplace=True)
df_Binding_Task_3.columns = ['acc_Sess17h00','average_response_time_Sess17h00','BindingRawScore_Sess17h00','correct_Sess17h00','correct_response_Sess17h00',
                             'counter_Sess17h00','Delay_Sess17h00','eightsec_accuracy_Sess17h00','FalseAlarms_Sess17h00','height_Sess17h00','Hits_Sess17h00',
                             'live_row_Sess17h00','logfile_Sess17h00','match_1s_accuracy_Sess17h00','match_1s_avg_rt_Sess17h00','match_8s_accuracy_Sess17h00',
                             'match_8s_avg_rt_Sess17h00','mismatch_1s_accuracy_Sess17h00','mismatch_1s_avg_rt_Sess17h00','mismatch_8s_accuracy_Sess17h00',
                             'mismatch_8s_avg_rt_Sess17h00','NNonResponses_Sess17h00','Omissions_Sess17h00','onesec_accuracy_Sess17h00',
                             'QuinetteAccuracyScore_Sess17h00','QuinetteProcessingScore_Sess17h00','response_Sess17h00','response_time_Sess17h00',
                             'ResponsesGiven_Sess17h00','total_correct_Sess17h00','total_match_1s_rt_Sess17h00','total_match_8s_rt_Sess17h00',
                             'total_mismatch_1s_rt_Sess17h00','total_mismatch_8s_rt_Sess17h00','total_response_time_Sess17h00','total_responses_Sess17h00',
                             'width_Sess17h00']

#'selSNr',
df_Binding_Task_4 = df_Binding_Task_4[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'acc', 'average_response_time',
     'BindingRawScore', 'correct', 'correct_response', 'counter', 'Delay', 'eightsec_accuracy', 'FalseAlarms', 'height',
     'Hits', 'live_row', 'logfile', 'match_1s_accuracy', 'match_1s_avg_rt', 'match_8s_accuracy', 'match_8s_avg_rt',
     'mismatch_1s_accuracy', 'mismatch_1s_avg_rt', 'mismatch_8s_accuracy', 'mismatch_8s_avg_rt', 'NNonResponses',
     'Omissions', 'onesec_accuracy', 'QuinetteAccuracyScore', 'QuinetteProcessingScore', 'response',
     'response_time', 'ResponsesGiven', 'total_correct', 'total_match_1s_rt', 'total_match_8s_rt',
     'total_mismatch_1s_rt', 'total_mismatch_8s_rt', 'total_response_time', 'total_responses', 'width']]
df_Binding_Task_4[['acc', 'average_response_time']] = df_Binding_Task_4[['acc', 'average_response_time']].replace(',', '.')
df_Binding_Task_4 = df_Binding_Task_4.astype(
    {'acc': 'float64', 'average_response_time': 'float64', 'correct_response': 'str', 'response': 'str'})
#df_Binding_Task_4 = df_Binding_Task_4.sort_values(by=['selSNr'], kind='mergesort')
#df_Binding_Task_4 = df_Binding_Task_4.sort_values(by=['subject_nr'], kind='mergesort')
df_Binding_Task_4.drop(['subject_nr','CB_ref','practice','TrialNumber'],axis=1,inplace=True)
df_Binding_Task_4.columns = ['acc_Sess21h00','average_response_time_Sess21h00','BindingRawScore_Sess21h00','correct_Sess21h00','correct_response_Sess21h00',
                             'counter_Sess21h00','Delay_Sess21h00','eightsec_accuracy_Sess21h00','FalseAlarms_Sess21h00','height_Sess21h00','Hits_Sess21h00',
                             'live_row_Sess21h00','logfile_Sess21h00','match_1s_accuracy_Sess21h00','match_1s_avg_rt_Sess21h00','match_8s_accuracy_Sess21h00',
                             'match_8s_avg_rt_Sess21h00','mismatch_1s_accuracy_Sess21h00','mismatch_1s_avg_rt_Sess21h00','mismatch_8s_accuracy_Sess21h00',
                             'mismatch_8s_avg_rt_Sess21h00','NNonResponses_Sess21h00','Omissions_Sess21h00','onesec_accuracy_Sess21h00',
                             'QuinetteAccuracyScore_Sess21h00','QuinetteProcessingScore_Sess21h00','response_Sess21h00','response_time_Sess21h00',
                             'ResponsesGiven_Sess21h00','total_correct_Sess21h00','total_match_1s_rt_Sess21h00','total_match_8s_rt_Sess21h00',
                             'total_mismatch_1s_rt_Sess21h00','total_mismatch_8s_rt_Sess21h00','total_response_time_Sess21h00','total_responses_Sess21h00',
                             'width_Sess21h00']

df_Binding_Task_Final = pd.concat([df_Binding_Task_1,df_Binding_Task_2,df_Binding_Task_3,df_Binding_Task_4],axis=1)

df_Binding_Task_Final = df_Binding_Task_Final[['subject_nr','CB_ref','practice','TrialNumber','acc_Sess09h00','acc_Sess13h00','acc_Sess17h00','acc_Sess21h00',
                                         'average_response_time_Sess09h00','average_response_time_Sess13h00','average_response_time_Sess17h00','average_response_time_Sess21h00',
                                         'BindingRawScore_Sess09h00','BindingRawScore_Sess13h00','BindingRawScore_Sess17h00','BindingRawScore_Sess21h00','correct_Sess09h00',
                                         'correct_Sess13h00','correct_Sess17h00','correct_Sess21h00','correct_response_Sess09h00','correct_response_Sess13h00',
                                         'correct_response_Sess17h00','correct_response_Sess21h00','counter_Sess09h00','counter_Sess13h00','counter_Sess17h00','counter_Sess21h00',
                                         'Delay_Sess09h00','Delay_Sess13h00','Delay_Sess17h00','Delay_Sess21h00','eightsec_accuracy_Sess09h00','eightsec_accuracy_Sess13h00',
                                         'eightsec_accuracy_Sess17h00','eightsec_accuracy_Sess21h00','FalseAlarms_Sess09h00','FalseAlarms_Sess13h00','FalseAlarms_Sess17h00',
                                         'FalseAlarms_Sess21h00','height_Sess09h00','height_Sess13h00','height_Sess17h00','height_Sess21h00','Hits_Sess09h00','Hits_Sess13h00',
                                         'Hits_Sess17h00','Hits_Sess21h00','live_row_Sess09h00','live_row_Sess13h00','live_row_Sess17h00','live_row_Sess21h00','logfile_Sess09h00',
                                         'logfile_Sess13h00','logfile_Sess17h00','logfile_Sess21h00','match_1s_accuracy_Sess09h00','match_1s_accuracy_Sess13h00',
                                         'match_1s_accuracy_Sess17h00','match_1s_accuracy_Sess21h00','match_1s_avg_rt_Sess09h00','match_1s_avg_rt_Sess13h00','match_1s_avg_rt_Sess17h00',
                                         'match_1s_avg_rt_Sess21h00','match_8s_accuracy_Sess09h00','match_8s_accuracy_Sess13h00','match_8s_accuracy_Sess17h00',
                                         'match_8s_accuracy_Sess21h00','match_8s_avg_rt_Sess09h00','match_8s_avg_rt_Sess13h00','match_8s_avg_rt_Sess17h00',
                                         'match_8s_avg_rt_Sess21h00','mismatch_1s_accuracy_Sess09h00','mismatch_1s_accuracy_Sess13h00','mismatch_1s_accuracy_Sess17h00',
                                         'mismatch_1s_accuracy_Sess21h00','mismatch_1s_avg_rt_Sess09h00','mismatch_1s_avg_rt_Sess13h00','mismatch_1s_avg_rt_Sess17h00',
                                         'mismatch_1s_avg_rt_Sess21h00','mismatch_8s_accuracy_Sess09h00','mismatch_8s_accuracy_Sess13h00','mismatch_8s_accuracy_Sess17h00',
                                         'mismatch_8s_accuracy_Sess21h00','mismatch_8s_avg_rt_Sess09h00','mismatch_8s_avg_rt_Sess13h00','mismatch_8s_avg_rt_Sess17h00',
                                         'mismatch_8s_avg_rt_Sess21h00','NNonResponses_Sess09h00','NNonResponses_Sess13h00','NNonResponses_Sess17h00',
                                         'NNonResponses_Sess21h00','Omissions_Sess09h00','Omissions_Sess13h00','Omissions_Sess17h00',
                                         'Omissions_Sess21h00','onesec_accuracy_Sess09h00','onesec_accuracy_Sess13h00','onesec_accuracy_Sess17h00',
                                         'onesec_accuracy_Sess21h00','QuinetteAccuracyScore_Sess09h00','QuinetteAccuracyScore_Sess13h00','QuinetteAccuracyScore_Sess17h00',
                                         'QuinetteAccuracyScore_Sess21h00','QuinetteProcessingScore_Sess09h00','QuinetteProcessingScore_Sess13h00',
                                         'QuinetteProcessingScore_Sess17h00','QuinetteProcessingScore_Sess21h00','response_Sess09h00',
                                         'response_Sess13h00','response_Sess17h00','response_Sess21h00','response_time_Sess09h00','response_time_Sess13h00',
                                         'response_time_Sess17h00','response_time_Sess21h00','ResponsesGiven_Sess09h00','ResponsesGiven_Sess13h00',
                                         'ResponsesGiven_Sess17h00','ResponsesGiven_Sess21h00','total_correct_Sess09h00','total_correct_Sess13h00','total_correct_Sess17h00',
                                         'total_correct_Sess21h00','total_match_1s_rt_Sess09h00','total_match_1s_rt_Sess13h00','total_match_1s_rt_Sess17h00',
                                         'total_match_1s_rt_Sess21h00','total_match_8s_rt_Sess09h00','total_match_8s_rt_Sess13h00','total_match_8s_rt_Sess17h00',
                                         'total_match_8s_rt_Sess21h00','total_mismatch_1s_rt_Sess09h00','total_mismatch_1s_rt_Sess13h00','total_mismatch_1s_rt_Sess17h00',
                                         'total_mismatch_1s_rt_Sess21h00','total_mismatch_8s_rt_Sess09h00','total_mismatch_8s_rt_Sess13h00','total_mismatch_8s_rt_Sess17h00',
                                         'total_mismatch_8s_rt_Sess21h00','total_response_time_Sess09h00','total_response_time_Sess13h00','total_response_time_Sess17h00',
                                         'total_response_time_Sess21h00','total_responses_Sess09h00','total_responses_Sess13h00','total_responses_Sess17h00','total_responses_Sess21h00',
                                         'width_Sess09h00','width_Sess13h00','width_Sess17h00','width_Sess21h00']]

############################################################################################
############################################################################################
#'selSNr',
df_Operation_Span_1 = df_Operation_Span_1[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName', 'acc', 'avg_rt',
     'BlockChoice', 'correct', 'correct_response', 'height', 'letter', 'List_Prev_Letter', 'List_responses_memory',
     'live_row', 'logfile', 'response_average_time_memory', 'response_memory', 'response_processing',
     'response_time_memory', 'response_time_processing', 'response_total_time_memory', 'OP_part_process_time',
     'score_practice', 'score_operation_span', 'score_subblock_2', 'score_subblock_3', 'score_subblock_4', 'score_subblock_5',
     'score_subblock_6', 'Tipo', 'total_correct', 'total_response_time',
     'total_responses', 'width']]
df_Operation_Span_1[['acc', 'avg_rt']] = df_Operation_Span_1[['acc', 'avg_rt']].replace(',', '.')
df_Operation_Span_1 = df_Operation_Span_1.astype(
    {'acc': 'float64', 'avg_rt': 'float64', 'correct_response': 'str', 'response_processing': 'str'})
example_c = df_Operation_Span_1["response_processing"].iloc[2]
df_Operation_Span_1 = df_Operation_Span_1.replace(example_c, '')
#df_Operation_Span_1 = df_Operation_Span_1.sort_values(by=['selSNr'], kind='mergesort')
#df_Operation_Span_1 = df_Operation_Span_1.sort_values(by=['subject_nr'], kind='mergesort')
df_Operation_Span_1.columns = ['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco',
                               'SubTaskName','acc_Sess09h00','avg_rt_Sess09h00','BlockChoice_Sess09h00','correct_Sess09h00',
                               'correct_response_Sess09h00','height_Sess09h00','letter_Sess09h00','List_Prev_Letter_Sess09h00',
                               'List_responses_memory_Sess09h00','live_row_Sess09h00','logfile_Sess09h00','response_average_time_memory_Sess09h00',
                               'response_memory_Sess09h00','response_processing_Sess09h00','response_time_memory_Sess09h00',
                               'response_time_processing_Sess09h00','response_total_time_memory_Sess09h00','OP_part_process_time_Sess09h00',
                               'score_practice_Sess09h00','score_operation_span_Sess09h00','score_subblock_2_Sess09h00','score_subblock_3_Sess09h00',
                               'score_subblock_4_Sess09h00','score_subblock_5_Sess09h00','score_subblock_6_Sess09h00','Tipo_Sess09h00',
                               'total_correct_Sess09h00','total_response_time_Sess09h00','total_responses_Sess09h00','width_Sess09h00']

#'selSNr',
df_Operation_Span_2 = df_Operation_Span_2[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName', 'acc', 'avg_rt',
     'BlockChoice', 'correct', 'correct_response', 'height', 'letter', 'List_Prev_Letter', 'List_responses_memory',
     'live_row', 'logfile', 'response_average_time_memory', 'response_memory', 'response_processing',
     'response_time_memory', 'response_time_processing', 'response_total_time_memory', 'OP_part_process_time',
     'score_practice', 'score_operation_span', 'score_subblock_2', 'score_subblock_3', 'score_subblock_4', 'score_subblock_5',
     'score_subblock_6', 'Tipo', 'total_correct', 'total_response_time',
     'total_responses', 'width']]
df_Operation_Span_2[['acc', 'avg_rt']] = df_Operation_Span_2[['acc', 'avg_rt']].replace(',', '.')
df_Operation_Span_2 = df_Operation_Span_2.astype(
    {'acc': 'float64', 'avg_rt': 'float64', 'correct_response': 'str', 'response_processing': 'str'})
example_c = df_Operation_Span_2["response_processing"].iloc[2]
df_Operation_Span_2 = df_Operation_Span_2.replace(example_c, '')
#df_Operation_Span_2 = df_Operation_Span_2.sort_values(by=['selSNr'], kind='mergesort')
#df_Operation_Span_2 = df_Operation_Span_2.sort_values(by=['subject_nr'], kind='mergesort')
df_Operation_Span_2.drop(['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco','SubTaskName'],axis=1,inplace=True)
df_Operation_Span_2.columns = ['acc_Sess13h00','avg_rt_Sess13h00','BlockChoice_Sess13h00','correct_Sess13h00',
                               'correct_response_Sess13h00','height_Sess13h00','letter_Sess13h00','List_Prev_Letter_Sess13h00',
                               'List_responses_memory_Sess13h00','live_row_Sess13h00','logfile_Sess13h00','response_average_time_memory_Sess13h00',
                               'response_memory_Sess13h00','response_processing_Sess13h00','response_time_memory_Sess13h00',
                               'response_time_processing_Sess13h00','response_total_time_memory_Sess13h00','OP_part_process_time_Sess13h00',
                               'score_practice_Sess13h00','score_operation_span_Sess13h00','score_subblock_2_Sess13h00','score_subblock_3_Sess13h00',
                               'score_subblock_4_Sess13h00','score_subblock_5_Sess13h00','score_subblock_6_Sess13h00','Tipo_Sess13h00',
                               'total_correct_Sess13h00','total_response_time_Sess13h00','total_responses_Sess13h00','width_Sess13h00']

#'selSNr',
df_Operation_Span_3 = df_Operation_Span_3[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName', 'acc', 'avg_rt',
     'BlockChoice', 'correct', 'correct_response', 'height', 'letter', 'List_Prev_Letter', 'List_responses_memory',
     'live_row', 'logfile', 'response_average_time_memory', 'response_memory', 'response_processing',
     'response_time_memory', 'response_time_processing', 'response_total_time_memory', 'OP_part_process_time',
     'score_practice', 'score_operation_span', 'score_subblock_2', 'score_subblock_3', 'score_subblock_4', 'score_subblock_5',
     'score_subblock_6', 'Tipo', 'total_correct', 'total_response_time',
     'total_responses', 'width']]
df_Operation_Span_3[['acc', 'avg_rt']] = df_Operation_Span_3[['acc', 'avg_rt']].replace(',', '.')
df_Operation_Span_3 = df_Operation_Span_3.astype(
    {'acc': 'float64', 'avg_rt': 'float64', 'correct_response': 'str', 'response_processing': 'str'})
example_c = df_Operation_Span_3["response_processing"].iloc[2]
df_Operation_Span_3 = df_Operation_Span_3.replace(example_c, '')
#df_Operation_Span_3 = df_Operation_Span_3.sort_values(by=['selSNr'], kind='mergesort')
#df_Operation_Span_3 = df_Operation_Span_3.sort_values(by=['subject_nr'], kind='mergesort')
df_Operation_Span_3.drop(['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco','SubTaskName'],axis=1,inplace=True)
df_Operation_Span_3.columns = ['acc_Sess17h00','avg_rt_Sess17h00','BlockChoice_Sess17h00','correct_Sess17h00',
                               'correct_response_Sess17h00','height_Sess17h00','letter_Sess17h00','List_Prev_Letter_Sess17h00',
                               'List_responses_memory_Sess17h00','live_row_Sess17h00','logfile_Sess17h00','response_average_time_memory_Sess17h00',
                               'response_memory_Sess17h00','response_processing_Sess17h00','response_time_memory_Sess17h00',
                               'response_time_processing_Sess17h00','response_total_time_memory_Sess17h00','OP_part_process_time_Sess17h00',
                               'score_practice_Sess17h00','score_operation_span_Sess17h00','score_subblock_2_Sess17h00','score_subblock_3_Sess17h00',
                               'score_subblock_4_Sess17h00','score_subblock_5_Sess17h00','score_subblock_6_Sess17h00','Tipo_Sess17h00',
                               'total_correct_Sess17h00','total_response_time_Sess17h00','total_responses_Sess17h00','width_Sess17h00']

#'selSNr',
df_Operation_Span_4 = df_Operation_Span_4[
    ['subject_nr', 'CB_ref', 'practice', 'TrialNumber', 'Sub_bloco', 'SubTaskName', 'acc', 'avg_rt',
     'BlockChoice', 'correct', 'correct_response', 'height', 'letter', 'List_Prev_Letter', 'List_responses_memory',
     'live_row', 'logfile', 'response_average_time_memory', 'response_memory', 'response_processing',
     'response_time_memory', 'response_time_processing', 'response_total_time_memory', 'OP_part_process_time',
     'score_practice', 'score_operation_span', 'score_subblock_2', 'score_subblock_3', 'score_subblock_4', 'score_subblock_5',
     'score_subblock_6', 'Tipo', 'total_correct', 'total_response_time',
     'total_responses', 'width']]
df_Operation_Span_4[['acc', 'avg_rt']] = df_Operation_Span_4[['acc', 'avg_rt']].replace(',', '.')
df_Operation_Span_4 = df_Operation_Span_4.astype(
    {'acc': 'float64', 'avg_rt': 'float64', 'correct_response': 'str', 'response_processing': 'str'})
example_c = df_Operation_Span_4["response_processing"].iloc[2]
df_Operation_Span_4 = df_Operation_Span_4.replace(example_c, '')
#df_Operation_Span_4 = df_Operation_Span_4.sort_values(by=['selSNr'], kind='mergesort')
#df_Operation_Span_4 = df_Operation_Span_4.sort_values(by=['subject_nr'], kind='mergesort')
df_Operation_Span_4.drop(['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco','SubTaskName'],axis=1,inplace=True)
df_Operation_Span_4.columns = ['acc_Sess21h00','avg_rt_Sess21h00','BlockChoice_Sess21h00','correct_Sess21h00',
                               'correct_response_Sess21h00','height_Sess21h00','letter_Sess21h00','List_Prev_Letter_Sess21h00',
                               'List_responses_memory_Sess21h00','live_row_Sess21h00','logfile_Sess21h00','response_average_time_memory_Sess21h00',
                               'response_memory_Sess21h00','response_processing_Sess21h00','response_time_memory_Sess21h00',
                               'response_time_processing_Sess21h00','response_total_time_memory_Sess21h00','OP_part_process_time_Sess21h00',
                               'score_practice_Sess21h00','score_operation_span_Sess21h00','score_subblock_2_Sess21h00','score_subblock_3_Sess21h00',
                               'score_subblock_4_Sess21h00','score_subblock_5_Sess21h00','score_subblock_6_Sess21h00','Tipo_Sess21h00',
                               'total_correct_Sess21h00','total_response_time_Sess21h00','total_responses_Sess21h00','width_Sess21h00']

df_Operation_Span_Final = pd.concat([df_Operation_Span_1,df_Operation_Span_2,df_Operation_Span_3,df_Operation_Span_4],axis=1)


df_Operation_Span_Final = df_Operation_Span_Final[['subject_nr','CB_ref','practice','TrialNumber','Sub_bloco','SubTaskName',
                                                   'acc_Sess09h00','acc_Sess13h00','acc_Sess17h00','acc_Sess21h00','avg_rt_Sess09h00','avg_rt_Sess13h00','avg_rt_Sess17h00','avg_rt_Sess21h00',
                                                   'BlockChoice_Sess09h00','BlockChoice_Sess13h00','BlockChoice_Sess17h00','BlockChoice_Sess21h00','correct_Sess09h00',
                                                   'correct_Sess13h00','correct_Sess17h00','correct_Sess21h00','correct_response_Sess09h00','correct_response_Sess13h00',
                                                   'correct_response_Sess17h00','correct_response_Sess21h00','height_Sess09h00','height_Sess13h00','height_Sess17h00','height_Sess21h00',
                                                   'letter_Sess09h00','letter_Sess13h00','letter_Sess17h00','letter_Sess21h00','List_Prev_Letter_Sess09h00','List_Prev_Letter_Sess13h00',
                                                   'List_Prev_Letter_Sess17h00','List_Prev_Letter_Sess21h00','List_responses_memory_Sess09h00','List_responses_memory_Sess13h00',
                                                   'List_responses_memory_Sess17h00','List_responses_memory_Sess21h00','live_row_Sess09h00','live_row_Sess13h00','live_row_Sess17h00',
                                                   'live_row_Sess21h00','logfile_Sess09h00','logfile_Sess13h00','logfile_Sess17h00','logfile_Sess21h00',
                                                   'response_average_time_memory_Sess09h00','response_average_time_memory_Sess13h00','response_average_time_memory_Sess17h00',
                                                   'response_average_time_memory_Sess21h00','response_memory_Sess09h00','response_memory_Sess13h00','response_memory_Sess17h00',
                                                   'response_memory_Sess21h00','response_processing_Sess09h00','response_processing_Sess13h00','response_processing_Sess17h00',
                                                   'response_processing_Sess21h00','response_time_memory_Sess09h00','response_time_memory_Sess13h00','response_time_memory_Sess17h00',
                                                   'response_time_memory_Sess21h00','response_time_processing_Sess09h00','response_time_processing_Sess13h00',
                                                   'response_time_processing_Sess17h00','response_time_processing_Sess21h00','response_total_time_memory_Sess09h00',
                                                   'response_total_time_memory_Sess13h00','response_total_time_memory_Sess17h00','response_total_time_memory_Sess21h00',
                                                   'OP_part_process_time_Sess09h00','OP_part_process_time_Sess13h00','OP_part_process_time_Sess17h00',
                                                   'OP_part_process_time_Sess21h00','score_practice_Sess09h00','score_practice_Sess13h00','score_practice_Sess17h00',
                                                   'score_practice_Sess21h00','score_operation_span_Sess09h00','score_operation_span_Sess13h00','score_operation_span_Sess17h00',
                                                   'score_operation_span_Sess21h00','score_subblock_2_Sess09h00','score_subblock_2_Sess13h00','score_subblock_2_Sess17h00',
                                                   'score_subblock_2_Sess21h00','score_subblock_3_Sess09h00','score_subblock_3_Sess13h00','score_subblock_3_Sess17h00',
                                                   'score_subblock_3_Sess21h00','score_subblock_4_Sess09h00','score_subblock_4_Sess13h00','score_subblock_4_Sess17h00',
                                                   'score_subblock_4_Sess21h00','score_subblock_5_Sess09h00','score_subblock_5_Sess13h00','score_subblock_5_Sess17h00',
                                                   'score_subblock_5_Sess21h00','score_subblock_6_Sess09h00','score_subblock_6_Sess13h00','score_subblock_6_Sess17h00',
                                                   'score_subblock_6_Sess21h00','Tipo_Sess09h00','Tipo_Sess13h00','Tipo_Sess17h00','Tipo_Sess21h00','total_correct_Sess09h00',
                                                   'total_correct_Sess13h00','total_correct_Sess17h00','total_correct_Sess21h00','total_response_time_Sess09h00',
                                                   'total_response_time_Sess13h00','total_response_time_Sess17h00','total_response_time_Sess21h00','total_responses_Sess09h00',
                                                   'total_responses_Sess13h00','total_responses_Sess17h00','total_responses_Sess21h00','width_Sess09h00','width_Sess13h00',
                                                   'width_Sess17h00','width_Sess21h00']]

cols_to_round = [
    "Reading Span Session 09h00",
    "Reading Span Session 13h00",
    "Reading Span Session 17h00",
    "Reading Span Session 21h00",
    "Updating Task Session 09h00",
    "Updating Task Session 13h00",
    "Updating Task Session 17h00",
    "Updating Task Session 21h00",
    "Symmetry Span Session 09h00",
    "Symmetry Span Session 13h00",
    "Symmetry Span Session 17h00",
    "Symmetry Span Session 21h00",
    "Binding Task Session 09h00",
    "Binding Task Session 13h00",
    "Binding Task Session 17h00",
    "Binding Task Session 21h00",
    "Operation Span Session 09h00",
    "Operation Span Session 13h00",
    "Operation Span Session 17h00",
    "Operation Span Session 21h00",
]

df_normalized_scores[cols_to_round] = (
    df_normalized_scores[cols_to_round]
    .apply(pd.to_numeric, errors="coerce")  # converts text to numbers safely
    .round(2)  # rounds to 2 decimal places
)

df_normalized_scores["subject_nr"] = pd.to_numeric(df_normalized_scores["subject_nr"], errors="coerce")
df_normalized_scores = df_normalized_scores.sort_values(by="subject_nr").reset_index(drop=True)

df_raw_scores["subject_nr"] = pd.to_numeric(df_raw_scores["subject_nr"], errors="coerce")
df_raw_scores = df_raw_scores.sort_values(by="subject_nr").reset_index(drop=True)

################################################################################################################################################################################
#
#
#
#
#
#
#
#
###############################################################################################################################################################################
#6 - Merge and creates Database with all data that was processed and worked on.
import pandas as pd
#Guarda as dataframes criadas anteriormente com num único excel com várias folhas.
#Cada uma da folhas contém informação referente (1) Screening data, (2) sleep and (3) activity diary, (4) grades and schedules,
# and (5) WM performance
with pd.ExcelWriter('BD_all_data_combined.xlsx') as writer:
    df_excel_Screening.to_excel(writer, sheet_name='Screening_Part', index=False)
    SD_df_excel_data_part.to_excel(writer, sheet_name='Sleep Diary', index=False)
    AD_df_excel_data_part.to_excel(writer, sheet_name='Activity Diary', index=False)
    df_Actigraphy.to_excel(writer,sheet_name="Actigraphy", index=False)
    df_raw_scores.to_excel(writer, sheet_name='Raw Scores', index=False)
    df_normalized_scores.to_excel(writer, sheet_name='Normalized Scores', index=False)
    df_Reading_Span_Final.to_excel(writer, sheet_name='Reading Span', index=False)
    df_WMU_Task_Final.to_excel(writer, sheet_name='Updating Task', index=False)
    df_Symmetry_Span_Final.to_excel(writer, sheet_name='Symmetry Span', index=False)
    df_Binding_Task_Final.to_excel(writer, sheet_name='Binding Task', index=False)
    df_Operation_Span_Final.to_excel(writer, sheet_name='Operation Span', index=False)
    df_raw_scores_pract.to_excel(writer, sheet_name='Practice Raw Scores', index=False)
    df_normalized_scores_pract.to_excel(writer, sheet_name='Practice Normalized Scores', index=False)
    df_Reading_Span.to_excel(writer, sheet_name='Practice RS', index=False)
    df_WMU_Task.to_excel(writer, sheet_name='Practice UT', index=False)
    df_Symmetry_Span.to_excel(writer, sheet_name='Practice SS', index=False)
    df_Binding_Task.to_excel(writer, sheet_name='Practice BT', index=False)
    df_Operation_Span.to_excel(writer, sheet_name='Practice OS', index=False)