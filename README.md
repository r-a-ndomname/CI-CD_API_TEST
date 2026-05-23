# CI/CD Тестирование API

Учебный проект по автоматизации тестирования REST API на **Python + pytest + requests** с автоматическим запуском через GitHub Actions.

## Что внутри

| День | Тема |
|------|------|
| Day 1 | HTTP методы: GET, POST, PUT, DELETE |
| Day 2 | Тело запроса, фикстуры, mock API на json-server |
| Day 3 | Path-параметры и query-параметры |
| Day 4 | Аутентификация: Bearer токен, Basic Auth, Digest Auth, API Key |
| Day 6 | Парсинг и валидация сложных JSON-ответов |
| Day 7 | Парсинг XML, валидация JSON и XML схем |
| Day 8 | Цепочки API-запросов, генерация фейковых данных |
| Day 9 | Data-driven тесты: JSON, CSV, Excel |

## Стек технологий

- **Python 3.12**
- **pytest** — запуск тестов
- **requests** — HTTP клиент
- **json-server** — локальный mock REST API (Node.js)
- **xmltodict** — конвертация XML в dict
- **Faker** — генерация фейковых данных
- **GitHub Actions** — CI пайплайн

## Запуск локально

### Требования

- Python 3.12+
- Node.js 20+

### Установка зависимостей

```bash
pip install -r requirements.txt
npm install -g json-server@1.0.0-beta.3
```

### Запуск mock API сервера

```bash
cd Day2
json-server --watch students.json --port 3000
```

### Запуск тестов (в отдельном терминале)

```bash
pytest --ignore=Day5 -k "not test_open_app and not test_calculation" -v
```

## Необходимые секреты GitHub

Для запуска в GitHub Actions добавь секреты в репозиторий:

**Settings → Secrets and variables → Actions → New repository secret**

| Название секрета | Описание | Где получить |
|------------------|----------|--------------|
| `API_RESUME_TOKEN` | Personal Access Token GitHub | GitHub → Settings → Developer settings → Personal access tokens |
| `SIMPLEBOOKS_TOKEN` | Токен для Simple Books API | Регистрация на [simple-books-api.click](http://simple-books-api.click) |
| `GOREST_TOKEN` | Токен для GoRest API | Вход через GitHub на [gorest.co.in](https://gorest.co.in) |
|`REQRES_API_KEY`| Токен для ReqRes API | Регистрация на [https://reqres.in/] |



## CI пайплайн

Workflow (`.github/workflows/api-tests.yml`) запускается автоматически при каждом `push` и `pull_request`:

1. Поднимает mock API (json-server) на порту 3000
2. Устанавливает Python-зависимости
3. Запускает все тесты (кроме UI и Day5)
4. Показывает результаты во вкладке Actions

## Структура проекта

```
.
├── Day1/       # HTTP методы
├── Day2/       # Фикстуры, тело запроса, mock API данные
├── Day3/       # URL параметры
├── Day4/       # Методы аутентификации
├── Day6/       # Валидация сложного JSON
├── Day7/       # XML и валидация схем
├── Day8/       # Цепочки запросов и фейковые данные
├── Day9/       # Data-driven тесты
├── requirements.txt
└── .github/
    └── workflows/
        └── api-tests.yml
```
