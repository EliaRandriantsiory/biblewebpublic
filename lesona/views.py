from django.shortcuts import render,redirect
from .models import *

def indexLesona(request):
    return render(request, "lesonahome.html")

def listLesona(request):
    titreLesona = lesona.objects.all()
    sTitre = sousTitre.objects.all()
    context={
        "titreLesona":titreLesona,
        "soustitre":sTitre,
    }
    return render(request, 'lesonaList.html',context)

def viewContent(request, title):
    
    try:
        #print(title)
        titrelesona=lesona.objects.get(Titre=title)
        
        subtitle = sousTitre.objects.all()
        contentt=fanazavana.objects.all()
        #subTitle = fanazavana.objects.get(sousTitre=sousTitre.objects.get(titre=titre))
        print(subtitle)
        print(contentt)
        print(titrelesona)
        
        context={"title":titrelesona,"sousTitres":subtitle,"contents":contentt}
        return render(request,'viewContent.html',context)
    except:
        print(title)
        fanazavanacontent= fanazavana.objects.get(sousTitre=sousTitre.objects.get(sousTitre=title))
        context={"title":title,"content":fanazavanacontent}
        return render(request,'viewContent.html',context)

def ajoutContent(request, title):
    #print(title)
    try:
        lesona.objects.get(Titre=title)
        if request.method == "POST":
                soustitre = request.POST.get("soustitre")
                content = request.POST.get("soustitreContent")
                tokoSyAndininy = request.POST.get("tokoSyAndininy")
                if sousTitre != "":
                    subTitle = sousTitre(sousTitre=soustitre,titre=lesona.objects.get(Titre=title))
                    subTitle.save()
                ctnt= fanazavana(fanazavana=content,tokoSyAndininy=tokoSyAndininy,sousTitre=sousTitre.objects.get(soustitre=soustitre))
                ctnt.save()
            
                return redirect("listLesona")
        context={"title":title,"etat":True}
        return render(request,"ajoutContent.html",context)
    except:
        
        if request.method == "POST":
            content = request.POST.get("soustitreContent")
            tokoSyAndininy = request.POST.get("tokoSyAndininy")
            #print(title)
            ctnt= fanazavana(fanazavana=content,tokoSyAndininy=tokoSyAndininy,sousTitre=sousTitre.objects.get(sousTitre=title))
            ctnt.save()
            # if content !="":
            #     ctnt= fanazavana(fanazavana=content,sousTitre=sousTitre.objects.get(sousTitre=title))
            #     ctnt.save()
            # form.save()
            return redirect("listLesona")
        sub=sousTitre.objects.get(sousTitre=title)
        context={"title":sub,"etat":False}
        return render(request,"ajoutContent.html",context)
        
        
    # try:
    #     lesona.objects.get(Titre=title)
    #     #print(titre)
    #     if request.method == "POST":
    #         soustitre = request.POST.get("soustitre")
    #         content = request.POST.get("soustitreContent")
    #         tokoSyAndininy = request.POST.get("tokoSyAndininy")
    #         if sousTitre != "":
    #             subTitle = sousTitre(sousTitre=soustitre,titre=lesona.objects.get(Titre=title))
    #             subTitle.save()
    #         ctnt= fanazavana(fanazavana=content,tokoSyAndininy=tokoSyAndininy,sousTitre=sousTitre.objects.get(soustitre=soustitre))
    #         ctnt.save()
           
    #         return redirect("listLesona")
    #     context={"title":title,"etat":True}
    #     return render(request,"ajoutContent.html",context)
    # except:
    #     if request.method == "POST":
    #         content = request.POST.get("soustitreContent")
    #         tokoSyAndininy = request.POST.get("tokoSyAndininy")
    #         #print(title)
    #         ctnt= fanazavana(fanazavana=content,tokoSyAndininy=tokoSyAndininy,sousTitre=sousTitre.objects.get(sousTitre=title))
    #         ctnt.save()
    #         # if content !="":
    #         #     ctnt= fanazavana(fanazavana=content,sousTitre=sousTitre.objects.get(sousTitre=title))
    #         #     ctnt.save()
    #         # form.save()
    #         return redirect("listLesona")
    #     sub=sousTitre.objects.get(titre=title)
    #     context={"title":sub,"etat":False}
    #     return render(request,"ajoutContent.html",context)