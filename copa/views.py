from django.shortcuts import render, HttpResponseRedirect
from copa.models import Jogos

def listaJogo(request):
	jogo=Jogos.objects.all()
	return render(request, 'copa.html', {'jogo':jogo})

def salvar(request):
	Brasil = request.POST.get('Brasil')
	Placar1 = request.POST.get('Placar1')
	Croacia = request.POST.get('Croacia')
	Placar2 = request.POST.get('Placar2')

	Brasil = request.POST.get('Brasil')
	Placar1 = request.POST.get('Placar1')
	Mexico = request.POST.get('Mexico')
	Placar2 = request.POST.get('Placar2')

	Brasil = request.POST.get('Brasil')
	Placar1 = request.POST.get('Placar1')
	Camaroes = request.POST.get('Placar2')
	Placar2 = request.POST.get('Camaroes')

	

	jogo = Jogos(Brasil=Brasil,
 Placar2=Placar2,
 Croacia=Croacia,
 Placar1=Placar1,
 Brasil=Brasil,
 Placar2=Placar2,
 Mexico=Mexico,
 Placar1=Placar1,
 Brasil=Brasil,
 Placar2=Placar2,
 Camaroes=Camaroes,
Placar1=Placar1)
	jogo.save()
	return listaJogo(request)




