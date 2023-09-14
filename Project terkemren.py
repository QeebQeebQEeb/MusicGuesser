import random

def main():
    """Start a music genre guessing game."""
    print("Guess the genre!")
    print('you have to guess 3 genres, use them well!')
    
    music_genres = [
        'Pop music',
        'Hip hop',
        'Jazz',
        'rock',
        'Kpop',
        'Jpop',
        'Phonk',
        'Country music',
        'Instrumental'
        ]
    count = 0
    score = 0
    x = random.choice(music_genres)
    guess = None
    while x != guess and count < 5:
        guess = str(input("1) What genre do you think it is?"))
        if x == guess:
           print("Woah, good one. You are correct!")
           score += 1
           print('score:',(score))
           break
        elif x != guess:
             count+= 1
             print('Wrong!')
        if count == 5:
             print('you failed')
        
        if x == ('Jazz'):
           print('Clue: a type of music characterized by improvisation')
        if x == ('Pop music'):
           print('Clue: it has catchy rhythms that make us want to sing along and dance.')
        if x == ('Hip hop'):
           print('Clue: a style of popular featuring rap with an electronic backing.')
        if x == ('rock'):
           print('Clue: a form of music with a strong beat')
        if x == ('Kpop'):
           print('Clue: popular genre of music originating from South Korea.')
        if x == ('Jpop'):
           print('Clue: one of the most popular music genres in Japan')
        if x == ('Phonk'):
           print('Clue: a type of hip-hop and trap music.')
        if x == ('Country music'):
           print('Clue: mixture of ballads and dance tunes')
        if x == ('Instrumental'):
           print('Clue: involves just instruments')
    x = random.choice(music_genres)
    guess = None
    while x != guess and count < 5:
        guess = str(input("2) What genre do you think it is?"))
        if x == guess:
           print("Woah, good one. You are correct!")
           score += 1
           print('score:',(score))
           break
        elif x != guess:
             count+= 1
             print('Wrong!')
        if count == 5:
             print('you failed')
        
        if x == ('Jazz'):
           print('Clue: a type of music characterized by improvisation')
        if x == ('Pop music'):
           print('Clue: it has catchy rhythms that make us want to sing along and dance.')
        if x == ('Hip hop'):
           print('Clue: a style of popular featuring rap with an electronic backing.')
        if x == ('rock'):
           print('Clue: a form of music with a strong beat')
        if x == ('Kpop'):
           print('Clue: popular genre of music originating from South Korea.')
        if x == ('Jpop'):
           print('Clue: one of the most popular music genres in Japan')
        if x == ('Phonk'):
           print('Clue: a type of hip-hop and trap music.')
        if x == ('Country music'):
           print('Clue: mixture of ballads and dance tunes')
        if x == ('Instrumental'):
           print('Clue: involves just instruments')
    x = random.choice(music_genres)
    guess = None
    while x != guess and count < 5:
        guess = str(input("3) What genre do you think it is?"))
        if x == guess:
           print("Woah, good one. You are correct!")
           score += 1
           print('score:',(score))
           break
        elif x != guess:
             count+= 1
             print('Wrong!')
        if count == 5:
             print('you failed')

        if x == ('Jazz'):
           print('Clue: a type of music characterized by improvisation')
        if x == ('Pop music'):
           print('Clue: it has catchy rhythms that make us want to sing along and dance.')
        if x == ('Hip hop'):
           print('Clue: a style of popular featuring rap with an electronic backing.')
        if x == ('rock'):
           print('Clue: a form of music with a strong beat')
        if x == ('Kpop'):
           print('Clue: popular genre of music originating from South Korea.')
        if x == ('Jpop'):
           print('Clue: one of the most popular music genres in Japan')
        if x == ('Phonk'):
           print('Clue: a type of hip-hop and trap music.')
        if x == ('Country music'):
           print('Clue: mixture of ballads and dance tunes')
        if x == ('Instrumental'):
           print('Clue: involves just instruments')
main()