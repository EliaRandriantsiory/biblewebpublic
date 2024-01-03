import os,json,sqlite3
import datetime,time

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
        curseur.execute('INSERT OR REPLACE INTO Bbl_baiboly (bible, content_bible) VALUES (?, ?)', (nm[0], content))

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
        pass
        #self.Creat_table_dt()
        #self.import_bible()
        #self.import_fihirana()
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
            curseur.execute('INSERT OR REPLACE INTO baiboly_baiboly (bible, content_bible) VALUES (?, ?)', (nm[0], content))

        connexion.commit()
        connexion.close()

    def import_fihirana(self):
        
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()
        for x in os.listdir(link_fihirana1):
            with open((f"{link_fihirana1}\\{x}"), "r", encoding='utf-8') as fichier1:
                donnees1=json.load(fichier1)
            
            ord=str(donnees1.pop('ord'))
            ord=ord.replace("[",'')
            ord=ord.replace("]",'')
            ord=ord.replace("'",'')
            ord=ord.replace('"','')

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
    
    def __init__(self,nomDbout):
        

        db_in=f"{current_link}//db.sqlite3"
        db_out=f"{current_link}//{nomDbout}.sqlite3"
        
        self.Creat_table_dt(db_out)
        self.Export_bible(db_in,db_out)
        self.Export_fihirana(db_in,db_out)
        self.Export_trad(db_in,db_out)
        self.Export_verset(db_in,db_out)
        self.Export_list_fihirana1(db_in,db_out)
        self.Export_list_fihirana2(db_in,db_out)
        self.Export_fihirana_ajout(db_in,db_out)
        self.Export_list_fihirana_ajout(db_in,db_out)
        self.Export_a_propos(db_in,db_out)
     
    def Creat_table_dt(self,db_out):
        #a=time.asctime()
        #a=a.split(' ')
        #b=a[3].split(':')
        #b="".join(b)
        #print(b)
        #filtr=f"{a[4]} {a[1]} {a[4]}-{a[2]} {a[3]} ({a[0]})"  
        connexion = sqlite3.connect(db_out)
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
        Content TEXT,Ord_diff TEXT
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS fihirana2(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Titre TEXT  ,              
        Content TEXT,Ord_diff TEXT
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS fihirana_ajout(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Titre TEXT  ,              
        Content TEXT,
        Ord_diff TEXT
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
        curseur.execute('''CREATE TABLE IF NOT EXISTS list_fihirana_ajout(
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
        Trad2 TEXT,chpt TEXT
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS vrs(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        Bible TEXT,
        Chapitre INTEGER,
        Nb_Verset INTEGER
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
        curseur.execute('''CREATE TABLE IF NOT EXISTS Signalement(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        type VARCHAR,
        content VARCHAR,
        etat INTEGER,
        date DATETIME DEFAULT CURRENT_TIMESTAMP
        )''')
        curseur.execute('''CREATE TABLE IF NOT EXISTS APropos(
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
        fihirana1_count INTEGER,
        fihirana1_date_dernier_mis_à_jour VARCHAR,
        fihirana2_count INTEGER,
        fihirana2_date_dernier_mis_à_jour VARCHAR,
        fihirana_fanampiny_count INTEGER,
        fihirana_fanampiny_date_dernier_mis_à_jour VARCHAR,
        Date_mis_à_jour VARCHAR
        )''')
        connexion.close()
        
    def Export_bible(self,db_in,db_out):
        connexion_src = sqlite3.connect(db_in)
        curseur_src = connexion_src.cursor()

        connexion_out = sqlite3.connect(db_out)
        curseur_out = connexion_out.cursor()
        curseur_src.execute('SELECT * FROM baiboly_baiboly')
        resultats=curseur_src.fetchall()
        for resultat in resultats:
            curseur_out.execute('INSERT OR REPLACE INTO Baiboly (bible, Content_file) VALUES (?, ?)', (resultat[1], resultat[2]))
        
        connexion_out.commit()

        connexion_out.close()
        connexion_src.close()

    def Export_fihirana(self,db_in,db_out):
        
        connexion_src = sqlite3.connect(db_in)
        curseur_src = connexion_src.cursor()
        curseur_src2 = connexion_src.cursor()

        connexion_out = sqlite3.connect(db_out)
        curseur_out = connexion_out.cursor()
        #fihirana 1
        curseur_src.execute('SELECT * FROM fihirana_fihirana1')
        resultats=curseur_src.fetchall()
        for resultat in resultats:
            #curseur_out.execute('INSERT OR REPLACE INTO Baiboly (bible, Content_file) VALUES (?, ?)', (resultat[1], resultat[2]))
            #curseur.execute('INSERT OR REPLACE INTO fihirana_fihirana1 (Titre, Content, ord_diff) VALUES (?, ?, ?)', (nm[0], content_file, ord))
            #print(type(resultat[3]))
            curseur_out.execute('INSERT OR REPLACE INTO fihirana1 (Titre, Content, ord_diff) VALUES (?, ?, ?)', (resultat[1], resultat[2], resultat[3]))
        
        connexion_out.commit()
        #fihirana2
        curseur_src2.execute('SELECT * FROM fihirana_fihirana2')
        resultats2=curseur_src2.fetchall()
        for resultat2 in resultats2:
            #curseur_out.execute('INSERT OR REPLACE INTO Baiboly (bible, Content_file) VALUES (?, ?)', (resultat[1], resultat[2]))
            #curseur.execute('INSERT OR REPLACE INTO fihirana_fihirana1 (Titre, Content, ord_diff) VALUES (?, ?, ?)', (nm[0], content_file, ord))
            #print(type(resultat[3]))
            curseur_out.execute('INSERT OR REPLACE INTO fihirana2 (Titre, Content, ord_diff) VALUES (?, ?, ?)', (resultat2[1], resultat2[2], resultat2[3]))
        
        connexion_out.commit()


        connexion_out.close()
        connexion_src.close()

            #print(type(ord))
            
    def Export_trad(self,db_in,db_out):
        connexion_src = sqlite3.connect(db_in)
        curseur_src = connexion_src.cursor()

        connexion_out = sqlite3.connect(db_out)
        curseur_out = connexion_out.cursor()
        curseur_src.execute('SELECT * FROM baiboly_trad')
        resultats=curseur_src.fetchall()
        for resultat in resultats:
            #print(len(resultat))    
            curseur_out.execute('INSERT OR REPLACE INTO trad (Trad1, Trad2,chpt) VALUES (?, ?, ?)', (resultat[1], resultat[2],resultat[3]))
        
        connexion_out.commit()

        connexion_out.close()
        connexion_src.close()
    
    def Export_verset(self,db_in,db_out):
        connexion_src = sqlite3.connect(db_in)
        curseur_src = connexion_src.cursor()

        connexion_out = sqlite3.connect(db_out)
        curseur_out = connexion_out.cursor()
        curseur_src.execute('SELECT * FROM baiboly_vrs_baibl')
        resultats=curseur_src.fetchall()
        for resultat in resultats:
            curseur_out.execute('INSERT OR REPLACE INTO vrs (Bible, Chapitre, Nb_Verset) VALUES (?, ?, ?)', (resultat[1], resultat[2], resultat[3]))
        
        connexion_out.commit()

        connexion_out.close()
        connexion_src.close()

    def Chapitre(self,db_in,db_out):
        
        connexion_src = sqlite3.connect(db_in)
        curseur_src = connexion_src.cursor()

        connexion_out = sqlite3.connect(db_out)
        curseur_out = connexion_out.cursor()
        curseur_src.execute('SELECT * FROM baiboly_vrs_baibl')
        resultats=curseur_src.fetchall()
        for resultat in resultats:
            curseur_out.execute('INSERT OR REPLACE INTO chp(Bible, Nb_Chapitre_Bible) VALUES (?, ?)', (resultat[1], resultat[2]))
        
        connexion_out.commit()

        connexion_out.close()
        connexion_src.close()

    def Export_list_fihirana1(self,db_in,db_out):
        connexion_src = sqlite3.connect(db_in)
        curseur_src = connexion_src.cursor()

        connexion_out = sqlite3.connect(db_out)
        curseur_out = connexion_out.cursor()
        curseur_src.execute('SELECT * FROM fihirana_list_fihirana1')
        resultats=curseur_src.fetchall()
        for resultat in resultats:
            #print(len(resultat))
            curseur_out.execute('INSERT OR REPLACE INTO list_fihirana1 (Rang_file, Clés, Transpose, Titre) VALUES (?, ?, ?, ?)', (resultat[1], resultat[2], resultat[3],resultat[4]))
        
        connexion_out.commit()
        connexion_out.close()
        connexion_src.close()
            
    def Export_list_fihirana2(self,db_in,db_out):
        connexion_src = sqlite3.connect(db_in)
        curseur_src = connexion_src.cursor()

        connexion_out = sqlite3.connect(db_out)
        curseur_out = connexion_out.cursor()
        curseur_src.execute('SELECT * FROM fihirana_list_fihirana2')
        resultats=curseur_src.fetchall()
        for resultat in resultats:
            #print(len(resultat))
            curseur_out.execute('INSERT OR REPLACE INTO list_fihirana2 (Rang_file, Clés, Transpose, Titre) VALUES (?, ?, ?, ?)', (resultat[1], resultat[2], resultat[3],resultat[4]))
        
        connexion_out.commit()
        connexion_out.close()
        connexion_src.close()
            
    def Export_fihirana_ajout(self,db_in,db_out):
        connexion_src = sqlite3.connect(db_in)
        curseur_src = connexion_src.cursor()

        connexion_out = sqlite3.connect(db_out)
        curseur_out = connexion_out.cursor()
        curseur_src.execute('SELECT * FROM fihirana_fhrn_ajout')
        resultats=curseur_src.fetchall()

        for resultat in resultats:
            curseur_out.execute('INSERT OR REPLACE INTO fihirana_ajout (Titre, Content, Ord_diff) VALUES (?, ?, ?)', (resultat[1], resultat[2], resultat[3]))
        
        connexion_out.commit()

        connexion_out.close()
        connexion_src.close()

    def Export_list_fihirana_ajout(self,db_in,db_out):
        connexion_src = sqlite3.connect(db_in)
        curseur_src = connexion_src.cursor()

        connexion_out = sqlite3.connect(db_out)
        curseur_out = connexion_out.cursor()
        curseur_src.execute('SELECT Titre FROM fihirana_fhrn_ajout')
        resultats=curseur_src.fetchall()

        for resultat in resultats:
            
            curseur_out.execute('INSERT OR REPLACE INTO list_fihirana_ajout (Titre,Rang_file,Clés,Transpose) VALUES (?,?,?,?)', (resultat[0],"","",""))
        
        connexion_out.commit()

        connexion_out.close()
        connexion_src.close()

    def Export_a_propos(self,db_in,db_out):
        connexion_src = sqlite3.connect(db_in)
        curseur_src = connexion_src.cursor()

        curseur_src.execute('SELECT * FROM fihirana_list_fihirana1')
        resultats_fihirana1=curseur_src.fetchall()
        curseur_src.execute('SELECT * FROM fihirana_fhrn_ajout')
        resultats_fhrn_ajout=curseur_src.fetchall()
        curseur_src.execute('SELECT * FROM fihirana_list_fihirana2')
        resultats_fihirana2=curseur_src.fetchall()
        #print(len(resultats_fihirana1),len(resultats_fhrn_ajout),len(resultats_fihirana2))



        connexion_out = sqlite3.connect(db_out)
        curseur_out = connexion_out.cursor()
        date_mis_a_jour=time.asctime()
        curseur_out.execute('INSERT OR REPLACE INTO APropos (fihirana1_count,fihirana1_date_dernier_mis_à_jour,fihirana2_count,fihirana2_date_dernier_mis_à_jour,fihirana_fanampiny_count,fihirana_fanampiny_date_dernier_mis_à_jour,Date_mis_à_jour) VALUES (?,?,?,?,?,?,?)', (len(resultats_fihirana1),"",len(resultats_fihirana2),"",len(resultats_fhrn_ajout),"",date_mis_a_jour))
        
        connexion_out.commit()

        connexion_out.close()
        connexion_src.close()
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

#fl=export_files_in_database.export_fihirana()
#fl_=fl[0]
#content=fl_[2]
#content=str(content).replace("\r", "")
#content=content.split("\n")
#exp_to_json1(content)
#print((content))

def export_fihirana_ajout_to_db(rng):
    content_fl=["\n"]
    dt=dict()
    ord=['1','2','3','4','5','6','7','8','9','1. (In-2)','2. (In-2)','3. (In-2)','4. (In-2)','5. (In-2)','6. (In-2)','7. (In-2)','8. (In-2)','9. (In-2)','1.','2.','3.','4.','5.','6.','7.','8.','9',"Isan'andininy","Isan'andininy2","Isan’andininy: (Bis)","","Isan’andininy: ","Isan’andininy : (in 2)","Isan’andininy :","Isan ’andininy:"]
    connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
    curseur = connexion.cursor()
    curseur.execute('SELECT * FROM fihirana_fhrn_ajout')
    donnees = curseur.fetchall()
    curseur.close()
    dtt=donnees[rng]
    dt_=dtt[2]
    dt_=str(dt_).replace("\r","")
    dt_=str(dt_).split("\n")

    for te in dt_:
        t = te.replace('\n','')
        tex=t.split('\t')
        #print(tex[0])
        
        if tex[0] in ord:
            t = content_fl[0].replace('\n','')
            #print(t)
            dt[t]=content_fl
            content_fl=[]
        #print(te)
        content_fl.append(te)

    return dt
    
#export_files_in_database()
#fl=export_fihirana_ajout_to_db(1)
#print(fl.keys())

#export_files_in_database()
#a=time.asctime()
#a=a.split(' ')
#b=a[3].split(':')
#b="".join(b)
#
#backup_file = f'db_out_test2'
#export_files_in_database(backup_file)

#a=time.asctime()
#print(a)
#a=a.split(' ')
#b=a[3].split(':')
#b="".join(b)
#filtr=f"{a[4]} {a[1]} {a[4]}-{a[2]} {a[3]} ({a[0]})"  
#print(a)


