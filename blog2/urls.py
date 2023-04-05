# @Time: 2023/4/5 15:20
# _*_coding : utf-8 _*_
# @Authon : 
# @File : utils
# 应用 层次路由配置
from django.urls import path,include
import blog2.views
urlpatterns = [
    path('hello_world',blog2.views.hello_world),
    path('content',blog2.views.article_content),
    path('index',blog2.views.get_index_page),
    # path('detail',blog2.views.get_detail_page)
    path('detail/<int:article_id>', blog2.views.get_detail_page)

]