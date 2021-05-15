from django.contrib import admin


from .models import Article # Aynı dizinde oluşturulan sınıf  -model- import ediliyor.
# Register your models here.
from .models import Comment
admin.site.register(Comment)


# admin.site.register(Article) # Bu model admin panelinde gösteriliyor
# Üst satır yorumlandı python decorator oluşturuldu
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ["title", "author", "created_date"] # Admin panelinde özelleştirme -- Tablo da görülmeleri
    list_display_links = [ "title", "created_date"] # sadece başlığa tıklanarak değiş oluşturma tarihine göre de 

    search_fields = ["title"] # Title ile makaleler içerisinde arama yapmak için

    list_filter = ["created_date"] # Süzgeçe göre son yedi gün de geçen yılda yazılanlar diye listelenenler
    class Meta:
        model = Article

