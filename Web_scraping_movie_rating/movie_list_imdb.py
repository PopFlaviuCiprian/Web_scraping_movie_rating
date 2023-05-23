import requests
from bs4 import BeautifulSoup

def get_movies(max_number_of_pages):

    page =1
    while page <= max_number_of_pages:
        url = "https://www.cinemagia.ro/filme/?pn=" + str(page)
        source_code = requests.get(url)
        soup = BeautifulSoup(source_code.content)
        movies_title_div = soup.find_all('div',{'class' : 'title'})
        movies = [movie.text.strip('\n')[0:movie.text.strip('\n').find('\n')] for movie in movies_title_div]
        movies.remove(movies[-1])
        rating_div = soup.find_all('div', {'class' : 'rating'})
        rating_imdb = [float(rating.text.strip('\n')[rating.text.strip('\n').find(' ') +1:]) for rating in rating_div ]
        print('The lenght of movie list  {}, the lenght of the rating list {}'.format(str(len(movies)), str(len(rating_imdb))))
        with open('MovieRating.txt', 'a', encoding='utf-8') as f:
            for i in range(len(movies)):
                if rating_imdb[i] >=8:
                    f.write(movies[i] + ':' + str(rating_imdb[i]) + '\n')
                    print(('Movie: {}\n IMDM rating {}' .format(movies[i], str(rating_imdb[i]))))
        page += 1

if __name__ == '__main__':
    get_movies(15)