from django.contrib import admin

from .models import Course
from .models import CourseHoleDetail

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
                    'legacy_id','course_name','course_short_name','active'
                    )
    list_filter = ('active',)
    search_fields = ('course_name','course_short_name')


@admin.register(CourseHoleDetail)
class CourseHoleDetailAdmin(admin.ModelAdmin):
    list_display = ('course','hole_num', 'men_par', 'men_hcp', 'ladies_par', 'ladies_hcp')
    list_filter = ('course',)
