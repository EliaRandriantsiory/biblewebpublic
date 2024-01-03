import os,json,sqlite3

current_link=os.getcwd()
link_bible=f"{current_link}//DB//baiboly"
#link_trad=f"{current_link}//trad.txt"

connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
curseur = connexion.cursor()

def import_trad_chapt_dans_server():
    #connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
    #curseur = connexion.cursor()
    f =open(f"{current_link}\\trad.txt", "r", encoding='utf-8')
    texts= f.readlines()
    for te in texts:
        t = te.replace('\n','')
        tex=t.split('\t')
        curseur.execute('INSERT OR REPLACE INTO baiboly_trad (bbl_m, bbl_fr, chpt) VALUES (?, ?, ?)', (tex[0], tex[1], tex[2]))
        connexion.commit()
    
    print('import trad dans serveur ok..')

def import_list_bbl_dans_server():
    f =open(f"{current_link}\\list_bbl.txt", "r", encoding='utf-8')
    texts= f.readlines()
    for te in texts:
        t = te.replace('\n','')
        tex=t.split('\t')
        curseur.execute('INSERT OR REPLACE INTO baiboly_cls_baibl (bible, type_bible, nbr_chapitre) VALUES (?, ?, ?)', (tex[1], tex[0], tex[2]))
        connexion.commit()
    
    print('import list_bbl dans serveur ok..')

def import_vrs_bbl_dans_server():
    f =open(f"{current_link}\\vrs_bbl.txt", "r", encoding='utf-8')
    texts= f.readlines()
    for te in texts:
        t = te.replace('\n','')
        tex=t.split('\t')
        curseur.execute('INSERT OR REPLACE INTO baiboly_vrs_baibl (bible_vrs, chptr, nbr_vrs) VALUES (?, ?, ?)', (tex[0], tex[1], tex[2]))
        connexion.commit()
    print('import vrs_bbl dans serveur ok..')

def import_DB_baiboly_dans_server():
    #connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
    #curseur = connexion.cursor()
    for x in os.listdir(link_bible):
        with open((f"{link_bible}\\{x}"), "r", encoding='utf-8') as fichier:
            donnees=json.load(fichier)
        content=json.dumps(donnees)
        nm=os.path.splitext(x)
        curseur.execute('INSERT OR REPLACE INTO baiboly_baiboly (bible, content_bible) VALUES (?, ?)', (nm[0], content))
        connexion.commit()
    print('import DB_baiboly dans serveur ok..')

#import_trad_chapt_dans_server()
#import_list_bbl_dans_server()
#import_vrs_bbl_dans_server()
#import_DB_baiboly_dans_server()

    

