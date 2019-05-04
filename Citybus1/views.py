from django.shortcuts import render
import random
from django.http import HttpResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound
from .froms import Authform, Regform, Busform, Driform, Schform
from .models import User, Admin, Bus, Driver, Schedule, Ticket
from django.forms.models import model_to_dict
def Auth(request):
	if request.method == "POST":
		log = request.POST.get("login")
		pas = request.POST.get("password")
		users = User.objects.all()
		admins = Admin.objects.all()
		for us in users:
			if us.log == log and us.pas == pas:
				request.session['cur'] = model_to_dict(us)
				us.save()
				return HttpResponseRedirect('user/')
		for ad in admins:
			if ad.log == log and ad.pas == pas:
				request.session['cur'] = model_to_dict(ad)
				return HttpResponseRedirect('admin/')
		return HttpResponseNotFound("<h2>Such User Not Found</h2>")
	forma = Authform()
	return render(request, 'index.html', {"form": forma})

def Reg(request):
	forma = Regform()
	if request.method == "POST":
		new = User()
		new.log = request.POST.get("log")
		new.pas = request.POST.get("pas")
		new.nam = request.POST.get("nam")
		new.sur = request.POST.get("sur")
		new.age = int(request.POST.get("age"))
		new.rol = request.POST.get("rol")
		new.save()
		return HttpResponseRedirect('/')
	return render(request, 'reg2.html', {"form": forma})
	
def user(request):
	us = User.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	return render(request, 'user.html', {'us': us})
def admin(request):
	ad = Admin.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	return render(request, 'admin.html', {'ad': ad})
def logout(request):
	del request.session['cur']
	return HttpResponseRedirect('/')
def addbus(request):
	ad = Admin.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	form = Busform()
	if request.method == "POST":
		new = Bus()
		new.num = request.POST.get("num")
		new.mar = request.POST.get("mar")
		new.mod = request.POST.get("mod")
		new.path = request.POST.get("path")
		new.yea = int(request.POST.get("yea"))
		new.sea = int(request.POST.get("sea"))
		new.cap = int(request.POST.get("cap"))
		new.save()
		return HttpResponseRedirect('/admin')
	return render(request, 'addbus.html', {"form": form, "ad": ad})
def adddri(request): 
	ad = Admin.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	form = Driform()
	if request.method == "POST":
		new = Driver()
		new.log = request.POST.get("log")
		new.pas = request.POST.get("pas")
		new.nam = request.POST.get("nam")
		new.sur = request.POST.get("sur")
		new.path = request.POST.get("path")
		new.age = int(request.POST.get("age"))
		new.cla = int(request.POST.get("cla"))
		new.save()
		return HttpResponseRedirect('/admin')
	return render(request, 'adddri.html', {"form": form, "ad": ad})
def addschint(request):
	ad = Admin.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	form = Schform()
	dlist = Driver.objects.all()
	blist = Bus.objects.all()
	if request.method == "POST":
		news = Schedule()
		news.sou = request.POST.get("sou")
		news.des = request.POST.get("des")
		news.dep = request.POST.get("dep")
		news.arr = request.POST.get("arr")
		news.pri = int(request.POST.get("pri"))
		news.bus = Bus.objects.get(id=int(request.POST.get("bus")))
		news.dri = Driver.objects.get(id=int(request.POST.get("dri")))
		news.save()
		for gh in range(news.bus.sea):
			newt = Ticket()
			if request.POST.get('che')==None:
				newt.ocu = False
				newt.hol = User.objects.get(id=1)
			else:
				zin = random.randint(0, 1)
				if zin == 1:
					newt.ocu = True
					newt.hol = User.objects.get(id=3)
				else:
					newt.ocu = False
					newt.hol = User.objects.get(id=1)
			newt.sea = gh+1
			newt.sch = news
			newt.save()
		return HttpResponseRedirect('/admin') 
	return render(request, 'addschint.html', {"form": form, 'dlist': dlist, 'blist': blist, 'ad': ad})
def viewD(request):
	ad = Admin.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	dlist = Driver.objects.all()
	return render(request, 'viewD.html', {'dlist': dlist, "ad": ad})
def viewB(request):
	ad = Admin.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	blist = Bus.objects.all()
	return render(request, 'viewB.html', {'blist': blist, "ad": ad})
def viewTint(request):
	ad = Admin.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	ids = int(request.GET.get('sch'))
	zoro = Schedule.objects.get(id = ids)
	tlist = Ticket.objects.filter(sch = zoro)
	return render(request, 'viewTint.html', {'tlist': tlist, "ad": ad, "zoro": zoro})
def viewSint(request):
	ad = Admin.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	slist = Schedule.objects.all()
	return render(request, 'viewSint.html', {'slist': slist, "ad": ad})
def viewBT(request):
	us = User.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	tlist = Ticket.objects.filter(hol = us, ocu = True)
	return render(request, 'viewBT.html', {'tlist': tlist, "us": us})
def buyT(request):
	us = User.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	tlist = Ticket.objects.all()
	zipo = list()
	for re in tlist:
		if re.ocu==False and re.sch not in zipo:
			zipo.append(re.sch)
	return render(request, 'buyT.html', {"us": us, "tlist": tlist, "zipo": zipo})
def findz(request):
	us = User.objects.get(id=request.session.get('cur')['id'], log=request.session.get('cur')['log'], pas=request.session.get('cur')['pas'])
	ids = request.GET.get('sch')
	ds = 0;
	vf =0;
	ob = Schedule.objects.get(id=str(ids))
	tlist = Ticket.objects.filter(sch=ob)
	if ob.bus.sea<11:
		ds = 260
		vf = 23
	elif ob.bus.sea<21:
		ds = 320
		vf = 52
	else:
		ds = 400
		vf = 92
	if request.method=="POST":
		num = int(tlist[0].id)
		halla = request.POST.get(str(num))
		while halla:
			if int(halla)==1:
				sir = Ticket.objects.get(id = num)
				sir.hol = us
				sir.ocu = True
				sir.save()
			num = num + 1
			halla = request.POST.get(str(num))
		return HttpResponseRedirect('/user')
	return render(request, 'findz.html', {'s': ob, 'tlist': tlist, "us": us, "ds": ds, "vf": vf})