from django.shortcuts import render
import wikipedia

wikipedia.set_user_agent("WikipediaSearchApp/1.0 (Django student project)")

def home(request):
    if request.method == "POST":
        search = request.POST['search']
        try:
            title = wikipedia.search(search)[0] 
            result = wikipedia.summary(title, sentences = 3, auto_suggest = False) 
        except:
            return render(request, "main/index.html", {"error": "Wrong Input", "search": search})
        return render(request, "main/index.html", {"result": result, "title": title, "search": search})
    return render(request, "main/index.html")
