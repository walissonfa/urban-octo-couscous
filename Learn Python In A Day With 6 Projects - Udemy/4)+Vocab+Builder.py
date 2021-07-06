vocabs = {'programming': ['the activity or job of writing computer programs','_______ming'],         
          'python': ['a very large snake that kills animals for food by wrapping itself around them and crushing them', '___hon'],
          'fun': ['pleasure, enjoyment, or entertainment', '__n']}


def test_yourself():
    quit_the_test = False
    points = 0
    incorrect_word_list = []
    for key, value in vocabs.items():
        while True:
            answer = input('\nWhat is {}? \n'
                           ' or [h]int, [p]ass, [q]uit\n: '.format(value[0]))
            if answer == 'h':
                print(value[1])
            elif answer == key:
                points += 1
                print('Correct!')
                break
            elif answer == 'p':
                print('The correct answer is {}'.format(key))
                incorrect_word_list.append(key)
                break
            elif answer == 'q':
                quit_the_test = True
                break
            else:
                print('It\'s not correct')
                
        if quit_the_test:
            break

    print('')
    print('Score {}/{}'.format(points, len(vocabs)))
    print('Incorrect words list:')
    for key in incorrect_word_list:
        values = vocabs[key]
        print('{} ({})\n{}'.format(key, values[1], values[0]))


def list_all_words():
    print('\nYour Vocab List\n')
    for key, value in vocabs.items():
        print('  {} ({})\n   - {}\n'.format(key, value[1], value[0]))


def new_word():
    try:
        word, definition, hint = input('Enter your new word (word|meaning|hint):\n').split('|')
        if word in vocabs:
            print('{} is already in the vocab builder'.format(word))
        else:
            vocabs[word] = [definition, hint]
            print('word {} added.'.format(word))
    except ValueError:
        print('Please make sure the format is correct.')
    except:
        print('Unexpected Error!')


def remove_a_word():
    word = input('Enter a word to remove: ')
    if word in vocabs:
        del(vocabs[word])
        print('{} has been removed.'.format(word))
    else:
        print('Can not find the word {} in your vocab builder'.format(word))


while True:
    cmd = input("""\nWelcome to Vocab Builder!
1) Test yourself!
2) Add a new word
3) remove a word
4) List all words
5) Exit\n""")

    if cmd == '1':
        test_yourself()
    elif cmd == '2':
        new_word()
    elif cmd == '3':
        remove_a_word()
    elif cmd == '4':
        list_all_words()
    elif cmd == '5':
        break

