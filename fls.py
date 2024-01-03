import os,json,sqlite3
import datetime,time
from add_fonction1_5 import *

current_link=os.getcwd()
link_bible=f"{current_link}//files//DB//baiboly"
link_fihirana1=f"{current_link}//files//DB//fihirana//fihirana1"
link_fihirana2=f"{current_link}//files//DB//fihirana//fihirana2"

#print(len(os.listdir(link_bible)))
connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
curseur = connexion.cursor()
def import_dans_server():
    #connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
    #curseur = connexion.cursor()
    for x in os.listdir(link_bible):
        with open((f"{link_bible}\\{x}"), "r", encoding='utf-8') as fichier:
            donnees=json.load(fichier)
        content=json.dumps(donnees)
        nm=os.path.splitext(x)
        
        #print(baiboly_G.trad(nm[0],0))
        
        curseur.execute('INSERT OR REPLACE INTO baiboly_baiboly (bible, content_bible) VALUES (?, ?)', (baiboly_G.trad(nm[0],0), content))

    connexion.commit()
    connexion.close()

def export_du_serveur():
    #connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
    #curseur = connexion.cursor()
    
    curseur.execute('SELECT bible FROM Bbl_baiboly')
    donnees = curseur.fetchall()
    #for x in donnees:
    #    print(x[0])

    
    #print(donnees)

    #connexion.commit()
    connexion.close()
    return donnees
    

def exp_to_json1(b):
    content_fl=[""]
    all_keys=[]
    key=[]
    dt=dict()

    ord=['b', '1','2','3','4','5','6','7','8','9','1.1','2.1','3.1','4.1','5.1','6.1','7.1','8.1','9.1','1. (In-2)','2. (In-2)','3. (In-2)','4. (In-2)','5. (In-2)','6. (In-2)','7. (In-2)','8. (In-2)','9. (In-2)','1.','2.','3.','4.','5.','6.','7.','8.','9',"Isan'andininy","Isan'andininy2","Isan’andininy: (Bis)","","Isan’andininy: ","Isan’andininy : (in 2)","Isan’andininy :","Isan ’andininy:"]
    
    ctn=str(b).split("\n")

    for te in b:
        
        t=te.replace('\r','')
        if te in ord:
        #    print('oui')
            
            te = content_fl[0].replace('\n','')
            dt[key[-1]]=content_fl
            key.append(te)
            content_fl=[]
        content_fl.append(te)
    t_ = content_fl[0].replace('\n','')
    dt[t_]=content_fl    
    print((dt))

