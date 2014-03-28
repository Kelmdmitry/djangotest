from django.shortcuts import render
from django.http import HttpResponse

from django.template.loader import get_template
from django.template import Context

from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView
from django.utils import timezone

from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

from .models import Article
from .forms import ArticleForm, CommentForm

def hello(request):
    name = "Dmitry"
    html = "<html><body>Hi %s, this seems to have worked!</body></html>" %name
    return HttpResponse(html)

def hello_template(request):
    name = 'Dmitry'
    t = get_template('hello_template.html')
    html = t.render(Context({'name': name}))
    return HttpResponse(html)

def hello_template_simple(request):
    name = 'Dmitry'
    return render_to_response('hello_template.html', {'name': name})

class HelloTemplate(TemplateView):

    template_name = 'hello_class.html'

    def get_context_data(self, **kwargs):
        context = super(HelloTemplate, self).get_context_data(**kwargs)
        context['name'] = 'Dmitre'
        return context

# All news
def articles(request):
    language = 'en-us'
    session_language = 'en-us'

    if 'lang' in request.COOKIES:
        language = request.COOKIES['lang']

    if 'lang' in request.session:
        session_language = request.session['lang']

    args = {}
    args.update(csrf(request))
    args['articles'] = Article.objects.all()
    args['language'] = language
    args['session_language'] = session_language

    return render_to_response('article/articles.html', args)

# One news
def article(request, article_id=1):
    return render_to_response('article/article.html',
        {'article': Article.objects.get(id=article_id) })

#session and cook settigs
def lang_function(request, language='en-us'):
    response = HttpResponse("setting language to %s" % language)

    response.set_cookie('lang', language)
    request.session['lang'] = language

    return response

#create model
def create(request):
    if request.POST:
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/articles/all')
    else:
        form = ArticleForm()

    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('article/create_article.html', args)

#like_it
def like_article(request, article_id):
    if article_id:
        a = Article.objects.get(id=article_id)
        count = a.likes
        count += 1
        a.likes = count
        a.save()
    return HttpResponseRedirect('/articles/get/%s' % article_id)

#add_comment
def add_comment(request, article_id):
    a = Article.objects.get(id=article_id)

    if request.method == "POST":
        f = CommentForm(request.POST)
        if f.is_valid():
            c = f.save(commit=False)
            c.pub_date = timezone.now()
            c.article = a
            c.save()
        return HttpResponseRedirect('/articles/get/%s' % article_id)
    else:
        f = CommentForm()

    args = {}
    args.update(csrf(request))
    args['article'] = a
    args['form'] = f
    return render_to_response('article/add_comment.html', args)

#search news
def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    articles = Article.objects.filter(title__contains=search_text)
    return render_to_response('ajax_search.html', {'articles': articles})