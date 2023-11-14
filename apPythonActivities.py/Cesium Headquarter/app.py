def preference():
    print('What kind of movies do you like')
    movie=(input('Please enter a genre of movie'))
    if movie == 'action':
        print('Watch a superhero, spy movie')
    elif movie == 'Science fiction':
        print('Watch a star wars or star trek movie')
    elif movie == 'Western':
        print('Watch Rango, Old Western')
    elif movie == 'Horror':
        print('Watch scream or Jason, Hallween')
    elif movie == 'Thriller':
        print('Watch Hallween house')
    elif movie == 'Comedy':
        print('Watch Home alone, strays')
    elif movie == 'Romance':
        print('Watch No hard feeling, past lives, before we go')
    elif movie == 'Drama':
        print('Watch Fair play, forgotten love, the burial')
    else:
        print('I do not understand your answer, please put in a genra of movies')
    
preference()

