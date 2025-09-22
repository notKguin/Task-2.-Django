from django.shortcuts import render

def index(request):
    # Список фильмов с жанрами и ссылками на картинки
    films = [
        {
            'title': 'Зеленая миля', 
            'genre': 'драма', 
            'year': 1999, 
            'rating': 9.1,
            'image': 'https://m.media-amazon.com/images/M/MV5BMTUxMzQyNjA5MF5BMl5BanBnXkFtZTYwOTU2NTY3._V1_FMjpg_UX1000_.jpg'
        },
        {
            'title': 'Побег из Шоушенка', 
            'genre': 'драма', 
            'year': 1994, 
            'rating': 9.0,
            'image': 'https://m.media-amazon.com/images/M/MV5BNDE3ODcxYzMtY2YzZC00NmNlLWJiNDMtZDViZWM2MzIxZDYwXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_FMjpg_UX1000_.jpg'
        },
        {
            'title': 'Крестный отец', 
            'genre': 'криминал', 
            'year': 1972, 
            'rating': 8.9,
            'image': 'https://m.media-amazon.com/images/M/MV5BM2MyNjYxNmUtYTAwNi00MTYxLWJmNWYtYzZlODY3ZTk3OTFlXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_FMjpg_UX1000_.jpg'
        },
        {
            'title': 'Темный рыцарь', 
            'genre': 'фантастика', 
            'year': 2008, 
            'rating': 8.9,
            'image': 'https://m.media-amazon.com/images/M/MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_FMjpg_UX1000_.jpg'
        },
        {
            'title': 'Форрест Гамп', 
            'genre': 'мелодрама', 
            'year': 1994, 
            'rating': 8.8,
            'image': 'https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_FMjpg_UX1000_.jpg'
        },
        {
            'title': 'Начало', 
            'genre': 'фантастика', 
            'year': 2010, 
            'rating': 8.7,
            'image': 'https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_FMjpg_UX1000_.jpg'
        },
        {
            'title': 'Леон', 
            'genre': 'боевик', 
            'year': 1994, 
            'rating': 8.7,
            'image': 'https://m.media-amazon.com/images/M/MV5BODllNWE0MmEtYjUwZi00ZjY3LThmNmQtZjZlMjI2YTZjYmQ0XkEyXkFqcGdeQXVyNTc1NTQxODI@._V1_FMjpg_UX1000_.jpg'
        },
        {
            'title': 'Django освобожденный', 
            'genre': 'вестерн', 
            'year': 2012, 
            'rating': 8.5,
            'image': 'https://m.media-amazon.com/images/M/MV5BMjIyNTQ5NjQ1OV5BMl5BanBnXkFtZTcwODg1MDU4OA@@._V1_FMjpg_UX1000_.jpg'
        },
        {
            'title': 'Титаник', 
            'genre': 'мелодрама', 
            'year': 1997, 
            'rating': 8.4,
            'image': 'https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_FMjpg_UX1000_.jpg'
        }
    ]
    
    # Получаем выбранный жанр из GET-параметра
    selected_genre = request.GET.get('genre', '')
    
    # Фильтруем фильмы по жанру, если выбран
    if selected_genre:
        filtered_films = [film for film in films if film['genre'] == selected_genre]
    else:
        filtered_films = films
    
    # Получаем уникальные жанры для фильтра
    genres = sorted(set(film['genre'] for film in films))
    
    context = {
        'films': filtered_films,
        'genres': genres,
        'selected_genre': selected_genre,
    }
    
    return render(request, 'cinemapp/index.html', context)