main_url = 'https://www.kinopoisk.ru/'
api_url = 'https://api.kinopoisk.dev/'
cookie_string = 'L=AG1BR2ZRDgd9dkwPYUJ4eQNJXWxEdQdbHS5LCzYzDw==.1737278171.16021.386523.91d4f36cebd7ecb73bda75ac8dea834a; _ym_d=1737278175; _ym_uid=1737277987308414627; i=+mOZMg8//0nyP03JsoV52BFe4cHKzhHCU6PkmAhELqIxJYWs2ac6L+horV6UjyLXO1b3OGwbbSCu6BhjQIMDw+BPt6E=; mda2_beacon=1737278174929; sessar=1.1198.CiB06x8q0bOr4DbUJZLleRxwwoA40dKFeNdwekp2M6TMPg.Tpq5ARzoTq-St82gvj4yf6u8BGXZ6R7moJ3uwBrSikY; sso_status=sso.passport.yandex.ru:synchronized; ya_sess_id=3:1737278174.5.0.1737278171875:f-1Hsg:5faa.1.2:1|6463924.0.2.3:1737278171|30:10231796.23462.g62F8YhENqyIk2lFGGfkiowGwNU; yandex_login=Xoziaka; yandexuid=2827376041737278021; ys=udn.cDrQldC60LDRgtC10YDQuNC90LAg0J0u#c_chck.4263342057; cycada=4nE0/7Jchog+jk1R8EscEnRlp/XU0lPGsxhMsim/HjY=; _ym_visorc=b; gdpr=0; yandex_plus_metrika_cookie=true; mda_exp_enabled=1; PHPSESSID=4d6ba9a75ed2d5f55b72a63cad577ae3; _yasc=GE1fXw9CkoMfA26pWTTkwUm5JE+de4X5z1GkxcWzZfb0NDYEWawfOhqPmeogn/EY; mobile=no; my_perpages=%5B%5D; yashr=4571734761737277983; _csrf_csrf_token=O4J3uu62PGzxmeUQTKuxTiR2NtxDKTW4x6dq_zJXYaU; desktop_session_key=0a13b3f3bdd1a62d751c22239b7ea8034b340eb60f93897fae50c8a03484fa30aa7ba33f6deb3dc143e64f974b2f07e93f2e238f5b6d0822ab415218831fc7268d82d40668201d21f5a14ebd8704b6560c4c0cdaa22ea097edf5ca54d29cd2db; desktop_session_key.sig=y0W8YmaSLlFc4XGBty23yv7SDUU'

def parse_cookies(cookie_string):
    cookies = []
    for cookie in cookie_string.split(';'):
        name, value = cookie.strip().split('=', 1)
        cookies.append({'name': name, 'value': value, 'path': '/'})
    return cookies

cookies = parse_cookies(cookie_string)