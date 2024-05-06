# %% [markdown]
# Ce fichier servira a importer les données des tableurs excel

# %%
import pandas as pd

# %% [markdown]
# Importation des données brutes

# %%
brut_data_filepath="..\Data\data_brut.xlsx"

brut_df=pd.read_excel(brut_data_filepath) #On convertit le fichier excel en DataFrame

# %% [markdown]
# Mise en forme de dictionnaire des données brutes

# %%
nb_lignes_brut=len(brut_df.index)   #nombre de lignes du tableur excel/DataFrame

nb_colonnes_brut=len(brut_df.columns)   #nombre de colonnes du tableur excel/DataFrame

brut_dict={}    #on initialise un dictionnaire vide

for i in range(0,nb_lignes_brut):   #on parcourt les lignes 
    key=brut_df.iloc[i][0]          #on associe key au libellé de la ligne

    if key not in brut_dict:        #s'il n'existe pas de key correspondant au libellé
        brut_dict[key]=[]           #on initialise la clé avec une liste vide

    for j in range(1,nb_colonnes_brut):             #on parcourt les colonnes de la ligne i
        brut_dict[key].append(brut_df.iloc[i][j])   #on ajoute chaque valeur à la liste vide précédemment crée


# %% [markdown]
# Importation des données CVS-CJO

# %%
cvs_cjo_data_filepath="..\Data\CVS_CJO_data.xlsx"

cvs_cjo_df=pd.read_excel(cvs_cjo_data_filepath) #On convertit le fichier excel en DataFrame

# %% [markdown]
# Mise en forme de dictionnaire des données CVS_CJO

# %%
nb_lignes_cvs_cjo=len(cvs_cjo_df.index)   #nombre de lignes du tableur excel/DataFrame

nb_colonnes_cvs_cjo=len(cvs_cjo_df.columns)   #nombre de colonnes du tableur excel/DataFrame

cvs_cjo_dict={}    #on initialise un dictionnaire vide

for i in range(0,nb_lignes_cvs_cjo):   #on parcourt les lignes 
    key=cvs_cjo_df.iloc[i][0]          #on associe key au libellé de la ligne

    if key not in cvs_cjo_dict:        #s'il n'existe pas de key correspondant au libellé
        cvs_cjo_dict[key]=[]           #on initialise la clé avec une liste vide

    for j in range(1,nb_colonnes_cvs_cjo):             #on parcourt les colonnes de la ligne i
        cvs_cjo_dict[key].append(cvs_cjo_df.iloc[i][j])   #on ajoute chaque valeur à la liste vide précédemment crée

#print(cvs_cjo_dict["Indice CVS-CJO de la production industrielle (base 100 en 2015) - Extraction d\'hydrocarbures (NAF rév. 2, niveau division, poste 06)"])   #test


