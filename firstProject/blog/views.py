from django.shortcuts import render

# Create your views here.
def blog_index(request):
    articles = [
    {"id" : 1, "title": "Article Title 1", "content": "Lorem ipsum dolor sit amet.", "created_at": "2024-11-10 12:00:00"},
    {"id" : 2, "title": "Article Title 2", "content": "Curabitur vehicula, dui eu feugiat.", "created_at": "2024-11-11 15:30:00"},
    {"id" : 3, "title": "Article Title 3", "content": "Phasellus accumsan, arcu non feugiat.", "created_at": "2024-11-12 09:45:00"},
    ]
    context = {'articles': articles}
    return render(request,'blog/index.html' , context)

def articles(request, id):
    # In your case, the articles are static, but you can filter the list using the ID
    articles = [
        {"id": 1, "title": "Article Title 1", "content": "Lorem ipsum dolor sit amet.", "created_at": "2024-11-10 12:00:00"},
        {"id": 2, "title": "Article Title 2", "content": "Curabitur vehicula, dui eu feugiat.", "created_at": "2024-11-11 15:30:00"},
        {"id": 3, "title": "Article Title 3", "content": "Phasellus accumsan, arcu non feugiat.", "created_at": "2024-11-12 09:45:00"},
    ]
    # Find the article by id
    article = next((item for item in articles if item["id"] == id), None)
    print("articles: " , article)
    return render(request, 'blog/articles.html', {'article': article})

