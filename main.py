
def parse_parameters(query: str) -> dict:
    token = {}
    if query.find('?') != -1:
        params = query.split('?')[1].split('&')
        # print(params)
        if params == ['']:
            return {}
        else:
            for i in params:
                x = i.split('=')
                # print(x)
                token.update({x[0]: x[1]})
    # else:
    #     print("Your url isn`t correct")
    return token


def parse_cookies(cookies: str) -> dict:
    jar = {}
    if cookies == (''):
        return {}
    else:
        params = cookies.split(';')
        # print(params)
        for i in params:
            x = i.split('=')
            # print(f'x = {x}')
            jar.update({x[0]: x[1]})
    return jar


if __name__ == '__main__':
    # Извините сделал через кучу костылей так как пока не вижу решения без них.
    # Вроде работает но буду рад если подскажете как обойти try и !(костыль в куках)

    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/') == {}
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret') == {'name': 'ferret'}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret',
                                                                                             'color': 'purple'}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple&backgroundcolor=white&age=19') ==\
           {'name': 'ferret', 'color': 'purple', 'backgroundcolor': 'white', 'age': '19'}

    # # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima') == {'name': 'Dima'}
    assert parse_cookies('name=Dima;age=20') == {'name': 'Dima', 'age': '20'}
    assert parse_cookies('name=Dima;age=20;height=194') == {'name': 'Dima', 'age': '20', 'height': '194'}
    assert parse_cookies('name=Dima;age=20;height=194;weight=80') == {'name': 'Dima', 'age': '20', 'height': '194', 'weight': '80'}
