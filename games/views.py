from django.shortcuts import render, get_object_or_404, redirect
from bs4 import BeautifulSoup
import requests
from django import template
from django.utils.safestring import mark_safe

register = template.Library()
@register.filter()
def make_the_string_ready(value):
    return mark_safe("%20".join(value.split(' ')))

def api_view(request):
    if 'game_name_input' in request.POST:
        game_name_safe = make_the_string_ready(request.POST['game_name_input'])
        response = requests.get('https://api.rawg.io/api/games?page_size=5&search={}'.format(game_name_safe))
        data = response.json()
        temp_list = []
        game_informations = []

        for i in range (0, len (data['results'])):
            if 'slug' in (data['results'][i]):
                temp_list.append(data['results'][i]['slug'])
                temp_list.append(data['results'][i]['name'])
                temp_list.append(data['results'][i]['background_image'])
            game_informations.append(temp_list)
            temp_list = []

        return render(request, 'api.html', {'game_name' : game_informations})

    elif 'game-slug' in request.GET:
        game_slug = request.GET['game-slug']
        response = requests.get('https://api.rawg.io/api/games/{}'.format(game_slug))
        data = response.json()
        platforms = []
        genres = []
        developers = []
        publishers = []

        for i in range (0, len (data['metacritic_platforms'])):
            platforms.append(data['metacritic_platforms'][i]['platform']['slug'])

        for i in range (0, len (data['genres'])):
            genres.append(data['genres'][i]['slug'])

        for i in range (0, len (data['developers'])):
            developers.append(data['developers'][i]['slug'])

        for i in range (0, len (data['publishers'])):
            publishers.append(data['publishers'][i]['slug'])

        context = {
            'game_name' : data['name'],
            'platforms' : platforms,
            'released' : data['released'],
            'genres' : genres,
            'esrb_rating' : data['esrb_rating']['slug'],
            'developers' : developers,
            'publishers' : publishers,
        }

        return render(request, 'api.html', context)
    return render(request, 'api.html')
################################################################################
def add_new_game_view(request):
    if request.method == "POST":
        website_link = request.POST.get('web_link', None)

        #requests
        url = website_link #url
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0'}#headers
        source=requests.get(url, headers=headers).text # url source

        #beautifulsoup
        soup = BeautifulSoup(source, 'html.parser')
        h1_val = soup.h1.string #h1 value
        temp_list = []
        game_informations = []

        for div in soup.find_all(class_='game__meta-block'):
            for childdiv in div.find_all('div', attrs={'class': 'game__meta-text'}):
                temp_list.append(childdiv.get_text())
            game_informations.append(temp_list)
            temp_list = []


        context = {
            'game_informations' : game_informations,
            'game_name' : ''.join(soup.h1.string),
            'platforms' : ''.join(game_informations[0]),
            'genre' : ''.join(game_informations[2]),
            'release_date' : ''.join(game_informations[3]),
            'developer' : ''.join(game_informations[4]),
            'publisher' : ''.join(game_informations[5]),
        }

        return render(request, 'django-bs.html', context)

    return render(request, 'django-bs.html')
