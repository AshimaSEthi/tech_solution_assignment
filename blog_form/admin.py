from django.contrib import admin
from .models import team_structure
from .models import player_structure
from .models import match_team
from .models import points_table
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('name','created_on')
    list_filter = ("name",)
    
class PostAdmin2(admin.ModelAdmin):
	list_display = ('firstName','lastName','player_jersey_number','imageUri','country')



class PostAdmin3(admin.ModelAdmin):
	list_display = ('first_team','second_team','match_winner')

class PostAdmin4(admin.ModelAdmin):
	list_display = ('points',)
admin.site.register(team_structure, PostAdmin)
admin.site.register(player_structure, PostAdmin2)
admin.site.register(match_team,PostAdmin3)

admin.site.register(points_table,PostAdmin4)