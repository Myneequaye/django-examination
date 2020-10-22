from django.contrib import admin
from .models import Question, Quiz, Subject, TakenQuiz, Student, StudentAnswer, Answer
from .forms import BaseAnswerInlineFormSet

class AnswerInline(admin.TabularInline):
    '''Tabular Inline View for Answer'''

    model = Answer
    can_delete = False
    min_num = 4
    max_num = 5
    extra = 1
    formset = BaseAnswerInlineFormSet

    
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    '''Admin View for Question'''

    model = Question
    list_display = ('quiz','text')
    list_filter = ('text',)
    inlines = (AnswerInline,)
    search_fields = ('quiz',)
    actions = None

admin.site.register(Quiz)
admin.site.register(Subject)
admin.site.register(TakenQuiz)
admin.site.register(Student)
admin.site.register(StudentAnswer)
