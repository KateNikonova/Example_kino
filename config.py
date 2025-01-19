main_url = 'https://www.kinopoisk.ru/'
api_url = 'https://api.kinopoisk.dev/'
cookie_string = '<добавьте свои cookie>'
def parse_cookies(cookie_string):
    cookies = []
    for cookie in cookie_string.split(';'):
        name, value = cookie.strip().split('=', 1)
        cookies.append({'name': name, 'value': value, 'path': '/'})
    return cookies

cookies = parse_cookies(cookie_string)