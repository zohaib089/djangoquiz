from django.contrib import admin

from .models import Choice,Question,EvaluationTest,GradeEvaluationText,Category
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(EvaluationTest)
admin.site.register(GradeEvaluationText)
admin.site.register(Category)

