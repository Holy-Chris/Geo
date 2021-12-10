# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import
import csv
import pandas as pd

import os

# Ouverture des txt
fd = "D:\\OneDrive\\Cours\\Master 2 - TELENVI\\S3\\Modélisation climatique\\Modèles_DINARD"

## Chaque sous-dossier contient 1 modèle
fd_danish = "D:\\OneDrive\\Cours\\Master 2 - TELENVI\\S3\\Modélisation climatique\\Modèles_DINARD\\DANISH"
fd_aladin = "D:\\OneDrive\\Cours\\Master 2 - TELENVI\\S3\\Modélisation climatique\\Modèles_DINARD\\ALADIN63_CNRM-CM5"
fd_ipsl = "D:\\OneDrive\\Cours\\Master 2 - TELENVI\\S3\\Modélisation climatique\\Modèles_DINARD\\IPSL"

namestxt = []

for path, subdirs, files in os.walk(fd_danish):
    for name in files:
        # NCC ==> Nom de fichier pour le modèle danois
        if "NCC" in name and "txt" in name:
            if "4.5" in name:
                ncc_45 = os.path.join(fd_danish,name)
                namestxt.append(ncc_45)
            if "Historical" in name:
                ncc_his = os.path.join(fd_danish,name)
                namestxt.append(ncc_his)
            if "8.5" in name:
                ncc_85 = os.path.join(fd_danish,name)
                namestxt.append(ncc_85)

for path, subdirs, files in os.walk(fd_aladin):
    for name in files:
        if "ALADIN" in name and "txt" in name:
            if "4.5" in name:
                aladin_45 = os.path.join(fd_aladin,name)
                namestxt.append(aladin_45)
            if "Historical" in name:
                aladin_his = os.path.join(fd_aladin,name)
                namestxt.append(aladin_his)
            if "8.5" in name:
                aladin_85 = os.path.join(fd_aladin,name)
                namestxt.append(aladin_85)
                
for path, subdirs, files in os.walk(fd_ipsl):
    for name in files:
        if "IPSL" in  name and "txt" in name:
            if "4.5" in name:
                ipsl_45 = os.path.join(fd_ipsl,name)
                namestxt.append(ipsl_45)
            if "Historical" in name:
                ipsl_his = os.path.join(fd_ipsl,name)
                namestxt.append(ipsl_his)
            if "8.5" in name:
                ipsl_85 = os.path.join(fd_ipsl,name)
                namestxt.append(ipsl_85)

namestxt


            ##### SUPPRESSION LIGNES INUTILES DE L'EN-TETE #####

import shutil

csv_liste = []


for elem in namestxt:    
    # defining object file1 to
    # open file1 in
    # read mode
    file1 = open(elem,'r')

    # defining object file2 to
    # open file2
    # in write mode ==> Créé le fichier dans le dossier fd 
    temp_file = shutil.copy(elem,fd,follow_symlinks=True)
    file2 = open(temp_file,'w')


    # reading each line from original
    # text file

    for line in file1.readlines():
    # reading all lines that do not
    # begin with "#"
        if not (line.startswith('#')):
            # printing those lines
            ## print(line)
            # storing only those lines that
            # do not begin with "#"
            file2.write(line)
    
    
    # close and save the files
    file2.close()
    file1.close()
    
    # Remplace le fichier d'origine par le fichier créé
    shutil.move(temp_file,elem)
    
    csv_liste.append(temp_file)


# reading given csv file
# and creating dataframe
# + ajout nom de colonnes
namescsv = []
for elem in namestxt:
    df = pd.read_csv(elem,sep=";", header=None, error_bad_lines=False)
    df
    namescsv.append(os.path.join(elem[:-4]+".csv"))
    # Ici, je rajoute la colonne "neige" car j'ai téléchargé les modèles avec cette donnée. 
    # Si toi t'as pas les données neige, supprime juste le dernier élément de la liste ci-dessous
    df.columns = ['JJ','MM','AAAA','Lat','Long','Tmin','Tmax','Tmoy','Pluie','Neige']
    df.to_csv(os.path.join((elem[:-4]+".csv")),header=True,index=None,sep=";")
