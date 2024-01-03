from django.test import TestCase
import json,os,textwrap 

current_link=os.getcwd()
image_path=f"{current_link}//images//milky-way-8153503_1280.jpg"
chm_baiboly=f"{current_link}//DB//baiboly"
chm_fihirana=f"{current_link}//DB//fihirana"


class baiboly_G():
    def trad(inn,lng):
        f =open(f"{current_link}\\trad.txt", "r", encoding='utf-8')
        texts= f.readlines()
        for te in texts:
            t = te.replace('\n','')
            tex=t.split('\t')
            
            if tex[0]==inn:
                tte=tex[lng]
                break
            else:tte=''
        return tte

    def baiboly(b):
        baiboly=b.split(' ')
    #print(baiboly[0])
        with open(f"{chm_baiboly}\\{baiboly_G.trad(baiboly[0],1)}.json", "r", encoding='utf-8') as fichier:
            donnees = json.load(fichier)
        bb_chpt=donnees[f"Chapitre {baiboly[1]} "]
        bb_v=baiboly[3]
        bb_vr=bb_v.split(',')
        bb_vrs=bb_vr[0].split('-')
        bb_vrs[1]
        bbl=bb_chpt[int(bb_vrs[0])-1:int(bb_vrs[1])]
        return bbl

    def gen_list():
        list_bbl_at=[]
        list_bbl_nt=[]
        f_at =open(f"{current_link}\\at.txt", "r", encoding='utf-8')
        f_nt =open(f"{current_link}\\nt.txt", "r", encoding='utf-8')
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
