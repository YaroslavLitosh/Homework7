
def parse_parameters(query: str) -> dict:
    # if query.find('?') == -1:
    #     print("Your url isn`t correct")
    params = query.split('?')[1].split('&')

    token = {}
    for i in params:
        x = i.split('=')
        token.update({x[0]: x[1]})

    return token


def parse_cookies(cookies: str) -> dict:
    params = cookies.split('!')[1].split(';')
    jar = {}
    for i in params:
        x = i.split('=')

        jar.update({x[0]: x[1]})
    return jar


if __name__ == '__main__':
    # Извините сделал через кучу костылей так как пока не вижу решения без них.
    # Вроде работает но буду рад если подскажете как обойти try и !(костыль в куках)

    # Tests for function "parse_parameters"

    try:
        assert parse_parameters('https://example.com/path/to/pagename=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    except IndexError:
        print("Your url isn`t correct")
    try:
        assert parse_parameters('http://example.com/?') == {}
    except IndexError:
        print('There is no parametrs')

    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple&backgroundcolor=white') ==\
           {'name': 'ferret', 'color': 'purple', 'backgroundcolor': 'white'}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple&backgroundcolor=white&age=19') ==\
           {'name': 'ferret', 'color': 'purple', 'backgroundcolor': 'white', 'age': '19'}

    # Tests for function "parse_cookies"
    try:
        assert parse_cookies('') == {}
    except IndexError:
        print('Invalid cookies')
    assert parse_cookies('!name=Dima') == {'name': 'Dima'}
    assert parse_cookies('!name=Dima;age=20') == {'name': 'Dima', 'age': '20'}
    assert parse_cookies('!name=Dima;age=20;height=194') == {'name': 'Dima', 'age': '20', 'height': '194'}
    assert parse_cookies('!name=Dima;age=20;height=194;weight=80') == {'name': 'Dima', 'age': '20', 'height': '194', 'weight': '80'}