class import_files_to_database:
    def __init__(self):
        
        #self.Creat_table_dt()
        #self.import_bible()
        self.import_fihirana()
        #self.import_trad()
        #self.verset()
        #self.Chapitre()
        #self.list_fihirana1()
        #self.list_fihirana2()
        #self.import_bible()

    def Creat_table_dt(self):
        a=time.asctime()
        a=a.split(' ')
        #filtr=f"{a[4]} {a[1]} {a[4]}-{a[2]} {a[3]} ({a[0]})"  
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()

        curseur.execute('''CREATE TABLE IF NOT EXISTS Baiboly(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Bible TEXT,
        Content_file TEXT
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS chp(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Bible TEXT,
        Nb_Chapitre_Bible INTEGER
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS fihirana1(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Titre TEXT    ,            
        Content TEXT
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS fihirana2(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Titre TEXT  ,              
        Content TEXT
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS list_fihirana1(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Rang_file INTEGER,
        Clés VARCHAR,
        Transpose INTEGER,
        Titre TEXT 
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS list_fihirana2(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Rang_file INTEGER,
        Clés VARCHAR,
        Transpose INTEGER,
        Titre TEXT
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS nt(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Content TEXT
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS trad(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Trad1 TEXT,
        Trad2 TEXT
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS vrs(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Bible TEXT,
        Chapitre INTEGER,
        Nb_Chapitre INTEGER
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS Historique(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                    jour VARCHAR,
                    date VARCHAR,
                    heure VARCHAR,
                    type VARCHAR,
                    content VARCHAR
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS innit_param(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        scrn1 TEXT,
        scrn2 TEXT,
        scrn2_baiboly TEXT,
        scrn2_label_size TEXT
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS param(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        scrn1 TEXT,
        scrn2 TEXT,
        scrn2_baiboly TEXT,
        scrn2_label_size TEXT
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS scrn1_out(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        type VARCHAR,
        titre VARCHAR,
        content VARCHAR,
        ord_diff INTEGER
        )''')
        connexion.close()

    def import_bible(self):
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()
        for x in os.listdir(link_bible):
            with open((f"{link_bible}\\{x}"), "r", encoding='utf-8') as fichier:
                donnees=json.load(fichier)
            content=json.dumps(donnees)
            nm=os.path.splitext(x)
            curseur.execute('INSERT OR REPLACE INTO Baiboly (Bible, Content_file) VALUES (?, ?)', (nm[0], content))

        connexion.commit()
        connexion.close()

    def import_fihirana(self):
        print('oui')
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()
        for x in os.listdir(link_fihirana1):
            with open((f"{link_fihirana1}\\{x}"), "r", encoding='utf-8') as fichier1:
                donnees1=json.load(fichier1)
            
            ord=str(donnees1.pop('ord'))
            # ord=ord.replace("[",'')
            # ord=ord.replace("]",'')
            # ord=ord.replace("'",'')
            # ord=ord.replace('"','')

            #print(type(ord))
            
            content_file=json.dumps(donnees1)
            
            nm=os.path.splitext(x)
            curseur.execute('INSERT OR REPLACE INTO fihirana_fihirana1 (Titre, Content, ord_diff) VALUES (?, ?, ?)', (nm[0], content_file, ord))
        
        for x in os.listdir(link_fihirana2):
            with open((f"{link_fihirana2}\\{x}"), "r", encoding='utf-8') as fichier2:
                donnees2=json.load(fichier2)
            
            ord=str(donnees2.pop('ord'))
            #print(donnees2)
            content2=json.dumps(donnees2)
            nm=os.path.splitext(x)
            curseur.execute('INSERT OR REPLACE INTO fihirana_fihirana2(Titre, Content, ord_diff) VALUES (?, ?, ?)', (nm[0], content2, ord))

        connexion.commit()
        connexion.close()

    def import_trad(self):
        f =open(f"{current_link}\\files\\dependances\\trad.txt", "r", encoding='utf-8')
        texts= f.readlines()
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()
        for te in texts:
            t = te.replace('\n','')
            tex=t.split('\t')
            curseur.execute('INSERT OR REPLACE INTO trad(Trad1, Trad2) VALUES (?, ?)', (tex[0], tex[1]))
            connexion.commit()
        connexion.close()
    
    def verset(self):
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()
        f =open(f"{current_link}\\files//dependances//vrs.txt", "r", encoding='utf-8')
        texts= f.readlines()
        for te in texts:
            t = te.replace('\n','')
            tex=t.split('\t')
            curseur.execute('INSERT OR REPLACE INTO vrs(Bible, Chapitre, Nb_Chapitre) VALUES (?, ?, ?)', (tex[0], tex[1], tex[2]))
            connexion.commit()
        connexion.close()

    def Chapitre(self):
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()
        f =open(f"{current_link}\\files//dependances//chp.txt", "r", encoding='utf-8')
        texts= f.readlines()
        for te in texts:
            t = te.replace('\n','')
            tex=t.split('\t')
            curseur.execute('INSERT OR REPLACE INTO chp(Bible, Nb_Chapitre_Bible) VALUES (?, ?)', (tex[0], tex[1]))
            connexion.commit()
        connexion.close()

    def list_fihirana1(self):
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()
        f =open(f"{current_link}\\files\\dependances\\fihirana1.txt", "r", encoding='utf-8')
        texts= f.readlines()
        for te in texts:
            t = te.replace('\n','')
            tex=t.split('\t')
            curseur.execute('INSERT OR REPLACE INTO fihirana_list_fihirana1(Range_file, Clés, Transpose, Titre) VALUES (?, ?, ?, ?)', (tex[0], tex[1], tex[2], tex[3]))
            connexion.commit()
        connexion.close()

    def list_fihirana2(self):
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()
        f =open(f"{current_link}\\files\\dependances\\fihirana2.txt", "r", encoding='utf-8')
        texts= f.readlines()
        for te in texts:
            t = te.replace('\n','')
            tex=t.split('\t')
            curseur.execute('INSERT OR REPLACE INTO fihirana_list_fihirana2(Range_file, Clés, Transpose, Titre) VALUES (?, ?, ?, ?)', (tex[0], tex[1], tex[2], tex[3]))
            connexion.commit()
        connexion.close()

class export_files_in_database:
    def __init__(self):
        pass
        #self.export_fihirana()
    def export_fihirana():
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()
        curseur.execute('SELECT * FROM fihirana_fhrn_mod')
        donnees = curseur.fetchall()
        fl=donnees[-1]
        fl_=str(fl[2]).replace('                    ','')
        fl_=fl_.replace('\r\n','')
        fl_=fl_.replace('                ','\n')
        return donnees
        #print(fl_)

class importlesona:
    def importTitre():
        rng = list(map(str,(range(0,65))))
        title = []
        subtitle = []
        content= dict()
        f =open(f"{current_link}\\files\\lesona\\lohatenyDetail.txt", "r", encoding='utf-8')
        texts= f.readlines()
        
        # connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        # curseur = connexion.cursor()
        #print(rng)
        for te in texts:
            te=te.replace("\n","")
            tex=te.split('-')
            subtitle.append(te)

            if tex[0] in rng:

                title.append(te)
                subtitle.pop(-1)
                content[title[len(title)-2]]=subtitle
                print(title[len(title)-2])
                curseur.execute('INSERT OR REPLACE INTO lesona_lesona(Titre) VALUES (?)', (title[len(title)-2],))
                connexion.commit()
                
                subtitle=[]
            
               
     
        
        #content[title[-1]]=subtitle
        curseur.execute('INSERT OR REPLACE INTO lesona_lesona(Titre) VALUES (?)', (title[len(title)-2],))
        # if len(subtitle)!=0:
        #     curseur.execute('INSERT OR REPLACE INTO lesona_soustitre(sousTitre) VALUES (?)', (subtitle))
        connexion.commit()
        connexion.close()
        #print(content)
        
importlesona.importTitre()  

        
#import_files_to_database()
#with open((f"{link_fihirana1}\\008.json"), "r", encoding='utf-8') as fichier1:
#    donnees1=json.load(fichier1)
#
#ord=str(donnees1.pop('ord'))
#ord=ord.replace("[",'')
#ord=ord.replace("]",'')
#ord=ord.replace("'",'')
#ord=ord.replace('"','')
#ord=ord.split(", ")
#print(ord)

# fl=export_files_in_database.export_fihirana()
# fl_=fl[0]
# content=fl_[2]
# content=str(content).replace("\r", "")
# content=content.split("\n")
# exp_to_json1(content)
#print((content))


