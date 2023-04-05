from django.db import models

# Create your models here.
# 先定义 ，再迁移
class Article(models.Model):
    # ID 指定 主键
    article_id = models.AutoField(primary_key=True)
    # 标题
    title = models.TextField()
    # 摘要
    brief_content = models.TextField()
    # 内容
    content = models.TextField()

    # 发布日期
    publish_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title