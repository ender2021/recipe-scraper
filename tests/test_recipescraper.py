# -*- coding: utf-8 -*-

from .context import recipescraper

html = recipescraper.get_recipe_html("https://www.blueapron.com/recipes/butter-soy-glazed-chicken-with-sesame-vegetables-brown-rice")

with open("response.html", "wb") as f:
    f.write(html)