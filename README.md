Программа для парсинга плейлиста из Яндекс.Музыки и добавления в любимые треки в Spotify.

##### Как использовать:
1. Склонировать репозиторий
2. `python -m venv venv`
3. `.\venv\Scripts\activate`
4. `pip install -r requirements.txt`
5. Положить chromedriver.exe совместимый с текущей версией Chrome в системе в папку с проектом. Скачать актуальный chromedriver можно тут - https://chromedriver.chromium.org/
6. python yandex_parser.py _url_to_parse_
7. python spotify_liker.py _login_ _password_

##### CMD args:

`python yandex_parser.py -h `

positional arguments:

  url ------------------ Ya.Music url to parse

optional arguments:

  -h, --help ------------------ show this help message and exit
  
  -p PATH, --path ------------------ PATH  Path to chromedriver.exe
  
`python spotify_liker.py -h`

positional arguments:

  login ------------------ login
  
  password ------------------ password

optional arguments:

  -h, --help ------------------ show this help message and exit
  
  -p PATH, --path PATH ------------------ Path to chromedriver.exe
  
  -f FILE, --file FILE ------------------ Path to result.txt
  
##### Описание:

**yandex_parser.py**

Переходит на страницу плейлиста (ВНИМАНИЕ! Плейлист должен быть открытым), пытается закрыть баннер с рекламой. 
Если в течение 5 секунда баннер не закроется, закройте самостоятельно. Далее плейлист парсится и скроллится вниз. 
Результат записывается в result.txt

**spotify_liker.py**

Логинится с переданными логином и паролем, переходит на страницу поиска, ищет треки из results.txt и лайкает их. Каждый
10 трек ждёт 10 секунд для имитации действий реального пользователя. Если трек уже лайкнут, то ничего не произойдёт.
Уже лайкнутые треки пишутся в консоль и в already_liked.txt, треки, которые Spotify не смог найти пишутся в консоль и в 
cant like.txt