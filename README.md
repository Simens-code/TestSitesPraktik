# 🚚 Автотесты для cargo-test.mwire.ru

Проект с автоматическими браузерными тестами для cargo-test.mwire.ru  
Тесты написаны для мобильной версии (iPhone 12/13) с использованием Selenium и pytest.

---

 Быстрый старт

1. Установите Python 3.9 или новее

Скачайте с официального сайта: https://www.python.org/downloads/

При установке обязательно поставьте галочку:
-  `Add Python to PATH`

Проверьте установку в терминале:
```bash
python --version

2. Скачайте Яндекс Браузер
Если у вас его нет: https://browser.yandex.ru/

3. Клонируйте репозиторий

git clone https://github.com/Simens-code/TestSitesPraktik.git
cd TestSitesPraktik

4. Скачайте YandexDriver
Ссылка для скачивания:
👉 https://github.com/yandex/YandexDriver/releases

Что нужно сделать:

Найдите последнюю версию (например, 26.3.1-stable)

В разделе Assets скачайте файл для Windows:
yandexdriver-версия-win32.zip

Распакуйте архив

Переименуйте файл yandexdriver → yandexdriver.exe

В папке проекта создайте папку drivers и положите туда yandexdriver.exe
mkdir drivers

5. Создайте виртуальное окружение

python -m venv venv

Активация:

Windows:
venv\Scripts\activate


Mac / Linux:
source venv/bin/activate
После активации в начале строки терминала появится (venv).

6. Установите библиотеки

pip install -r requirements.txt
Если файла requirements.txt нет, создайте его:


echo selenium==4.15.0 > requirements.txt
echo pytest==7.4.3 >> requirements.txt
echo webdriver-manager==4.0.1 >> requirements.txt
echo pytest-html==4.1.1 >> requirements.txt
echo python-dotenv==1.0.0 >> requirements.txt
И установите:


pip install -r requirements.txt

7. Настройте переменные окружения
Создайте файл .env:


echo BASE_URL=https://cargo-test.mwire.ru > .env
echo DEFAULT_TIMEOUT=10 >> .env
echo MOBILE_EMULATION=true >> .env
echo YANDEX_BROWSER_PATH=C:\Users\%USERNAME%\AppData\Local\Yandex\YandexBrowser\Application\browser.exe >> .env

8. Запустите тест

python -m pytest tests/test_reset_db.py -v -s

Данные для авторизации
Если тест требует авторизации, добавьте в файл .env:

echo TEST_PHONE=9008001234 >> .env
echo TEST_PASSWORD=uxENeov5GuvzkhxH >> .env