from django.contrib import admin
from studentsapp.models import student



class studentAdmin(admin.ModelAdmin):
    # 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
	list_display=('id','companyid','num','jobname','name','company','cash')
	list_filter=('companyid','jobname')
	search_fields=('companyid',)
	ordering=('id',)
	
admin.site.register(student,studentAdmin)
