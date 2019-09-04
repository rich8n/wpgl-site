from django.contrib import admin

from .models import Golfer
from .models import Team

@admin.register(Golfer)
class GolferAdmin(admin.ModelAdmin):
    list_display = (
                    'identifier','legacy_id','firstname', 'lastname', 'suffix',
                    'tees','team','active','role','email','phone'
                    )
    list_filter = ('team','tees','active','role')
    search_fields = ('lastname','firstname','team')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'active', 'bye_team', 'comment')
