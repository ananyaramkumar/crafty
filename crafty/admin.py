from django.contrib import admin
from .models import SkillLevel, Category, Diy, Material, Instruction, Favorite, Comment

admin.site.register(SkillLevel)
admin.site.register(Category)
admin.site.register(Diy)
admin.site.register(Material)
admin.site.register(Instruction)
admin.site.register(Favorite)
admin.site.register(Comment)
