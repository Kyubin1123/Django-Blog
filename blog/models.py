from django.db import models

class Blog(models.Model):
    CATEGORY_CHOICES = (
        ('romans', '로맨스'),
        ('fantasy', '판타지'),
        ('thriller', '스릴러'),
        ('mystery', '미스터리'),
        ('comic', '코믹'),
        ('diary', '하루일기')
    )

    category = models.CharField('카테고리',max_length=10, choices=CATEGORY_CHOICES)
    title = models.CharField('제목',max_length=50)
    content = models.TextField('본문')

    create_at = models.DateTimeField('작성일자', auto_now_add=True)
    update_at = models.DateTimeField('작성일자', auto_now=True)

