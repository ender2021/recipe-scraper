from bs4 import BeautifulSoup
from typing import List
from .classes import RecipeStep

def get_soup(doc: str):
    return BeautifulSoup(doc, 'lxml')

def get_ingredients(soup: BeautifulSoup) -> List[str]:
    list = []
    
    for ing in soup.find_all(itemprop='recipeIngredient'):
        list.append(ing.get_text(" ", strip=True).replace("\n", " "))
    
    return list

def get_title(soup: BeautifulSoup) -> str:
    mainTitle = soup.find("h1", "ba-recipe-title__main").get_text(strip=True)
    subTitle = soup.find("h2", "ba-recipe-title__sub").get_text(strip=True)
    return " ".join([mainTitle, subTitle])

def get_cooktime(soup: BeautifulSoup) -> str:
    return soup.find("span", "total-time").get_text(strip=True)

def get_servings(soup: BeautifulSoup) -> str:
    return soup.find(itemprop='recipeYield').get_text(strip=True)

def get_description(soup: BeautifulSoup) -> str:
    return soup.find(itemprop='description').get_text(strip=True)

def get_steps(soup: BeautifulSoup) -> List[RecipeStep]:
    list = []
    
    instructions = soup.find("section", "recipe-instructions")
    
    for step in instructions.find_all(itemprop='recipeInstructions'):
        imgUrl = step.find_previous()["src"]
        number = step.find("span", "step-number").get_text(strip=True)
        title = step.find("span", "step-title").get_text(strip=True)
        txt = step.find("div", "step-txt").get_text(" ", strip=True)
        list.append(RecipeStep(number, title, txt, imgUrl))
    
    return list

def get_hero_img_url(soup: BeautifulSoup):
    return soup.find("div", "ba-hero-image__hldr").find("img")['src']