from django.contrib import admin

from .models import Tag, Ingredient, Recipe, IngredientRecipe, FavoriteRecipe

admin.site.register(Tag)
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(IngredientRecipe)
admin.site.register(FavoriteRecipe)