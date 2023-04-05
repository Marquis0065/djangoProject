from django.shortcuts import render
from django.http import HttpResponse
from blog2.models import Article
# Create your views here.
def hello_world(request):
    return HttpResponse('Hello,world,测试')

def article_content(request):
    article = Article.objects.all()[1]
    title = article.title
    brief_content = article.brief_content
    content = article.content
    article_id = article.article_id
    publish_date = article.publish_date
    str = 'title:{},brief_content:{},content:{},' \
          'article_id:{},publish_date:{}'.format(title,
            brief_content,content,article_id,publish_date)
    return HttpResponse(str)

def get_index_page(request):
    all_article=Article.objects.all()
    return render(request,'blog2/index.html',{
        'article_list':all_article
    })

def get_detail_page(request,article_id):
    all_article = Article.objects.all()
    curr_article=None
    preview_index = 0
    next_index = 0
    preview_article=None
    next_article=None
    for index,article in enumerate(all_article):
        if index == 0:
            preview_index=index
            next_index=index+1
        elif index == len(all_article)-1:
            preview_index = index - 1
            next_index=index
        else:
            preview_index=index-1
            next_index=index+1

        if article.article_id==article_id:
            curr_article=article
            preview_article=all_article[preview_index]
            next_article=all_article[next_index]
            break
    return render(request,'blog2/detail.html',{
        'curr_article':curr_article,
        'preview_article':preview_article,
        'next_article':next_article
    })