import json,os,textwrap ,sqlite3
import datetime,time

current_link=os.getcwd()
image_path=f"{current_link}//files//images//milky-way-8153503_1280.jpg"
chm_baiboly=f"{current_link}//files//DB//baiboly"
chm_fihirana1=f"{current_link}//files//DB//fihirana//fihirana1"
chm_fihirana2=f"{current_link}//files//DB//fihirana//fihirana2"
historique_dict=dict()
class fihirana_G():
    def fihirana1(fhr,ttr):
        if len(fhr)==1:    
            fhr=f"00{fhr}"    
        elif len(fhr)==2:
            fhr=f"0{fhr}"
        else:
            fhr=fhr
#, encoding='utf-8'
        with open((f"{chm_fihirana1}\\{fhr}.json"), "r", encoding='utf-8') as fichier:
            donnees = json.load(fichier)
        #fh=fihirana("001 TSY MISY TANTARA")
        fh=donnees
        ttr=ttr
        fh_ord=fh['ord']
        fhi=[]
        for fh_ in fh_ord:
            fhi.append(''.join(fh[fh_]))
        fi='\n\n'.join(fhi)
        fhi_=  f"{ttr}\n\n {fi}" 
        return fhi_

    def fihirana2(fhr,ttr):
        if len(fhr)==1:    
            fhr=f"00{fhr}"    
        elif len(fhr)==2:
            fhr=f"0{fhr}"
        else:
            fhr=fhr

        with open((f"{chm_fihirana2}\\{fhr}.json"), "r", encoding='utf-8') as fichier:
            donnees = json.load(fichier)
        #fh=fihirana("001 TSY MISY TANTARA")
        fh=donnees
        ttr=ttr
        fh_ord=fh['ord']
        fhi=[]
        for fh_ in fh_ord:
            fhi.append(''.join(fh[fh_]))
        fi='\n'.join(fhi)
        fhi_=  f"{ttr}\n {fi}" 
        return fhi_

    def fihirana_1_get_lohateny(inn):
        f =open(f"{current_link}\\files\\dependances\\fihirana1.txt", "r", encoding='utf-8')
        texts= f.readlines()
        for te in texts:
            t = te.replace('\n','')
            tex=t.split('\t')

            if tex[0]==inn:
                tte=tex
                break
            else:tte=['', '', '', '']
        return tte
    
    def fihirana_2_get_lohateny(self):
        pass

    def fihirana1_get(inn):
        f =open(f"{current_link}\\files\\dependances\\fihirana1.txt", "r", encoding='utf-8')
        texts= f.readlines()
        for te in texts:
            t = te.replace('\n','')
            tex=t.split('\t')

            if tex[0]==inn:
                tte=tex
                break
            else:tte=['', '', '', '']
        return tte

    def fihirana2_get(inn):
        f =open(f"{current_link}\\files\\dependances\\fihirana2.txt", "r", encoding='utf-8')
        texts= f.readlines()
        for te in texts:
            t = te.replace('\n','')
            tex=t.split('\t')

            if tex[0]==inn:
                tte=tex
                break
            else:tte=['', '', '', '']
        return tte
    
    def fihirana1_nd_scren(fhr):
        if len(fhr)==1:    
            fhr=f"00{fhr}"    
        elif len(fhr)==2:
            fhr=f"0{fhr}"
        else:
            fhr=fhr
#, encoding='utf-8'
        with open((f"{chm_fihirana1}\\{fhr}.json"), "r", encoding='utf-8') as fichier:
            donnees = json.load(fichier)
        fh=donnees
        fh_ord=fh['ord']
        fhi=[]
        
        for fh_ in fh_ord:
            fi=''.join(fh[fh_])
            fhi.append(fi)
        return fhi
    
    def fihirana2_nd_scren(fhr):
        if len(fhr)==1:    
            fhr=f"00{fhr}"    
        elif len(fhr)==2:
            fhr=f"0{fhr}"
        else:
            fhr=fhr
#, encoding='utf-8'
        with open((f"{chm_fihirana2}\\{fhr}.json"), "r", encoding='utf-8') as fichier:
            donnees = json.load(fichier)
        fh=donnees
        fh_ord=fh['ord']
        fhi=[]
        
        for fh_ in fh_ord:
            fi=''.join(fh[fh_])
            fhi.append(fi)
        return fhi
    
