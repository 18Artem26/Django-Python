from django.views.generic import ListView, DetailView
from .models import Article

# Представлення для переліку статей
class ArticleListView(ListView):
    model = Article
    template_name = 'app_blog/article_list.html'
    context_object_name = 'articles'
    paginate_by = 10  # Кількість статей на сторінці

# Представлення для детального перегляду статті
class ArticleDetailView(DetailView):
    model = Article
    template_name = 'app_blog/article_detail.html'
    context_object_name = 'article'
