import time
import unicodedata

import pandas    as pd
import streamlit as st

from PIL import Image

#OBS.: Este arquivo funciona perfeitamente.

#Read file
df = pd.read_excel('REVISTA MAHIKARI - KAWASSAKI HOSA.xlsx')

df = df.sort_values(by=['ANO', 'Nº RM'], ascending=[False, True])

#ETL de dados e subscrição do arquivo.
df_1 = df.copy()

# Função para remover acentos
def remover_acentos(texto):
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode()

# Eliminando colunas vazias
df_1 = df_1.dropna(subset=['Nº RM'])
# SUbstituindo Valores NAN
df_1 = df_1.fillna('NULO')
# Set the 'Name' column as the index
df_1 = df_1.set_index('Nº RM')
# Reset the index
df_1 = df_1.reset_index()
#Eliminando coluna indesejada
df_1 = df_1.drop(['Unnamed: 38'], axis=1)


df_1.to_csv('REVISTA_MAHIKARI_HOSSA.csv', sep=';' , decimal='.')


data = pd.read_csv('REVISTA_MAHIKARI_HOSSA.csv', sep=';')

#Alterando os tipos de dados
data = data.drop(['Unnamed: 0'], axis=1)
data['Nº RM'] = data['Nº RM'].astype(str)
data['ANO'] = data['ANO'].astype(str)
data['Nº RM'] = data['Nº RM'].astype(str)

# Aplicando a função para remover acentos na coluna desejada
data['PRINCÍPIOS DIVINOS'] = data['PRINCÍPIOS DIVINOS'].apply(remover_acentos)
data['SUNKYO'] = data['SUNKYO'].apply(remover_acentos)
data['GOSEIGEN'] = data['GOSEIGEN'].apply(remover_acentos)
data['ENSINAMENTO OSHIENUSHISAMA'] = data['ENSINAMENTO OSHIENUSHISAMA'].apply(remover_acentos)
data['ENSINAMENTO SUKUINUSHISAMA'] = data['ENSINAMENTO SUKUINUSHISAMA'].apply(remover_acentos)
data['DEPOIMENTOS / RELATOS DE EXPERIÊNCIAS'] = data['DEPOIMENTOS / RELATOS DE EXPERIÊNCIAS'].apply(remover_acentos)
data['EXTRAS.1'] = data['EXTRAS.1'].apply(remover_acentos)
data['AGRICULTURA YOKO'] = data['AGRICULTURA YOKO'].apply(remover_acentos)
data['MAHIKARI-TAI.1'] = data['MAHIKARI-TAI.1'].apply(remover_acentos)
data['TORNAR-SE UMA PESSOA QUE RECEBE PROVIDÊNCIAS DE DEUS'] = data['TORNAR-SE UMA PESSOA QUE RECEBE PROVIDÊNCIAS DE DEUS'].apply(remover_acentos)
data['VOZ DA FELICIDADE'] = data['VOZ DA FELICIDADE'].apply(remover_acentos)
data['NO CAMINHO DO AMOR E DA SINCERIDADE'] = data['NO CAMINHO DO AMOR E DA SINCERIDADE'].apply(remover_acentos)
data['FÓRUM DA CRUZ PARA REFLETIR SOBRE O SÉCULO XXI'] = data['FÓRUM DA CRUZ PARA REFLETIR SOBRE O SÉCULO XXI'].apply(remover_acentos)
data['ECOA DO TEMPLO MUNDIAL SUZA O SINO DA AURORA DA CIVILIZAÇÃO ESPIRITUALISTA'] = data['ECOA DO TEMPLO MUNDIAL SUZA O SINO DA AURORA DA CIVILIZAÇÃO ESPIRITUALISTA'].apply(remover_acentos)
data['PRÁTICA DAS NORMAS DE CONDUTA E BOAS MANEIRAS DO KAMI-KUMITE'] = data['PRÁTICA DAS NORMAS DE CONDUTA E BOAS MANEIRAS DO KAMI-KUMITE'].apply(remover_acentos)
data['UM PASSO DE ELEVAÇÃO'] = data['UM PASSO DE ELEVAÇÃO'].apply(remover_acentos)
data['A GLÓRIA DE VIVER DEDICANDO-SE NA TERRA SAGRADA'] = data['A GLÓRIA DE VIVER DEDICANDO-SE NA TERRA SAGRADA'].apply(remover_acentos)
data['BRILHEM EXERCENDO OS TRÊS PAPÉIS DA EXPANSÃO'] = data['BRILHEM EXERCENDO OS TRÊS PAPÉIS DA EXPANSÃO'].apply(remover_acentos)
data['RUMO AO NOVO, VERDADEIRO E SAGRADO SÉCULO XXI'] = data['RUMO AO NOVO, VERDADEIRO E SAGRADO SÉCULO XXI'].apply(remover_acentos)
data['RUMO À ECONOMIA ESPIRITUALISTA DO SAGRADO SÉCULO XXI'] = data['RUMO À ECONOMIA ESPIRITUALISTA DO SAGRADO SÉCULO XXI'].apply(remover_acentos)
data['A RETRIBUIÇÃO A DEUS E A SALVAÇÃO DAS PESSOAS'] = data['A RETRIBUIÇÃO A DEUS E A SALVAÇÃO DAS PESSOAS'].apply(remover_acentos)
data['IMAGEM DA VONTADE CELESTIAL'] = data['IMAGEM DA VONTADE CELESTIAL'].apply(remover_acentos)
data['FONTE DE MILAGRES'] = data['FONTE DE MILAGRES'].apply(remover_acentos)
data['SER PRECURSOR NA SALVAÇÃO DO MUNDO, NA ABERTURA DO NOVO E SAGRADO SÉCULO'] = data['SER PRECURSOR NA SALVAÇÃO DO MUNDO, NA ABERTURA DO NOVO E SAGRADO SÉCULO'].apply(remover_acentos)
data['LUZ DO AMOR'] = data['LUZ DO AMOR'].apply(remover_acentos)
data['VIDAS QUE BRILHAM COM AL LUZ DE DEUS'] = data['VIDAS QUE BRILHAM COM AL LUZ DE DEUS'].apply(remover_acentos)
data['SUKUINUSHI-SAMA, OS 100 ANOS DO SEU NASCIMENTO'] = data['SUKUINUSHI-SAMA, OS 100 ANOS DO SEU NASCIMENTO'].apply(remover_acentos)
data['A FORMAÇÃO DE DEZ MIL PESSOAS DA CIVILIZAÇAO ESPIRITUALISTA'] = data['A FORMAÇÃO DE DEZ MIL PESSOAS DA CIVILIZAÇAO ESPIRITUALISTA'].apply(remover_acentos)
data['EXTRAS.2'] = data['EXTRAS.2'].apply(remover_acentos)
data['FAZENDA YOKO'] = data['FAZENDA YOKO'].apply(remover_acentos)
data['DIÁLOGO ENTRE MÃE E FILHO'] = data['DIÁLOGO ENTRE MÃE E FILHO'].apply(remover_acentos)
data['A FÉ VOLTADA A DEUS E A EDUCAÇÃO DA LEI DA VERDADE'] = data['A FÉ VOLTADA A DEUS E A EDUCAÇÃO DA LEI DA VERDADE'].apply(remover_acentos)
data['O CAMINHO PARA SE TORNAR SEMENTE DO SAGRADO SÉCULO XXI'] = data['O CAMINHO PARA SE TORNAR SEMENTE DO SAGRADO SÉCULO XXI'].apply(remover_acentos)
data['CULTIVANDO AS SEMENTES DA PRÓXIMA GERAÇÃO'] = data['CULTIVANDO AS SEMENTES DA PRÓXIMA GERAÇÃO'].apply(remover_acentos)
data['MAHIKARI-TAI 2'] = data['MAHIKARI-TAI 2'].apply(remover_acentos)