class baiboly_G():
    def trad(inn,lng):
        f =open(f"{current_link}\\files\\dependances\\trad.txt", "r", encoding='utf-8')
        texts= f.readlines()
        for te in texts:
            t = te.replace('\n','')
            tex=t.split('\t')
            
            
            if tex[1]==inn:
                tte=tex[lng]
                break
            else:tte=""#f"{inn},{inn}"
        return tte

    def baiboly(b):
        baiboly=b.split(' ')
    #print(baiboly[0])
        with open(f"{chm_baiboly}\\{baiboly_G.trad(baiboly[0],1)}.json", "r", encoding='utf-8') as fichier:
            donnees = json.load(fichier)
        bb_chpt=donnees[f"Chapitre {baiboly[1]}"]
        bb_v=baiboly[3]
        bb_vr=bb_v.split(',')
        #print(f"bb_vr({bb_vr})")
        #print(len(bb_vr))
        if len(bb_vr)==1:
            bb_vrs=bb_vr[0].split('-')
            #print(f"bb_vrs({bb_vrs})")
            if len(bb_vrs)==1:
            #    print("len 1")
                bbl1=''.join(bb_chpt[int(bb_vrs[0])-1])
                bbl2=''
                bbl3=''
            else:
                bbl1= ''.join(bb_chpt[int(bb_vrs[0])-1:int(bb_vrs[1])])
                bbl2=''
                bbl3=''
                #bbl=f'" {bbl_} "'

        elif len(bb_vr)==2:
            bb_vrs1=bb_vr[0].split('-')
            bb_vrs2=bb_vr[1].split('-')
            #print(f"bb_vrs({bb_vrs})")
            if len(bb_vrs1)==1 and len(bb_vrs2)==1:
            #    print("len 1")
                bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1])
                bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1])
                bbl3=''
            elif len(bb_vrs1)==2 and len(bb_vrs2)==1:
            #    print("len 1")
                bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1:int(bb_vrs1[1])])
                bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1])
                bbl3=''
            elif len(bb_vrs1)==1 and len(bb_vrs2)==2:
            #    print("len 1")
                bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1])
                bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1:int(bb_vrs2[1])])
                bbl3=''
            elif len(bb_vrs1)==2 and len(bb_vrs2)==2:
            #    print("len 1")
                bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1:int(bb_vrs1[1])])
                bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1:int(bb_vrs2[1])])
                bbl3=''
            
            else:
                bbl1=''
                bbl2=''
                bbl3=''

        # elif len(bb_vr)==3:
        #     bb_vrs1=bb_vr[0].split('-')
        #     bb_vrs2=bb_vr[1].split('-')
        #     bb_vrs3=bb_vr[2].split('-')
        #     #print(f"bb_vrs({bb_vrs})")
        #     if len(bb_vrs1)==1 and len(bb_vrs2)==1 and len(bb_vrs3)==1:
        #     #    print("len 1")
        #         bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1])
        #         bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1])
        #         bbl3=''.join(bb_chpt[int(bb_vrs3[0])-1])
        #     elif len(bb_vrs1)==2 and len(bb_vrs2)==1 and len(bb_vrs3)==1:
        #     #    print("len 1")
        #         bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1:int(bb_vrs1[1])])
        #         bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1])
        #         bbl3=''.join(bb_chpt[int(bb_vrs3[0])-1])
        #     elif len(bb_vrs1)==1 and len(bb_vrs2)==2 and len(bb_vrs3)==1:
        #     #    print("len 1")
        #         bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1])
        #         bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1:int(bb_vrs2[1])])
        #         bbl3=''.join(bb_chpt[int(bb_vrs3[0])-1])

        #     elif len(bb_vrs1)==1 and len(bb_vrs2)==2 and len(bb_vrs3)==1:
        #     #    print("len 1")
        #         bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1])
        #         bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1:int(bb_vrs2[1])])
        #         bbl3=''.join(bb_chpt[int(bb_vrs3[0])-1])
        #     elif len(bb_vrs1)==2 and len(bb_vrs2)==2 and len(bb_vrs3)==1:
        #     #    print("len 1")
        #         bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1:int(bb_vrs1[1])])
        #         bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1:int(bb_vrs2[1])])
        #         bbl3=''.join(bb_chpt[int(bb_vrs3[0])-1])

        #     """-------------------------222-------------------------"""
        #     if len(bb_vrs1)==1 and len(bb_vrs2)==1 and len(bb_vrs3)==2:
        #     #    print("len 1")
        #         bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1])
        #         bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1])
        #         bbl3=''.join(bb_chpt[int(bb_vrs3[0])-1:int(bb_vrs3[1])])

        #     elif len(bb_vrs1)==2 and len(bb_vrs2)==1 and len(bb_vrs3)==2:
        #     #    print("len 1")
        #         bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1:int(bb_vrs1[1])])
        #         bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1])
        #         bbl3=''.join(bb_chpt[int(bb_vrs3[0])-1:int(bb_vrs3[1])])

        #     elif len(bb_vrs1)==1 and len(bb_vrs2)==2 and len(bb_vrs3)==2:
        #     #    print("len 1")
        #         bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1])
        #         bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1:int(bb_vrs2[1])])
        #         bbl3=''.join(bb_chpt[int(bb_vrs3[0])-1:int(bb_vrs3[1])])

        #     elif len(bb_vrs1)==1 and len(bb_vrs2)==2 and len(bb_vrs3)==2:
        #     #    print("len 1")
        #         bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1])
        #         bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1:int(bb_vrs2[1])])
        #         bbl3=''.join(bb_chpt[int(bb_vrs3[0])-1:int(bb_vrs3[1])])

        #     elif len(bb_vrs1)==2 and len(bb_vrs2)==2 and len(bb_vrs3)==2:
        #     #    print("len 1")
        #         bbl1=''.join(bb_chpt[int(bb_vrs1[0])-1:int(bb_vrs1[1])])
        #         bbl2=''.join(bb_chpt[int(bb_vrs2[0])-1:int(bb_vrs2[1])])
        #         bbl3=''.join(bb_chpt[int(bb_vrs3[0])-1:int(bb_vrs3[1])])


        #     else:
        #         bbl1=''
        #         bbl2=''
        #         bbl3=''

        
        #bb_vr_1=bb_vr[0]
        #bb_vr_2=bb_vr[1]
        #bb_vrs=bb_vr_1.split('-')
        #bb_vrs[1]
        #
        ##if bb_vr==IndexError():
        ##    
        #if bb_vr_2:
        #    bb_vrs_2=bb_vr_2.split('-')
        #    bbl=''.join(bb_chpt[int(bb_vrs[0])-1:int(bb_vrs[1])],bb_chpt[int(bb_vrs_2[0])-1:int(bb_vrs_2[1])])
        #else:
        #    pass
