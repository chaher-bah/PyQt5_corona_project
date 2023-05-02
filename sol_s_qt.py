import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
import csv
import os
from datetime import datetime
from PyQt5 import QtCore
def ajouter_personne_dialog():
    dialog = QDialog()
    dialog.setWindowTitle("Ajouter une personne")
    dialog.resize(400, 400)
    dialog.setStyleSheet("background-color: rgb(198, 195, 161);")
    cin_label = QLabel("CIN:")
    cin_edit = QLineEdit()
    nom_label = QLabel("Nom:")
    nom_edit = QLineEdit()
    prenom_label = QLabel("Prenom:")
    prenom_edit = QLineEdit()
    age_label = QLabel("Age:")
    age_edit = QLineEdit()
    adresse_label = QLabel("Adresse:")
    adresse_edit = QLineEdit()
    nationalite_label = QLabel("Nationalité:")
    nationalite_edit = QLineEdit()
    nationalite_edit.setPlaceholderText("exp;Tun/Fr/Alg")
    telephone_label = QLabel("Téléphone:")
    telephone_edit = QLineEdit()
    d_infection_label = QLabel("Date d'infection:")
    d_infection_edit = QLineEdit()
    d_infection_edit.setPlaceholderText("jj/mm/aaaa")
    decede_label = QLabel("Décédé:")
    decede_edit = QLineEdit()
    decede_edit.setPlaceholderText("ecrire 1 si oui , 0 sinon")
    ajouter_button = QPushButton("Ajouter")
    annuler_button = QPushButton("Annuler")
    def on_ajouter_clicked():
        cin = cin_edit.text()
        nom = nom_edit.text()
        prenom = prenom_edit.text()
        age = age_edit.text()
        nationalite = nationalite_edit.text()
        telephone = telephone_edit.text()
        adresse= adresse_edit.text()
        d_infection = d_infection_edit.text()
        decede = decede_edit.text()
        if decede not in ['0', '1']:
            QMessageBox.warning(dialog, "Attention", "La valeur pour le champ 'décédé' doit être 0 ou 1.")
            return
        if len (cin)!=12:
            QMessageBox.warning(dialog, "Attention", "Les valeur pour le champ'CIN'  doit être 12 caractére.")
            return
        if cin.isalpha() or age.isalpha() or telephone.isalpha():
            QMessageBox.warning(dialog, "Attention", "Les valeur pour les champs 'CIN' 'age' 'Tel' doit être numérique.")
            return
        try:
            jour, mois, annee = d_infection.split('/')
            jour = int(jour)
            mois = int(mois)
            annee = int(annee)
            if not (1 <= jour <= 31 and 1 <= mois <= 12 and 1900 <= annee <= 2100):
                QMessageBox.warning(dialog, "Attention", "le champ d_infectin doit être de la forme jj/mm/aaaa .")
                return        
        except:
            QMessageBox.warning(dialog, "Attention", "le champ d_infectin doit être de la forme jj/mm/aaaa .")
            return
        with open('data.csv', 'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([cin, nom, prenom, age, nationalite, telephone, d_infection,adresse, decede])
            QMessageBox.information(dialog,"Info","Une Personne a été ajouter au BD")
    button_layout = QHBoxLayout()
    button_layout.addWidget(ajouter_button)
    button_layout.addWidget(annuler_button)
    field_layout = QVBoxLayout()
    field_layout.addWidget(cin_label)
    field_layout.addWidget(cin_edit)
    field_layout.addWidget(nom_label)
    field_layout.addWidget(nom_edit)
    field_layout.addWidget(prenom_label)
    field_layout.addWidget(prenom_edit)
    field_layout.addWidget(age_label)
    field_layout.addWidget(age_edit)
    field_layout.addWidget(adresse_label)
    field_layout.addWidget(adresse_edit)
    field_layout.addWidget(nationalite_label)
    field_layout.addWidget(nationalite_edit)
    field_layout.addWidget(telephone_label)
    field_layout.addWidget(telephone_edit)
    field_layout.addWidget(d_infection_label)
    field_layout.addWidget(d_infection_edit)
    field_layout.addWidget(decede_label)
    field_layout.addWidget(decede_edit)
    field_layout.addLayout(button_layout)
    dialog.setLayout(field_layout)
    ajouter_button.clicked.connect(on_ajouter_clicked)
    annuler_button.clicked.connect(dialog.reject)
    dialog.exec_()
def modif_personne_dialog():
    d=QDialog()
    d.setWindowTitle("Modifier personne")
    d.setMinimumWidth(400)
    d.setMinimumHeight(350)
    d.setMaximumWidth(400)
    d.setMaximumHeight(350)
    d.setStyleSheet("background-color: rgb(209, 239, 246);")
    titre=QLabel("Menu Modification")
    titre.setStyleSheet('font: 12pt "Copperplate Gothic Bold";')
    titre.setMinimumWidth(221)
    titre.setMinimumHeight(30)
    t2=QLabel("Modifier par Telephone")
    t2.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t2.setMinimumWidth(221)
    t2.setMinimumHeight(30)
    nom = QLineEdit()
    nom.setPlaceholderText("Nom")
    nom.setStyleSheet('background-color: rgb(117, 158, 168);')
    nom.setMinimumWidth(110)
    nom.setMinimumHeight(30)
    prenom = QLineEdit()
    prenom.setPlaceholderText("Prenom")
    prenom.setStyleSheet('background-color: rgb(117, 158, 168);')
    prenom.setMaximumHeight(30)
    tel = QLineEdit()
    tel.setPlaceholderText("Nouveau Tel")
    tel.setStyleSheet('background-color: rgb(117, 158, 168);')
    tel.setMinimumWidth(120)
    tel.setMinimumHeight(30)
    btn = QPushButton("Modifier")
    btn.setStyleSheet('background-color: rgb(117, 158, 168);')
    t3=QLabel("Modifier par Adresse")
    t3.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t3.setMinimumWidth(221)
    t3.setMinimumHeight(30)
    nom1 = QLineEdit()
    nom1.setPlaceholderText("Nom")
    nom1.setStyleSheet('background-color: rgb(117, 158, 168);')
    nom1.setMinimumWidth(110)
    nom1.setMinimumHeight(30)
    prenom1 = QLineEdit()
    prenom1.setPlaceholderText("Prenom")
    prenom1.setStyleSheet('background-color: rgb(117, 158, 168);')
    prenom1.setMaximumHeight(30)
    btn2 = QPushButton("Modifier")
    btn2.setStyleSheet('background-color: rgb(117, 158, 168);')
    add= QLineEdit()
    add.setPlaceholderText("Nouvelle Adresse")
    add.setStyleSheet('background-color: rgb(117, 158, 168);')
    add.setMinimumWidth(120)
    add.setMinimumHeight(30)
    res1=QLabel()
    res1.setMinimumWidth(250)
    res1.setMinimumHeight(30)
    res2=QLabel()
    res2.setMinimumWidth(250)
    res2.setMinimumHeight(30)
    def on_modifier1_clicked():
        n = nom.text()
        p = prenom.text()
        new_tel = tel.text()
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
            t = False
            for row in rows:
                if row[1] == n and row[2] == p:
                    row[5]=new_tel
                    t = True
                    break
            if t:
                with open("data.csv", "w",newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)
                res1.setText(f"Tél de {p} {n} a été modifié avec succès !")
            else:
                res1.setText("Personne n'exicte pas")
    def on_modifier2_clicked():
        n = nom1.text()
        p = prenom1.text()
        new_add = add.text()
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
            t = False
            for row in rows:
                if row[1] == n and row[2] == p:
                    row[7]=new_add
                    t = True
                    break
            if t:
                with open("data.csv", "w",newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)
                res2.setText(f"adresse de {p} {n} a été modifié avec succès !")
            else:
                res2.setText("Personne n'exicte pas")
    leyout=QGridLayout()
    leyout.addWidget(titre,0,1)
    leyout.addWidget(t2,1,0)
    leyout.addWidget(t3,5,0)
    leyout.addWidget(nom,2,0)
    leyout.addWidget(prenom,2,1)
    leyout.addWidget(nom1,6,0)
    leyout.addWidget(prenom1,6,1)
    leyout.addWidget(tel,2,2)
    leyout.addWidget(add,6,2)
    leyout.addWidget(btn,3,1)
    leyout.addWidget(btn2,7,1)
    leyout.addWidget(res1,4,0)
    leyout.addWidget(res2,8,0)
    btn.clicked.connect(on_modifier1_clicked)
    btn2.clicked.connect(on_modifier2_clicked)
    d.setLayout(leyout)
    d.exec_()   
def supp_personne_dialog():
    d=QDialog()
    d.setWindowTitle("Supprimer personne")
    d.setMinimumWidth(400)
    d.setMinimumHeight(300)
    d.setMaximumWidth(400)
    d.setMaximumHeight(300)
    d.setStyleSheet("background-color: rgb(209, 239, 246);")
    titre=QLabel("Menu suppression")
    titre.setStyleSheet('font: 12pt "Copperplate Gothic Bold";')
    titre.setMinimumWidth(221)
    titre.setMinimumHeight(30)
    t2=QLabel("Suppression personne donné;")
    t2.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t2.setMinimumWidth(221)
    t2.setMinimumHeight(30)
    nom = QLineEdit()
    nom.setPlaceholderText("Nom")
    nom.setStyleSheet('background-color: rgb(117, 158, 168);')
    nom.setMaximumWidth(110)
    nom.setMaximumHeight(30)
    prenom = QLineEdit()
    prenom.setPlaceholderText("Prenom")
    prenom.setStyleSheet('background-color: rgb(117, 158, 168);')
    prenom.setMaximumWidth(110)
    prenom.setMaximumHeight(30)
    btn = QPushButton("Supprimer")
    btn.setStyleSheet('background-color: rgb(117, 158, 168);')
    x = QLabel()
    x.setStyleSheet("background-color: rgb(117, 158, 168);")
    t3=QLabel("Suppression des personnes d'une nationalité donnée;")
    t3.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t3.setMinimumWidth(351)
    t3.setMinimumHeight(30)
    nati = QLineEdit()
    nati.setPlaceholderText("Nationlité")
    nati.setStyleSheet('background-color: rgb(117, 158, 168);')
    nati.setMaximumWidth(110)
    nati.setMaximumHeight(30)
    btn2 = QPushButton("Supprimer")
    btn2.setStyleSheet('background-color: rgb(117, 158, 168);')
    btn2.setMaximumWidth(110)
    btn2.setMaximumHeight(30)
    t4=QLabel("Suppression des personnes d'un indicatif* donné;")
    t4.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t4.setMinimumWidth(351)
    t4.setMinimumHeight(30)
    tel = QLineEdit()
    tel.setPlaceholderText("Téléphone (*ind)")
    tel.setStyleSheet('background-color: rgb(117, 158, 168);')
    tel.setMaximumWidth(110)
    tel.setMaximumHeight(30)
    btn3 = QPushButton("Supprimer")
    btn3.setStyleSheet('background-color: rgb(117, 158, 168);')
    btn3.setMaximumWidth(110)
    btn3.setMaximumHeight(30)
    res=QLabel()
    res.setMinimumWidth(200)
    res.setMinimumHeight(30)
    t5=QLabel("exp ind; +216")
    def on_supprimer_clicked():
        n = nom.text()
        p = prenom.text()
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
            t = False
            for row in rows:
                if row[1] == n and row[2] == p:
                    rows.remove(row)
                    t = True
                    break
            if t:
                with open("data.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)
                res.setText("Action terminée : Personne supprimée avec succès")
            else:
                res.setText("Personne n'existe pas")
    def on_supprimer2_clicked():
        n=nati.text()
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
        t = False
        for row in rows:
            if row[4] == n:
                rows.remove(row)
                t = True
        if t:
            with open("data.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(rows)
        if t:
            res.setText("Les personnes ont été supprimées avec succès !")
        else:
            res.setText("Aucune personne de cette nationalité n'a été trouvée.")
    def on_supprimer3_clicked():
        ind=tel.text()
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
        t = False
        for row in rows:
            if row[5].startswith(ind):
                rows.remove(row)
                t = True
        if t:
            with open("data.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(rows)
        if t:
            res.setText("Les personnes ont été supprimées avec succès !")
        else:
            res.setText("Aucune personne de cette indicatif n'a été trouvée.")
    leyout=QGridLayout()
    leyout.addWidget(titre,0,1)
    leyout.addWidget(t2,1,0)
    leyout.addWidget(t3,3,0)
    leyout.addWidget(t4,5,0)
    leyout.addWidget(t5,6,2)
    leyout.addWidget(nom,2,0)
    leyout.addWidget(nati,4,0)
    leyout.addWidget(tel,6,0)
    leyout.addWidget(prenom,2,1)
    leyout.addWidget(btn,2,2)
    btn.clicked.connect(on_supprimer_clicked)
    leyout.addWidget(btn2,4,1)
    btn2.clicked.connect(on_supprimer2_clicked)
    leyout.addWidget(btn3,6,1)
    btn3.clicked.connect(on_supprimer3_clicked)
    leyout.addWidget(x,4,3)
    leyout.addWidget(res,7,1)
    d.setLayout(leyout)
    d.exec_()
def dict_p_dialog():
    d=QDialog()
    d.setWindowTitle("Dictionnaire personne")
    d.setMinimumWidth(700)
    d.setMinimumHeight(510)
    d.setMaximumWidth(70)
    d.setMaximumHeight(510)
    d.setStyleSheet("background-color: rgb(171,120,171);")
    titre=QLabel("Dictionnaire des Personnes")
    titre.setStyleSheet('font: 12pt "Copperplate Gothic Bold";')
    titre.setMinimumWidth(221)
    titre.setMinimumHeight(30)
    continu=QLabel()
    continu.setMinimumWidth(650)
    continu.setMinimumHeight(401)
    btn = QPushButton("Afficher")
    btn.setStyleSheet('background-color: rgb(204,204,204);')
    btn.setMinimumWidth(90)
    btn.setMinimumHeight(30)
    def afficher_personnes():
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            rows=[row for row in reader]
            personnes = []
            for row in rows:
                personnes.append({
                    "CIN": row[0],
                    "Nom": row[1],
                    "Prenom": row[2],
                    "Age": row[3],
                    "Nationalite": row[4],
                    "TEL": row[5],
                    "D_infection": row[6],
                    "Decede": row[8]
                })
        text = ("{:<20}   {:<18}  {:<18}  {:<10} {:<15} {:<20} {:<15} {:<5} \n".format("CIN", "Nom", "Prenom", "Age","Nationalite","Telephone", "D_infection" , "Decede"))
        for personne in personnes:
            text +=("{:<20} {:^18} {:^18}   {:^10} {:^15} {:^20} {:^15}\t \t{:>5} \n".format(personne['CIN'],personne['Nom'] , personne['Prenom'], personne['Age'] ,personne['Nationalite'], personne['TEL'],personne['D_infection'] ,personne['Decede']))
        continu.setText(text)
    continu.setStyleSheet('font: 75 10pt "MS Sans Serif";background-color: rgb(230,240,230);')
    btn2 = QPushButton("Effacer tous")
    btn2.setStyleSheet('background-color: rgb(204, 204, 204);')
    btn2.setMinimumWidth(90)
    btn2.setMinimumHeight(30)
    def effacer_toutes():
        if os.path.exists("data.csv"):
            os.remove("data.csv")
            with open("data.csv", "w"):
                pass
            continu.setText("Toutes les données ont été supprimées avec succès.")
        else:
            continu.setText("Le fichier 'data.csv' n'existe pas.")
    btn.clicked.connect(afficher_personnes)
    btn2.clicked.connect(effacer_toutes)
    leyout=QGridLayout()
    d.setLayout(leyout)
    leyout.addWidget(titre,0,1)
    leyout.addWidget(continu,1,1)
    leyout.addWidget(btn,2,1)
    leyout.addWidget(btn2,2,2)
    d.exec_()
def rech_p_dialog():
    d=QDialog()
    d.setWindowTitle("Recherche personne")
    d.setMinimumWidth(700)
    d.setMinimumHeight(700)
    d.setMaximumWidth(700)
    d.setMaximumHeight(700)
    d.setStyleSheet("background-color: rgb(147, 32, 18);")
    t=QLabel("Recherche personne par Tel;")
    t.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t.setMinimumWidth(221)
    t.setMinimumHeight(30)
    tel = QLineEdit()
    tel.setPlaceholderText("Tele")
    tel.setStyleSheet('background-color: rgb(233, 216, 166);')
    tel.setMaximumWidth(110)
    tel.setMaximumHeight(30)
    btn = QPushButton("Recherche")
    btn.setStyleSheet('background-color: rgb(233, 216, 170);')
    btn.setMaximumWidth(110)
    btn.setMaximumHeight(30)
    res=QLabel()
    res.setMinimumWidth(650)
    res.setMinimumHeight(35)
    res.setStyleSheet('background-color: rgb(233, 216, 166);')
    def rech_tel():
        nbr=tel.text()
        txt = ("{:<18} {:<18} {:<18} {:<10} {:<15} {:<20} {:<15} {:<5} \n".format("CIN", "Nom", "Prenom", "Age","Nationalite","Telephone", "D_infection" , "Decede"))
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
            v = False
            for row in rows:
                if row[5] == nbr:
                    v=True
                    txt +=( "{:<18} {:<18} {:<18} {:<10} {:<15} {:<20} {:<15}\t {:<5}".format(row[0],row[1] , row[2], row[3] ,row[4], row[5],row[6] ,row[8]))
                    break
        if v:
            res.setText(txt)
        else:
            res.setText(f"Personne n'exicte pas avec nbr {nbr}")
    t2=QLabel("Recherche personne par Indic;")
    t2.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t2.setMinimumWidth(218)
    t2.setMinimumHeight(30)
    ind = QLineEdit()
    ind.setPlaceholderText("indic")
    ind.setStyleSheet('background-color: rgb(233, 216, 166);')
    ind.setMaximumWidth(110)
    ind.setMaximumHeight(30)
    btn2 = QPushButton("Recherche")
    btn2.setStyleSheet('background-color: rgb(233, 216, 170);')
    btn2.setMaximumWidth(100)
    btn2.setMaximumHeight(30)
    def indicatif ():
        ligne=0
        p_trouvee=[]
        id=ind.text()
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
        t = False
        for row in rows:
            if row[5].startswith(id):
                p_trouvee.append(row[:7])
                t = True
        if t:
            teb.setRowCount(len(p_trouvee))
            for i, row in enumerate(p_trouvee):
                for j, col in enumerate(row):
                    teb.setItem(i, j, QTableWidgetItem(col))
        else:
            res.setText("indic ne pas trouvee")       
    t3=QLabel("Recherche personne par Nationalité;")
    t3.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t3.setMinimumWidth(218)
    t3.setMinimumHeight(30)
    nati = QLineEdit()
    nati.setPlaceholderText("Nationalité")
    nati.setStyleSheet('background-color: rgb(233, 216, 166);')
    nati.setMaximumWidth(100)
    nati.setMaximumHeight(30)
    btn3 = QPushButton("Recherche")
    btn3.setStyleSheet('background-color: rgb(233, 216, 170);')
    btn3.setMaximumWidth(110)
    btn3.setMaximumHeight(30)
    def rech_n ():
        ligne=0
        p_n_trouvee=[]
        n=nati.text()
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
        t = False
        for row in rows:
            if row[4]==n:
                p_n_trouvee.append(row[:7])
                t = True
        if t:
            teb.setRowCount(len(p_n_trouvee))
            for i, row in enumerate(p_n_trouvee):
                for j, col in enumerate(row):
                    teb.setItem(i, j, QTableWidgetItem(col))
        else:
            res.setText("Nationalité ne pas trouvee")  
    t4=QLabel("Recherche personnes Décédés;")
    t4.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t4.setMinimumWidth(218)
    t4.setMinimumHeight(30)
    btn4 = QPushButton("Recherche")
    btn4.setStyleSheet('background-color: rgb(233, 216, 170);')
    btn4.setMaximumWidth(110)
    btn4.setMaximumHeight(30)
    def decede ():
        ligne=0
        p_decede=[]
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
        t = False
        for row in rows:
            if row[8]=="1":
                p_decede.append(row[:7])
                t = True
        if t:
            teb.setRowCount(len(p_decede))
            for i, row in enumerate(p_decede):
                for j, col in enumerate(row):
                    teb.setItem(i, j, QTableWidgetItem(col))
        else:
            res.setText("Aucun personne est décédé")   
    t5=QLabel("Recherche personnes non décédés;")
    t5.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t5.setMinimumWidth(218)
    t5.setMinimumHeight(30)
    btn5 = QPushButton("Recherche")
    btn5.setStyleSheet('background-color: rgb(233, 216, 170);')
    btn5.setMaximumWidth(110)
    btn5.setMaximumHeight(30)
    def n_decede ():
        ligne=0
        p_ndecede=[]
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
        t = False
        for row in rows:
            if row[8]!="1":
                p_ndecede.append(row[:7])
                t = True
        if t:
            teb.setRowCount(len(p_ndecede))
            for i, row in enumerate(p_ndecede):
                for j, col in enumerate(row):
                    teb.setItem(i, j, QTableWidgetItem(col))
        else:
            res.setText("Aucun personne est non décédé") 
    teb=QTableWidget()
    teb.setMinimumWidth(688)
    teb.setMinimumHeight(380)
    teb.setColumnCount(7)
    teb.setHorizontalHeaderLabels(["CIN","Nom","Prenom","Age","Nationalité","Téléphone","Date infection"])
    teb.setStyleSheet('font: 75 9pt "Rockwell";background-color: rgb(233, 216, 170)')
    btn.clicked.connect(rech_tel)
    btn2.clicked.connect(indicatif)
    btn3.clicked.connect(rech_n)
    btn4.clicked.connect(decede)
    btn5.clicked.connect(n_decede)
    leyout=QGridLayout()
    leyout.addWidget(t,0,0)
    leyout.addWidget(tel,1,0)
    leyout.addWidget(btn,1,1)
    leyout.addWidget(res,2,0)
    leyout.addWidget(t2,3,0)
    leyout.addWidget(ind,4,0)
    leyout.addWidget(btn2,4,1)
    leyout.addWidget(teb,6,0)
    leyout.addWidget(t3,3,2)
    leyout.addWidget(nati,4,2)
    leyout.addWidget(btn3,4,3)
    leyout.addWidget(t4,5,0)
    leyout.addWidget(btn4,5,1)
    leyout.addWidget(btn5,5,3)
    leyout.addWidget(t5,5,2)
    d.setLayout(leyout)
    d.exec_()
#ƒ
def ajouter_m_dialog():
    d= QDialog()
    d.setWindowTitle("Ajouter une Maladie")
    d.resize(300, 200)
    d.setStyleSheet("background-color: rgb(198, 195, 161);")
    cin_label = QLabel("CIN:")
    cin_edit = QLineEdit()
    nom_label = QLabel("Nom de maladie:")
    nom_edit = QLineEdit()
    annee_label = QLabel("Num d'années:")
    annee_edit = QLineEdit()
    ajouter_button = QPushButton("Ajouter")
    annuler_button = QPushButton("Annuler")
    def on_ajouter_clicked():
        cin = cin_edit.text()
        nom = nom_edit.text()
        annee = annee_edit.text()   
        if cin.isalpha() or annee.isalpha() :
            QMessageBox.warning(d, "Attention", "Les valeur pour les champs 'CIN' 'age' 'nbr années' doit être numérique.")
            return
        cin_trouve = False
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == cin:
                    cin_trouve = True
                    break
        if not cin_trouve:
            QMessageBox.warning(d, "Attention", "Le CIN donné n'existe pas dans le fichier 'data.csv'.")
            return
        with open('data_m.csv', 'a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([cin, nom,annee])
            QMessageBox.information(d,"Info","Une Maladie a été ajoutée")
    button_layout = QHBoxLayout()
    button_layout.addWidget(ajouter_button)
    button_layout.addWidget(annuler_button)
    field_layout = QVBoxLayout()
    field_layout.addWidget(cin_label)
    field_layout.addWidget(cin_edit)
    field_layout.addWidget(nom_label)
    field_layout.addWidget(nom_edit)
    field_layout.addWidget(annee_label)
    field_layout.addWidget(annee_edit)
    field_layout.addLayout(button_layout)
    d.setLayout(field_layout)
    ajouter_button.clicked.connect(on_ajouter_clicked)
    annuler_button.clicked.connect(d.reject)
    d.exec_()
def supp_m_dialog():
    d=QDialog()
    d.setWindowTitle("Supprimer Maladies")
    d.setMinimumWidth(300)
    d.setMinimumHeight(150)
    d.setMaximumWidth(300)
    d.setMaximumHeight(150)
    d.setStyleSheet("background-color: rgb(209, 239, 246);")
    titre=QLabel("Menu suppression")
    titre.setStyleSheet('font:10pt "Copperplate Gothic Bold";')
    titre.setMinimumWidth(180)
    titre.setMinimumHeight(30)
    nom = QLineEdit()
    nom.setPlaceholderText("Nom de maladie")
    nom.setStyleSheet('background-color: rgb(117, 158, 168);')
    nom.setMinimumWidth(100)
    nom.setMinimumHeight(30)
    btn = QPushButton("Supprimer")
    btn.setStyleSheet('background-color: rgb(117, 158, 168);')
    btn.setMinimumWidth(90)
    btn.setMinimumHeight(30)
    res=QLabel()
    res.setMinimumWidth(260)
    res.setMinimumHeight(30)
    def on_supp_clicked():
        n = nom.text()
        with open("data_m.csv", "r") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
            t = False
            for row in rows:
                if row[1] == n:
                    rows.remove(row)
                    t = True
                    break
            if t:
                with open("data_m.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)
                res.setText("Action terminée : Maladie supprimée avec succès")
            else:
                res.setText("Maladie n'existe pas")
    btn.clicked.connect(on_supp_clicked)
    leyout=QGridLayout()
    leyout.addWidget(titre,0,1)
    leyout.addWidget(nom,1,0)
    leyout.addWidget(btn,1,2)
    leyout.addWidget(res,2,0)
    d.setLayout(leyout)
    d.exec_()
def modif_m_dialog():
    d=QDialog()
    d.setWindowTitle("Modifier Maladies")
    d.setMinimumWidth(400)
    d.setMinimumHeight(300)
    d.setMaximumWidth(400)
    d.setMaximumHeight(300)
    d.setStyleSheet("background-color: rgb(209, 239, 246);")
    titre=QLabel("Menu Modification")
    titre.setStyleSheet('font: 12pt "Copperplate Gothic Bold";')
    titre.setMinimumWidth(221)
    titre.setMinimumHeight(30)
    t2=QLabel("Modifier Nombre d'années")
    t2.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t2.setMinimumWidth(221)
    t2.setMinimumHeight(30)
    nom_m = QLineEdit()
    nom_m.setPlaceholderText("Nom maladie")
    nom_m.setStyleSheet('background-color: rgb(117, 158, 168);')
    nom_m.setMinimumWidth(110)
    nom_m.setMinimumHeight(30)
    c = QLineEdit()
    c.setPlaceholderText("CIN")
    c.setStyleSheet('background-color: rgb(117, 158, 168);')
    c.setMaximumHeight(30)
    nbr = QLineEdit()
    nbr.setPlaceholderText("Nouvelle nbr")
    nbr.setStyleSheet('background-color: rgb(117, 158, 168);')
    nbr.setMinimumWidth(100)
    nbr.setMinimumHeight(30)
    btn = QPushButton("Modifier")
    btn.setStyleSheet('background-color: rgb(117, 158, 168);')
    t3=QLabel("Modifier Décés(de 0 a 1)")
    t3.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t3.setMinimumWidth(221)
    t3.setMinimumHeight(30)
    cin2 = QLineEdit()
    cin2.setPlaceholderText("CIN")
    cin2.setStyleSheet('background-color: rgb(117, 158, 168);')
    cin2.setMinimumWidth(110)
    cin2.setMinimumHeight(30)
    btn2= QPushButton("Modifier")
    btn2.setStyleSheet('background-color: rgb(117, 158, 168);')
    res1=QLabel()
    res1.setMinimumWidth(300)
    res1.setMinimumHeight(30)
    res2=QLabel()
    res2.setMinimumWidth(300)
    res2.setMinimumHeight(30)
    leyout=QGridLayout()
    leyout.addWidget(titre,0,1)
    leyout.addWidget(t2,1,0)
    leyout.addWidget(nom_m,2,0)
    leyout.addWidget(c,2,1)
    leyout.addWidget(nbr,2,2)
    leyout.addWidget(btn,3,1)
    leyout.addWidget(t3,5,0)
    leyout.addWidget(cin2,6,0)
    leyout.addWidget(btn2,6,1)
    leyout.addWidget(res1,4,1)
    leyout.addWidget(res2,7,1)
    def on_m1_clicked():
        n = nom_m.text()
        id = c.text()
        new_nbr = nbr.text()
        with open("data_m.csv", "r") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
            t = False
            for row in rows:
                if row[1] == n and row[0] == id:
                    row[2]=new_nbr
                    t = True
                    break
            if t:
                with open("data_m.csv", "w",newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)
                res1.setText(f"Nbr_annees de {n} a été modifié avec succès !")
            else:
                res1.setText("Maladie n'exicte pas")
    def on_m2_clicked():
        ide = cin2.text()
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            rows = [row for row in reader]
            t = False
            for row in rows:
                if row[0] == ide:
                    row[8]=1
                    t = True
                    break
            if t:
                with open("data.csv", "w",newline='') as f:
                    writer = csv.writer(f)
                    writer.writerows(rows)
                res2.setText(f"Etat de {ide} a été modifié avec succès !")
            else:
                res2.setText("n'exicte pas")
    btn.clicked.connect(on_m1_clicked)
    btn2.clicked.connect(on_m2_clicked)
    d.setLayout(leyout)
    d.exec_()   
def dict_m_dialog():
    d=QDialog()
    d.setWindowTitle("Dictionnaire Maladies")
    d.setMinimumWidth(700)
    d.setMinimumHeight(510)
    d.setMaximumWidth(700)
    d.setMaximumHeight(510)
    d.setStyleSheet("background-color: rgb(171,120,171);")
    titre=QLabel("Dictionnaire des Maladies")
    titre.setStyleSheet('font: 12pt "Copperplate Gothic Bold";')
    titre.setMinimumWidth(221)
    titre.setMinimumHeight(30)
    continu=QLabel()
    continu.setMinimumWidth(650)
    continu.setMinimumHeight(401)
    continu.setStyleSheet("background-color: rgb(204,204,204);")
    btn = QPushButton("Afficher")
    btn.setStyleSheet('background-color: rgb(204,204,204);')
    btn.setMinimumWidth(90)
    btn.setMinimumHeight(30)
    btn2 = QPushButton("Supprimer tous")
    btn2.setStyleSheet('background-color: rgb(204,204,204);')
    btn2.setMinimumWidth(90)
    btn2.setMinimumHeight(30)
    def afficher_m():
        c=1
        with open("data_m.csv", "r",newline='') as f:
            reader = csv.reader(f)
            rows=[row for row in reader]
            m = []
            for row in rows:
                m.append({
                    "code":c,
                    "CIN": row[0],
                    "Nom_m": row[1],
                    "nbr": row[2]
                })
                c+=1
        text = ("{:<10} {:<15} {:<20}\t{:<10} \n".format("Code", "CIN", "Nom maladie", "nbr d'années"))
        for maladi in m:
            text +=( "{:^10}  {:^15} {:^20} {:>10}\n".format(maladi["code"],maladi['CIN'],maladi['Nom_m'] , maladi['nbr']))
        continu.setText(text)
    continu.setStyleSheet('font: 75 15pt "MS Sans Serif";;background-color: rgb(204,204,204);')
    def effacer_toutes():
        if os.path.exists("data_m.csv"):
            os.remove("data_m.csv")
            with open("data_m.csv", "w"):
                pass
            continu.setText("Toutes les données ont été supprimées avec succès.")
        else:
            continu.setText("Le fichier 'data_m.csv' n'existe pas.")
    btn.clicked.connect(afficher_m)
    btn2.clicked.connect(effacer_toutes)
    leyout=QGridLayout()
    d.setLayout(leyout)
    leyout.addWidget(titre,0,1)
    leyout.addWidget(continu,1,1)
    leyout.addWidget(btn,2,1)
    leyout.addWidget(btn2,2,2)
    d.exec_()  
def rech_m_dialog():
    d=QDialog()
    d.setWindowTitle("Recherche Maladies")
    d.setMinimumWidth(700)
    d.setMinimumHeight(600)
    d.setMaximumWidth(700)
    d.setMaximumHeight(600)
    d.setStyleSheet("background-color: rgb(147, 32, 18);")
    t=QLabel("Pourcentage de chaques maladies;")
    t.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t.setMinimumWidth(221)
    t.setMinimumHeight(30)
    btn = QPushButton("Recherche")
    btn.setStyleSheet('background-color: rgb(233, 216, 170);')
    btn.setMaximumWidth(110)
    btn.setMaximumHeight(30)
    res=QLabel()
    res.setMinimumWidth(400)
    res.setMinimumHeight(200)
    res.setStyleSheet('background-color: rgb(233, 216, 166);font: 75 13pt "MS Sans Serif";')
    def pourcentage ():
        maladie_count = {}
        total = 0
        with open("data_m.csv", "r") as f:
            reader = csv.reader(f)
            rows=[row for row in reader]
            for row in rows:
                maladie = row[1]
                if maladie not in maladie_count:
                    maladie_count[maladie] = 1
                else:
                    maladie_count[maladie] += 1
                total += 1
        res_text = "\t{:<20} {:<7} \n".format("Nom Maladie", "Pourcentage")
        for nom_maladie, count in maladie_count.items():
            p = (count / total) * 100
            res_text += ("\t{:<20} {:<7.2f}%\n".format(nom_maladie ,p))
        res.setText(res_text)
    t2=QLabel("Recherche maladies d'une personne;")
    t2.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t2.setMinimumWidth(221)
    t2.setMinimumHeight(30)
    c = QLineEdit()
    c.setPlaceholderText("CIN")
    c.setStyleSheet('background-color: rgb(233, 216, 166);')
    c.setMaximumWidth(110)
    c.setMaximumHeight(30)
    btn2 = QPushButton("Recherche")
    btn2.setStyleSheet('background-color: rgb(233, 216, 170);')
    btn2.setMaximumWidth(110)
    btn2.setMaximumHeight(30)
    def cin_rech ():
        cin= c.text()
        with open("data.csv", "r") as f1, open("data_m.csv", "r") as f2:
            personnes = list(csv.reader(f1))
            maladies = list(csv.reader(f2))
            personne = None
            for p in personnes:
                if p[0] == cin:
                    personne = p
                    break
            if personne is not None:
                nom, prenom,age, tel, d_infection = personne[1], personne[2],personne[3] ,personne[5], personne[6]
                maladies_personne = ", ".join([m[1] for m in maladies if m[0] == cin])
                liste.setRowCount(1)
                row=0
                liste.setItem(row, 0, QTableWidgetItem(cin))
                liste.setItem(row, 1, QTableWidgetItem(nom))
                liste.setItem(row, 2, QTableWidgetItem(prenom))
                liste.setItem(row, 3, QTableWidgetItem(age))
                liste.setItem(row, 4, QTableWidgetItem(tel))
                liste.setItem(row, 5, QTableWidgetItem(d_infection))
                liste.setItem(row, 6, QTableWidgetItem(maladies_personne))
            else:
                res.setText(f"cette CIN {cin} n'exicte pas")
    t3=QLabel("Recherche par une maladie;")
    t3.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t3.setMinimumWidth(221)
    t3.setMinimumHeight(30)
    nm= QLineEdit()
    nm.setPlaceholderText("Nom Maladie")
    nm.setStyleSheet('background-color: rgb(233, 216, 166);')
    nm.setMaximumWidth(110)
    nm.setMaximumHeight(30)
    btn3= QPushButton("Recherche")
    btn3.setStyleSheet('background-color: rgb(233, 216, 170);')
    btn3.setMaximumWidth(110)
    btn3.setMaximumHeight(30)
    def rech_m():
        n=nm.text()
        with open("data_m.csv", "r") as f:
            maladies = list(csv.reader(f))
            personnes = []
            for m in maladies:
                if m[1] == n:
                    for p in personnes:
                        if p[0] == m[0]:
                            p[5].append(m[1])
                            break
                    else:
                        with open("data.csv", "r") as f:
                            personnes_csv = list(csv.reader(f))
                            for p_csv in personnes_csv:
                                if p_csv[0] == m[0]:
                                    personne = [p_csv[0], p_csv[1], p_csv[2],p_csv[3], p_csv[5], p_csv[6], [m[1]]]
                                    personnes.append(personne)
                                    break
            if personnes:
                liste.setRowCount(len(personnes))
                for i, p in enumerate(personnes):
                    cin, nom, prenom,age, tel, d_infection, maladies_personne = p
                    liste.setItem(i, 0, QTableWidgetItem(cin))
                    liste.setItem(i, 1, QTableWidgetItem(nom))
                    liste.setItem(i, 2, QTableWidgetItem(prenom))
                    liste.setItem(i, 3, QTableWidgetItem(age))
                    liste.setItem(i, 4, QTableWidgetItem(tel))
                    liste.setItem(i, 5, QTableWidgetItem(d_infection))
                    liste.setItem(i, 6, QTableWidgetItem(str(maladies_personne)))
            else:
                res.setText(f"Aucune personne n'a la maladie {n}")
    t4=QLabel("Recherche maladies de chaque Personne;")
    t4.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t4.setMinimumWidth(221)
    t4.setMinimumHeight(30)
    btn4= QPushButton("Recherche")
    btn4.setStyleSheet('background-color: rgb(233, 216, 170);')
    btn4.setMaximumWidth(110)
    btn4.setMaximumHeight(30)
    def afficher_personnes():
        with open("data.csv", "r") as f1, open("data_m.csv", "r") as f2:
            personnes = list(csv.reader(f1))
            maladies = list(csv.reader(f2))
            liste.setRowCount(len(personnes))
            for i, p in enumerate(personnes):
                cin, nom, prenom, age, tel, d_infection = p[0],p[1],p[2],p[3],p[5],p[6]
                maladies_personne = [m[1] for m in maladies if m[0] == cin]
                if not maladies_personne:
                    maladies_personne = ["aucune M trouvée"]
                liste.setItem(i, 0, QTableWidgetItem(cin))
                liste.setItem(i, 1, QTableWidgetItem(nom))
                liste.setItem(i, 2, QTableWidgetItem(prenom))
                liste.setItem(i, 3, QTableWidgetItem(age))
                liste.setItem(i, 4, QTableWidgetItem(tel))
                liste.setItem(i, 5, QTableWidgetItem(d_infection))
                liste.setItem(i, 6, QTableWidgetItem(", ".join(maladies_personne)))
    liste=QTableWidget()
    liste.setMinimumWidth(688)
    liste.setMinimumHeight(380)
    liste.setColumnCount(7)
    liste.setHorizontalHeaderLabels(["CIN","Nom","Prenom","Age","Téléphone","Date infection","Maladies"])
    liste.setStyleSheet('font: 75 9pt "Rockwell";background-color: rgb(233, 216, 170)')
    btn.clicked.connect(pourcentage)
    btn2.clicked.connect(cin_rech)
    btn3.clicked.connect(rech_m)
    btn4.clicked.connect(afficher_personnes)
    leyout=QGridLayout()
    leyout.addWidget(t,0,0)
    leyout.addWidget(btn,1,0)
    leyout.addWidget(res,0,1)
    leyout.addWidget(t2,2,0)
    leyout.addWidget(c,3,0)
    leyout.addWidget(btn2,3,1)
    leyout.addWidget(liste,6,0)
    leyout.addWidget(t3,4,0)
    leyout.addWidget(btn3,5,1)
    leyout.addWidget(t4,4,2)
    leyout.addWidget(btn4,5,2)
    leyout.addWidget(nm,5,0)
    d.setLayout(leyout)
    d.exec_()
##€
def p_nati_dialog():
    d=QDialog()
    d.setWindowTitle("Recherche par nationalité")
    d.setMinimumWidth(700)
    d.setMinimumHeight(400)
    d.setMaximumWidth(700)
    d.setMaximumHeight(400)
    d.setStyleSheet("background-color: #8294C4;")
    titre=QLabel("Recherch par nationalite")
    titre.setStyleSheet('font: 12pt "Copperplate Gothic Bold";')
    titre.setMinimumWidth(250)
    titre.setMinimumHeight(30)
    continu=QLabel()
    continu.setMinimumWidth(680)
    continu.setMinimumHeight(300)
    continu.setStyleSheet("background-color: #DBDFEA;")
    btn = QPushButton("Recherche")
    btn.setStyleSheet('background-color: #DBDFEA;')
    btn.setMaximumWidth(161)
    btn.setMaximumHeight(30)
    n = QLineEdit()
    n.setPlaceholderText("Nationalité")
    n.setStyleSheet('background-color: #DBDFEA;')
    n.setMinimumWidth(100)
    n.setMinimumHeight(30)
    def on_n_clicked():
        text = ("{:<18} {:<18} {:<18} {:<10} {:<15} {:<20} {:<15} {:<5} \n".format("CIN", "Nom", "Prenom", "Age","Nationalite","Telephone", "D_infection" , "Decede"))
        ligne=0
        p_n_trouvee=[]
        id=n.text()
        with open("data.csv", "r") as f:
            reader = csv.reader(f)
            rows = list(reader)
        t = False
        for row in rows:
            if row[4]==id:
                p_n_trouvee.append(row)
                t = True
        if t:
            for personne in p_n_trouvee:
                text +=( "{:<18} {:<18} {:<18} {:<10} {:<15} {:<20} {:<15} {:<5} \n".format(personne[0],personne[1] , personne[2], personne[3] ,personne[4], personne[5],personne[6] ,personne[8]))
                continu.setText(text)
        else:
            continu.setText("Nationalité ne pas trouvee")  
    leyout=QGridLayout()
    leyout.addWidget(titre,0,0)
    leyout.addWidget(n,1,0)
    leyout.addWidget(btn,1,2)
    leyout.addWidget(continu,2,0)
    btn.clicked.connect(on_n_clicked)
    d.setLayout(leyout)
    d.exec_()
def p_en_qu_dialog():
    d=QDialog()
    d.setWindowTitle("Personnes en Quarataine")
    d.setMinimumWidth(700)
    d.setMinimumHeight(400)
    d.setMaximumWidth(700)
    d.setMaximumHeight(400)
    d.setStyleSheet("background-color: #8294C4;")
    titre1=QLabel("Personnes en Quarataine")
    titre1.setStyleSheet('font: 12pt "Copperplate Gothic Bold";')
    titre1.setMinimumWidth(250)
    titre1.setMinimumHeight(30)
    continu1=QLabel()
    continu1.setMinimumWidth(680)
    continu1.setMinimumHeight(300)
    continu1.setStyleSheet('background-color: #DBDFEA;font: 75 8pt "MS Sans Serif";')
    d_l= QLineEdit()
    d_l.setPlaceholderText("Date de jour jj/mm/aaaa")
    d_l.setStyleSheet('background-color: #DBDFEA;')
    d_l.setMinimumWidth(100)
    d_l.setMinimumHeight(30)
    btn_1 = QPushButton("Recherche")
    btn_1.setStyleSheet('background-color: #DBDFEA;')
    btn_1.setMaximumWidth(161)
    btn_1.setMaximumHeight(30)
    def p_q():
        try:
            jour, mois, annee = (d_l.text()).split('/')
            jour = int(jour)
            mois = int(mois)
            annee = int(annee)
            if not (1 <= jour <= 31 and 1 <= mois <= 12 and 1900 <= annee <= 2100):
                QMessageBox.warning(d, "Attention", "le champ donnée doit être de la forme jj/mm/aaaa .")
                return        
        except:
            QMessageBox.warning(d, "Attention", "le champ donnée doit être de la forme jj/mm/aaaa .")
            return
        date = datetime.strptime(d_l.text(), "%d/%m/%Y") 
        personnes_quarantaine = []
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                cin, nom, prenom, age, tel, d_infection= row[0],row[1],row[2],row[3],row[5],row[6]
                d_infection = datetime.strptime(d_infection, '%d/%m/%Y')
                days_limit = (date - d_infection).days
                if days_limit >= 0 and days_limit < 14:
                    personnes_quarantaine.append([cin, nom, prenom, age, tel, d_infection.strftime('%d/%m/%Y')])
        if len(personnes_quarantaine) == 0:
            continu1.setText("Tous les personnes passent la période Qurantaine")
        else:
            text = ("CIN \t   Nom\t Prenom\t  \t age \tTéléphone\t  Date infection \n")
            for p in personnes_quarantaine:
                text +=( "{:^10}  {:^15} {:^20} {:>7} {:^20} {:^30} \n".format(p[0],p[1],p[2],p[3],p[4],p[5]))
            continu1.setText(text)
    leyout=QGridLayout()
    leyout.addWidget(titre1,0,0)
    leyout.addWidget(btn_1,1,1)
    leyout.addWidget(continu1,2,0)
    leyout.addWidget(d_l,1,0)
    btn_1.clicked.connect(p_q)
    d.setLayout(leyout)
    d.exec_()
def p_decedes_dialog():
    d=QDialog()
    d.setWindowTitle("Personnes décédés")
    d.setMinimumWidth(700)
    d.setMinimumHeight(500)
    d.setMaximumWidth(700)
    d.setMaximumHeight(500)
    d.setStyleSheet("background-color: #BE5A83;")
    titre=QLabel("Personnes Décédés")
    titre.setStyleSheet('font: 12pt "Copperplate Gothic Bold";')
    titre.setMinimumWidth(250)
    titre.setMinimumHeight(30)
    t2=QLabel("Pourcentage de Décédés")
    t2.setStyleSheet('font: 75 italic 9pt "Comic Sans MS";')
    t2.setMinimumWidth(150)
    t2.setMinimumHeight(30)
    t3=QLabel("Listes de Personnes Décédés")
    t3.setStyleSheet('font: 75 italic 9pt "Comic Sans MS";')
    t3.setMinimumWidth(200)
    t3.setMinimumHeight(30)
    continu=QLabel()
    continu.setMinimumWidth(680)
    continu.setMinimumHeight(340)
    continu.setStyleSheet('background-color: #F2B6A0')
    btn = QPushButton("Afficher")
    btn.setStyleSheet('background-color: #F2B6A0;')
    btn.setMaximumWidth(161)
    btn.setMaximumHeight(30)
    pourcent = QLabel()
    pourcent.setStyleSheet('background-color: #F2B6A0;font: 12pt "Franklin Gothic Heavy";')
    pourcent.setMinimumWidth(100)
    pourcent.setMinimumHeight(30)
    def decede():
        personnes_decede = []
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                cin, nom, prenom, age,netion, tel, d_infection, d_deces = row[0], row[1], row[2], row[3],row[4], row[5], row[6], row[8]
                if d_deces == "1":
                    personnes_decede.append([cin, nom, prenom, age, tel,netion, d_infection])

        total = len(personnes_decede)
        pourcentage_personnes = round(total / (len(list(csv.reader(open('data.csv'))))) * 100, 2)
        if total == 0:
            continu.setText("Aucune personne n'est décédée.")
        else:
            txt=("CIN \t   Nom\t   Prenom\t  \t age \t  Téléphone\t  Nationalité\t  Date infection \n")
            for p in personnes_decede:
                txt +=( "{:^10}  {:^15} {:^20} {:>7} {:^20} {:^30}  {:^30} \n".format(p[0],p[1],p[2],p[3],p[4],p[5],p[6]))
            continu.setText(txt)
            pourcent.setText(str(pourcentage_personnes)+"%")
    leyout=QGridLayout()
    leyout.addWidget(titre,0,0)
    leyout.addWidget(t2,1,0)
    leyout.addWidget(btn,1,2)
    leyout.addWidget(t3,2,0)
    leyout.addWidget(pourcent,1,1)
    leyout.addWidget(continu,3,0)
    btn.clicked.connect(decede)
    d.setLayout(leyout)
    d.exec_()
def p_enrisque_dialog():
    d=QDialog()
    d.setWindowTitle("Personnes en risque")
    d.setMinimumWidth(420)
    d.setMinimumHeight(400)
    d.setMaximumWidth(420)
    d.setMaximumHeight(400)
    d.setStyleSheet("background-color: #BE5A83;")
    titre=QLabel("Dictionnaire des Personnes en risque")
    titre.setStyleSheet('font: 12pt "Copperplate Gothic Bold";')
    titre.setMinimumWidth(250)
    titre.setMinimumHeight(30)
    liste=QTableWidget()
    liste.setMinimumWidth(380)
    liste.setMinimumHeight(300)
    liste.setColumnCount(3)
    liste.setHorizontalHeaderLabels(["Nom","Prenom","Pourcentage"])
    liste.setColumnWidth(0,145)
    liste.setColumnWidth(1,145)
    liste.setColumnWidth(2,100)
    liste.setStyleSheet('font: 75 9pt "Rockwell";background-color: #F2B6A0')
    btn = QPushButton("Afficher")
    btn.setStyleSheet('background-color: #F2B6A0;')
    btn.setMinimumWidth(90)
    btn.setMinimumHeight(30)
    def risque():
        personnes = []
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                cin, nom, prenom, age = row[0], row[1], row[2], int(row[3])
                risque = 0
                if age > 70:
                    risque += 20
                elif 50 <= age <= 70:
                    risque += 10
                with open('data_m.csv', 'r') as f_m:
                    reader_m = csv.reader(f_m)
                    for row_m in reader_m:
                        if row_m[0] == cin:
                            if row_m[1]== "diabete":
                                risque += 15
                                print(row_m[1])
                            elif row_m[1] == "hypertension":
                                risque += 20
                                print(row_m[1])
                            elif row_m[1] == "asthme":
                                risque += 20
                                print(row_m[1])
                if risque>0.0:
                    personnes.append([nom, prenom,risque])
        liste.setRowCount(len(personnes))
        for i, p in enumerate(personnes):
            liste.setItem(i, 0, QTableWidgetItem(p[0]))
            liste.setItem(i, 1, QTableWidgetItem(p[1]))
            liste.setItem(i, 2, QTableWidgetItem(str(p[2]) + "%"))
    btn.clicked.connect(risque)
    leyout=QGridLayout()
    d.setLayout(leyout)
    leyout.addWidget(titre,0,0)
    leyout.addWidget(liste,2,0)
    leyout.addWidget(btn,1,0)
    d.exec_()
#cd
def enreg_dialog():
    s=QDialog()
    s.setWindowTitle("Enreg. et Recup. Fichiers")
    s.setMinimumWidth(400)
    s.setMinimumHeight(200)
    s.setMaximumWidth(400)
    s.setMaximumHeight(200)
    s.setStyleSheet("background-color: #AAC8A7;")
    titre=QLabel("Menu Enregistrement;")
    titre.setStyleSheet('font: 12pt "Copperplate Gothic Bold";')
    titre.setMinimumWidth(221)
    titre.setMinimumHeight(30)
    t=QLabel("Enregistrement des Personnes")
    t.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t.setMinimumWidth(221)
    t.setMinimumHeight(30)
    btn = QPushButton("Enreg.")
    btn.setStyleSheet('background-color: #E3F2C1;')
    t2=QLabel("Enregistrement des Maladies")
    t2.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t2.setMinimumWidth(221)
    t2.setMinimumHeight(30)
    btn2= QPushButton("Enreg.")
    btn2.setStyleSheet('background-color: #E3F2C1;')
    def enreg_p():
        with open("data.csv", 'r') as f:
            reader = csv.reader(f)
            with open('Personnes.txt', 'w', newline='') as f_out:
                f_out.write("Fichier Infected:\n")
                f_out.write("{:<10} {:<10} {:<10} {:<5} {:<12} {:<12} {:<15} {:<15} {:<5} \n".format("CIN","Nom","Prenom","age","Nationalité","Téléphone","Date infection","adresse","Décédé"))
                for row in reader:
                    f_out.write("{:<10} {:<10} {:<10} {:<5} {:<12} {:<12} {:<15} {:<15} {:<5} \n".format(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
                QMessageBox.information(s,"Info","Les données sonr enregistrer sur personnes.txt")
    def enreg_m():
        code=1
        with open("data_m.csv", 'r') as f:
            reader = csv.reader(f)
            with open('Maladies.txt', 'w', newline='') as f_out:
                f_out.write("Fichier Maladies:\n")
                f_out.write("{:<10} {:<10} {:<10} {:<7}\n".format("Code","CIN","Nom maladie","nombre d'années"))
                for row in reader:
                    f_out.write("{:<10} {:<10} {:<10} {:>7}  \n".format(code,row[0],row[1],row[2]))
                    code+=1
                QMessageBox.information(s,"Info","Les données sonr enregistrer sur Maladies.txt")
    leyout=QGridLayout()
    leyout.addWidget(titre,0,0)
    leyout.addWidget(t,1,0)
    leyout.addWidget(btn,1,1)
    leyout.addWidget(t2,2,0)
    leyout.addWidget(btn2,2,1)
    btn.clicked.connect(enreg_p)
    btn2.clicked.connect(enreg_m)
    s.setLayout(leyout)
    s.exec_()  
def recup_dialog():
    s=QDialog()
    s.setWindowTitle("Enreg. et Recup. Fichiers")
    s.setMinimumWidth(400)
    s.setMinimumHeight(200)
    s.setMaximumWidth(400)
    s.setMaximumHeight(200)
    s.setStyleSheet("background-color: #AAC8A7;")
    titre=QLabel("Menu Recuperation;")
    titre.setStyleSheet('font: 12pt "Copperplate Gothic Bold";')
    titre.setMinimumWidth(221)
    titre.setMinimumHeight(30)
    t=QLabel("Recuperation des Personnes")
    t.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t.setMinimumWidth(221)
    t.setMinimumHeight(30)
    btn = QPushButton("Recup.")
    btn.setStyleSheet('background-color: #E3F2C1;')
    b = QPushButton("Ouvrir.")
    b.setStyleSheet('background-color: #E3F2C1;')
    d_p= QLineEdit()
    d_p.setPlaceholderText("File Path 'C:/......./File.txt'")
    d_p.setStyleSheet('background-color: #E3F2C1;')
    d_p.setMinimumWidth(100)
    d_p.setMinimumHeight(30)
    t2=QLabel("Recuperation des Maladies")
    t2.setStyleSheet('font: 8pt "Copperplate Gothic Bold";')
    t2.setMinimumWidth(221)
    t2.setMinimumHeight(30)
    btn2= QPushButton("Recup.")
    btn2.setStyleSheet('background-color: #E3F2C1;')
    b2= QPushButton("Ouvrir.")
    b2.setStyleSheet('background-color: #E3F2C1;')
    d_m= QLineEdit()
    d_m.setPlaceholderText("File Path 'C:/......./File.txt'")
    d_m.setStyleSheet('background-color: #E3F2C1;')
    d_m.setMinimumWidth(100)
    d_m.setMinimumHeight(30)
    def ouvrir_dielog():
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Fichier texte (*.txt)")
        file_dialog.selectNameFilter("Fichier texte (*.txt)")
        if file_dialog.exec_() == QFileDialog.Accepted:
            selected_file = file_dialog.selectedFiles()[0]
            d_p.setText(selected_file)
    def ouvrir_m_dielog():
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Fichier texte (*.txt)")
        file_dialog.selectNameFilter("Fichier texte (*.txt)")
        if file_dialog.exec_() == QFileDialog.Accepted:
            selected_file = file_dialog.selectedFiles()[0]
            d_m.setText(selected_file)
    leyout=QGridLayout()
    leyout.addWidget(titre,0,0)
    leyout.addWidget(t,1,0)
    leyout.addWidget(b,2,1)
    leyout.addWidget(b2,4,1)
    leyout.addWidget(btn,2,2)
    leyout.addWidget(d_p,2,0)
    leyout.addWidget(d_m,4,0)
    leyout.addWidget(t2,3,0)
    leyout.addWidget(btn2,4,2)
    def recu_p ():
        peth=d_p.text()
        with open(peth, 'r') as f:
            f.readline() 
            f.readline() 
            with open('data_new.csv', 'a', newline='') as f_out:
                writer = csv.writer(f_out)
                for ligne in f:
                    cin, nom, prenom, age, nationalite, tel, d_infection, adresse, decede = ligne.strip().split()
                    writer.writerow([cin, nom, prenom, age, nationalite, tel, d_infection, adresse, decede])
            QMessageBox.information(s, "Info", "Les données de fichiers données ont été ajoutées dans data_new.csv .")
    def recu_m ():
        peth=d_m.text()
        with open(peth, 'r') as f:
            f.readline() 
            f.readline() 
            with open('data_new_m.csv', 'a', newline='') as f_out:
                writer = csv.writer(f_out)
                for ligne in f:
                    code,cin, nom,nbr = ligne.strip().split()
                    writer.writerow([code,cin, nom,nbr])
            QMessageBox.information(s, "Info", "Les données de fichiers données ont été ajoutées dans data_new_m.csv .")
    btn.clicked.connect(recu_p)
    btn2.clicked.connect(recu_m)
    b.clicked.connect(ouvrir_dielog)
    b2.clicked.connect(ouvrir_m_dielog)
    s.setLayout(leyout)
    s.exec_()
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ma MainWindow')
        self.setGeometry(200, 200, 620, 350)
        self.setMinimumWidth(620)
        self.setMinimumHeight(350)
        self.setStyleSheet('background-color: rgb(198, 195, 161);')
        self.creat_menu()
        self.text_box()
    def text_box(self):
        text = QTextBrowser(self)
        text.setPlainText("Réalisé par :\n                Ouassleti Meyssa\n                Bahri Chaher\n                Miled Maram")
        text.setAlignment(Qt.AlignCenter)
        text.setFont(QFont("Comic Sans MS", 12))
        text.setStyleSheet("background-color: rgb(198, 195, 161); color: #000000;")
        text.setFixedSize(220, 130)
        text.setGeometry(QtCore.QRect(210, 110, 300, 150))
        self.setCentralWidget(text)     
    def creat_menu(self):
        m_b=self.menuBar()
        m_b.addMenu("Accueil")
         #---__---
        pers_menu = m_b.addMenu("Gestion des personnes")
        mise_a_jour= pers_menu.addMenu("Mise à jour des personnes")
        add_pers_action = QAction("Ajouter une personne", self)
        mise_a_jour.addAction(add_pers_action)
        add_pers_action.triggered.connect(ajouter_personne_dialog)
        edit_pers_action = QAction("Modifier une personne", self)
        mise_a_jour.addAction(edit_pers_action)
        edit_pers_action.triggered.connect(modif_personne_dialog)
        del_pers_action = QAction("Supprimer une personne", self)
        mise_a_jour.addAction(del_pers_action)
        del_pers_action.triggered.connect(supp_personne_dialog)
        #sep
        rech_aff = pers_menu.addMenu("Recherche et affichage")
        dictionnaire_action = QAction("Dictionnaire", self)
        rech_aff.addAction(dictionnaire_action)
        dictionnaire_action.triggered.connect(dict_p_dialog)
        rech_action = QAction("Recherche", self)
        rech_aff.addAction(rech_action)
        rech_action.triggered.connect(rech_p_dialog)
        #-_-_-_
        mal_menu = m_b.addMenu("Gestion des maladies")
        mise_a_jour= mal_menu.addMenu("Mise à jour des Maladies")
        add_mal_action = QAction("Ajouter une maladie", self)
        mise_a_jour.addAction(add_mal_action)
        add_mal_action.triggered.connect(ajouter_m_dialog)
        edit_mal_action = QAction("Modifier une maladie", self)
        mise_a_jour.addAction(edit_mal_action)
        edit_mal_action.triggered.connect(modif_m_dialog)
        del_mal_action = QAction("Supprimer une maladie", self)
        mise_a_jour.addAction(del_mal_action)
        del_mal_action.triggered.connect(supp_m_dialog)
        rech_aff_m=mal_menu.addMenu("Recherche et affichage")
        dict_m_action=QAction("Dictionnaire", self)
        rech_aff_m.addAction(dict_m_action)
        dict_m_action.triggered.connect(dict_m_dialog)
        rech_action = QAction("Recherche", self)
        rech_aff_m.addAction(rech_action)
        rech_action.triggered.connect(rech_m_dialog)
        #sep
        calc_aff=m_b.addMenu("Calcul et affichage")
        nati_action=QAction("afficher par nationalité",self)
        calc_aff.addAction(nati_action)
        nati_action.triggered.connect(p_nati_dialog)
        quarantine_action=QAction("Personnes en Quarantaine",self)
        calc_aff.addAction(quarantine_action)
        quarantine_action.triggered.connect(p_en_qu_dialog)
        decede_action=QAction("Personnes décédés",self)
        calc_aff.addAction(decede_action)
        decede_action.triggered.connect(p_decedes_dialog)
        risque_action=QAction("Personnes en Risque",self)
        calc_aff.addAction(risque_action)
        risque_action.triggered.connect(p_enrisque_dialog)
        # -_-_-_-_
        enreg_menu = m_b.addMenu("Enreg et recup des fichiers")
        enreg_action = QAction("Enregistrer les données", self)
        enreg_menu.addAction(enreg_action)
        enreg_action.triggered.connect(enreg_dialog)
        recup_action = QAction("Récupérer les données", self)
        enreg_menu.addAction(recup_action)
        recup_action.triggered.connect(recup_dialog)      
def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()  