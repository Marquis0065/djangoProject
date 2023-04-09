from django.shortcuts import render
from django.http import HttpResponse
from blog2.models import Article
from django.core.paginator import Paginator
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
    page = request.GET.get('page')
    if page:
        page=int(page)
    else:
        page=1
    print('page param：',page)
    all_article=Article.objects.all()
    top_article = Article.objects.order_by('-publish_date')[:2]
    paginator = Paginator(all_article,3)
    page_num=paginator.num_pages
    print('page num:',page_num)
    page_article_list = paginator.page(page)
    if page_article_list.has_next():
        next_page = page+1
    else:
        next_page=page
    if page_article_list.has_previous():
        pre_page=page-1
    else:
        pre_page=page
    return render(request,'blog2/index.html',{
        'article_list':page_article_list,
        'page_num':range(1,page_num+1),
        'curr_page':page,
        'next_page':next_page,
        'pre_next':pre_page,
        'top_article':top_article
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