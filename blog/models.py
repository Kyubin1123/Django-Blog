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

    # 제목이 노출되는 방식 설정
    def __str__(self):
        return f'[{self.get_category_display()}]{self.title}'

    # Meta 클래스 코드 추가
    class Meta:
        verbose_name : "블로그"
        verbose_name_plural : "블로그 목록"