data = data.reset_index(drop=True).applymap(lambda x: x.upper())

#df_1.to_csv('REVISTA_MAHIKARI_HOSSA_copia.csv', sep=';' , decimal='.')
#data.to_csv('REVISTA_MAHIKARI_HOSSA.csv', sep=';' , decimal='.')

#MONTANDO O STREAMLIT APP-site
#Configurando a aparência do Gráfico default
st.set_page_config(page_title='Catalogo Revistas SUKYO MAHIKARI',
                   page_icon='🌟',
                   layout='wide',
                   initial_sidebar_state='expanded',
                   )

image = Image.open('./img/goshimon.png')
st.image(image, caption=None, use_column_width=True, clamp=False, channels="RGB", output_format="png")

st.markdown("<h1 style='text-align: center; color: orange;'>CATALOGO REVISTAS - SUKYO MAHIKARI</h1>", unsafe_allow_html=True)
st.subheader('',divider='rainbow')

def main():


    # Crie a interface do streamlit
    st.subheader('Busca por palavra-chave')

    # Pede ao usuário para inserir a palavra-chave
    palavra_chave = st.text_input('Digite a palavra-chave e tecle "ENTER":')
    palavra_chave = palavra_chave.upper()
    st.caption('Obs.: A palavra-chave deve ser preenchida ignorando acentuação, ex. "divinização" deverá ser escrito como "divinizacao"')
    # Pede ao usuário para escolher a coluna em que deseja pesquisar
    
    coluna_escolhida = st.selectbox('Escolha em qual seção da revista deseja pesquisar:', data.columns)

    # Filtra o dataframe com base na palavra-chave e na coluna escolhida
    result_df = ''
    if palavra_chave and coluna_escolhida:
        resultado = data[data[coluna_escolhida].str.contains(palavra_chave)]
        result_df = resultado[['Nº RM', 'MÊS', 'ANO', coluna_escolhida]]

    else:
        st.table(data['SUNKYO'])
        
    with st.spinner('Buscando..'):
        time.sleep(1.7)
    st.success('O resultado da sua busca esta logo abaixo. Dōmo arigatōgozaimasu!')

    #st.dataframe(result_df.set_index(result_df.columns[0]))
    st.dataframe(result_df, hide_index=True, column_order=None, column_config=None)

main()

