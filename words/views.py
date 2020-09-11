from django.shortcuts import render,get_object_or_404,redirect,reverse
from .forms import WordForm
from .models import Word,Comment
from django.contrib.auth.models import User
from django.contrib import messages
import string
def index(request):
    return render(request,"index.html")

def wordsHome(request):
    
    try:
        words = Word.objects.filter(category = "home").order_by('-created_date')
    except Word.DoesNotExist:
        words = None
    return render(request,"wordsHome.html",{
        'words':words,
        })
             
def wordsFoods(request):
    try:
        words = Word.objects.filter(category = "food").order_by('-created_date')
    except Word.DoesNotExist:
        words = None
    return render(request,"wordsFoods.html",{
        'words':words,
        })

def wordsTechnology(request):
    try:
        words = Word.objects.filter(category = "technology").order_by('-created_date')
    except Word.DoesNotExist:
        words = None
    return render(request,"wordsTechnology.html",{
        'words':words,
        })
def wordsTransportation(request):
    try:
        words = Word.objects.filter(category = "transportation").order_by('-created_date')
    except Word.DoesNotExist:
        words = None
    return render(request,"wordsTransportation.html",{
        'words':words,
        })
def wordsVerbs(request):
    try:
        words = Word.objects.filter(category = "verb").order_by('-created_date')
    except Word.DoesNotExist:
        words = None
    return render(request,"wordsVerbs.html",{
        'words':words,
        })
def wordsGeneral(request):
    try:
        words = Word.objects.filter(category = "general").order_by('-created_date')
    except Word.DoesNotExist:
        words = None
    return render(request,"wordsGeneral.html",{
        'words':words,
        })

def detail(request,id):
    word = get_object_or_404(Word,id=id)
    word.word_en = string.capwords(word.word_en)
    comments = word.comments.all()
    if request.method == "POST":
        sentence = request.POST.get("sentence")
        new_comment = Comment(comment_content =sentence,word = word)
        new_comment.comment_author = request.user
        new_comment.save()
    return render(request,"detail.html",{'word':word,'comments':comments})

def updateWord(request,id):
    word = get_object_or_404(Word,id = id)
    if request.method == "POST":
        word.word_en = request.POST.get("word_en")
        word.word_tr = request.POST.get("word_tr")
        word.save()
        return redirect("words:"+word.category)
    return render(request,"wordUpdate.html",{'word':word})

def deleteWord(request,id):
    word = get_object_or_404(Word,id = id)
    user = request.user
    category = word.category
    if user.is_superuser or user == word.author:
        messages.success(request,"Kelime başarıyla silindi.")
        word.delete()
    return redirect("words:"+category)



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
                return redirect("words:"+category)
        messages.success(request,"Kelime başarıyla eklendi.")
        word = Word(word_en = word_en , word_tr=word_tr,category=category,author=author)
        word.save()
        return redirect("words:"+category)
     
    return render(request,"addWord.html")


def myWords(request):
    try:
        words = Word.objects.filter(author = request.user)
    except Word.DoesNotExist:
        words = None
    for word in words:
        word.category = string.capwords(word.category)
    return render(request,"myWords.html",{'words':words})


#COMMENT 

def deleteComment(request,id):
    comment = get_object_or_404(Comment,id = id)
    user = request.user
    if user.is_superuser or user == comment.comment_author:
        messages.success(request,"Yorum başarıyla silindi.")
        comment.delete()
    return redirect("index")

def updateComment(request,id):
    if request.method == "POST":
        comment = get_object_or_404(Comment,id = id)
        user = request.user
        if user.is_superuser or user == comment.comment_author:
            messages.success(request,"Yorum başarıyla güncellendi.")
            comment.comment_content = request.POST.get("sentence")
            comment.save()
            return redirect(reverse("words:detail",kwargs={'id':comment.word.id}))
    return render(request,"comment/updateComment.html")
