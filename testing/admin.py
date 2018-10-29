from django.contrib import admin
from django.utils.safestring import mark_safe

from testing.models import Test, Question, Answer, UserAnswer

# Register your models here.


class QuestionInline(admin.TabularInline):
    model = Question
    min_num = 1
    max_num = 10
    extra = 0


class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'level', 'updated_at', 'get_image')
    search_fields = ('name',)
    list_filter = ('level', 'updated_at')
    inlines = [QuestionInline]

    def get_image(self, obj):
        url = obj.image.url if obj.image else None
        if url:
            return mark_safe(f'<img src="{url}"/>')


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 0
    min_num = 1
    max_num = 4


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'test')
    list_display_links = ('number', 'name')
    list_filter = ('test', )
    search_fields = ('name', )
    inlines = [AnswerInline]


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'is_correct',
        'score', 'question'
    )
    list_filter = ('question', 'is_correct')


class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'get_answers')
    list_filter = ('user', )
    readonly_fields = ('user', 'question', 'answer')
    filter_horizontal = ('answer',)

    def get_answers(self, obj):
        return str(obj.answer.all())

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields
        return []


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)
