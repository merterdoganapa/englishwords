from django.shortcuts import render,get_object_or_404,redirect
from .models import Word
from django.contrib.auth.models import User
def index(request):
    return render(request,"index.html")

def wordsHome(request):
    
    try:
        words = Word.objects.filter(category = "home")
    except Word.DoesNotExist:
        words = None
    if words is not None:
        return render(request,"wordsHome.html",{
            'words':words,
            })
             
def wordsFoods(request):
    return render(request,"wordsFood.html")


def detail(request,id):
    word = get_object_or_404(Word,id=id)
    return render(request,"detail.html",{'word':word})

def deleteWord(request,id):
    word = get_object_or_404(Word,id = id)
    category = word.category
    word.delete()
    return redirect(category)

def addWord(request):
    if request.method == "POST":
        word_en = request.POST.get("word_en")
        word_tr = request.POST.get("word_tr")
        category = request.POST.get("sortType")
        author = request.user

        word = Word(word_en = word_en , word_tr=word_tr,category=category,author=author)
        word.save()
        return redirect(category)
    return render(request,"addWord.html")