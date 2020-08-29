from django.shortcuts import render,get_object_or_404,redirect
from .forms import WordForm
from .models import Word
from django.contrib.auth.models import User
from django.contrib import messages
def index(request):
    return render(request,"index.html")

def wordsHome(request):
    
    try:
        words = Word.objects.filter(category = "home").order_by('-created_date')
    except Word.DoesNotExist:
        words = None
    #if words is not None:
    return render(request,"wordsHome.html",{
        'words':words,
        })
             
def wordsFoods(request):
    try:
        words = Word.objects.filter(category = "food").order_by('-created_date')
    except Word.DoesNotExist:
        words = None
    #if words is not None:
    return render(request,"wordsFoods.html",{
        'words':words,
        })


def detail(request,id):
    word = get_object_or_404(Word,id=id)
    #form = WordForm(request.POST or None)
    #if form.is_valid():
    #    word.content = form.cleaned_data['content']
    return render(request,"detail.html",{'word':word})

def deleteWord(request,id):
    word = get_object_or_404(Word,id = id)
    user = request.user
    category = word.category
    if user.is_superuser or user == word.author:
        messages.success(request,"Kelime başarıyla silindi.")
        word.delete()
    return redirect(category)

def addWord(request):
    if request.method == "POST":
        word_en = request.POST.get("word_en")
        word_tr = request.POST.get("word_tr")
        category = request.path.split('/')[3]
        author = request.user
        words = Word.objects.filter(category = category)
        for word in words:
            if str(word).lower() == str(word_en).lower():
                messages.error(request,"Eklemeye çalıştığınız kelime daha önceden eklenmiş!")
                return redirect(category)
        messages.success(request,"Kelime başarıyla eklendi.")
        word = Word(word_en = word_en , word_tr=word_tr,category=category,author=author)
        word.save()
        return redirect(category)
     
    return render(request,"addWord.html")


def myWords(request):
    try:
        words = Word.objects.filter(author = request.user)
    except Word.DoesNotExist:
        words = None
    return render(request,"myWords.html",{'words':words})