from django.contrib import admin
from studentsapp.models import student



	
# 第一種方式，未加入 ModelAdmin 類別 
#admin.site.register(student)	

# 第二種方式，加入 ModelAdmin 類別，定義顯示欄位
#class studentAdmin(admin.ModelAdmin):
#	list_display=('id','cName','cSex','cBirthday','cEmail','cPhone','cAddr')
#admin.site.register(student,studentAdmin)


class studentAdmin(admin.ModelAdmin):
    # 第三種方式，加入 ModelAdmin 類別，定義顯示欄位、欄位過濾資料、搜尋和排序
	list_display=('companyid','num','jobname','name','company','cash','no')
	list_filter=('companyid','jobname')
	search_fields=('companyid',)
	ordering=('no',)
	
admin.site.register(student,studentAdmin)