#
        #bbl=bb_chpt[int(bb_vrs[0])-1:int(bb_vrs[1])]
        return bbl1,bbl2

    def gen_list():
        list_bbl_at=[]
        list_bbl_nt=[]
        f_at =open(f"{current_link}\\files\\dependances\\at.txt", "r", encoding='utf-8')
        f_nt =open(f"{current_link}\\files\\dependances\\nt.txt", "r", encoding='utf-8')
        texts_at= f_at.readlines()
        texts_nt= f_nt.readlines()
        for te in texts_nt:
            t = te.replace("\n",'')
            tex=t.split('\t')
            list_bbl_nt.append(tex[0])

        for te in texts_at:
            t = te.replace("\n",'')
            tex=t.split('\t')
            list_bbl_at.append(tex[0])

        return list_bbl_at, list_bbl_nt

class export_files():
    def export_out_file(fl):
        with open(f"{current_link}\\files\\dependances\\scrn1_out.json", "w") as f:
            json.dump(fl,f,indent=4, ensure_ascii= False, sort_keys=False)

        pass

    def ajout_historique(fl,ntr):
        a=time.asctime()
        a=a.split(' ')
        filtr=f"{a[4]} {a[1]} {a[4]}-{a[2]} {a[3]} ({a[0]})"  
        #historique_dict[filtr]=fl
        with open(f"{current_link}\\files\\dependances\\Historique.json", "r",encoding='utf-8') as f:
            dt=json.load(f)
            dt[filtr]=ntr,fl

        with open(f"{current_link}\\files\\dependances\\Historique.json", "w",encoding='utf-8') as f:
            json.dump(dt,f,indent=4, ensure_ascii= False, sort_keys=False)

        pass

    def sauvegarde_param():
        pass

class Save_file():
    def __init__(self,out_fl,fl,ntr):
        self.export_out_file(out_fl)
        self.ajout_historique(fl,ntr)

    def export_out_file(self,out_fl):
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()
        #print(out_fl['type'], out_fl['titre'], out_fl['content'], type(out_fl['ord_diff']))
        j_dt=json.dumps(out_fl)
        curseur.execute('INSERT OR REPLACE INTO scrn1_out(type, titre, content, ord_diff) VALUES (?, ?, ?, ?)', (out_fl['type'], out_fl['titre'], j_dt, out_fl['ord_diff']))
        connexion.commit()
        connexion.close()
    
    def ajout_historique(self,fl,ntr):
        connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
        curseur = connexion.cursor()
        a=time.asctime()
        a=a.split(' ')
        #filtr=f"{a[4]} {a[1]} {a[4]}-{a[2]} {a[3]} ({a[0]})"  
        #print(fl,ntr, filtr)
        curseur.execute('INSERT OR REPLACE INTO Historique(jour, date, heure, type, content) VALUES (?, ?, ?, ?, ?)', (a[0], a[2], a[3], ntr, fl))
        connexion.commit()
        connexion.close()


flii={'type': 'FIHIRANA', 'titre': ' MANGINA, MANGINA ', 'content': ["1\nMangina, mangina\nHenoy fa injao \n'Lay Tompo irina \nMiteny aminao \n", 'Henoy fa miteny \nAm-ponao izao \nMiteny, mifona \nFa tia anao \n', '2\nMangina, mangina \nFeo mamy tokoa \nMitory hafaliana \n‘Njao re ao am-po \n', 'Ekeko ry Tompo \nMangina aho izao \nMangina ny foko \nHihaino Anao \n'], 'ord_diff': 4}

#Save_file(flii,'','')
#reqq='1Chroniques'
#connexion = sqlite3.connect(f"{current_link}//db.sqlite3")
#curseur = connexion.cursor()
#curseur.execute("SELECT Content_file FROM Baiboly WHERE Bible = ?",reqq)
#result=curseur.fetchone()
#
#print((result))
#result=result[0]
#result=str(result).split(', ')
#print(type(result))
#print(result)
#print(type(fl))
#Save_file('file','baiboly')