<h1 align="center">Telegram Бот Кликер</h1>

## Начало работы :mag_right:

### Подробное руководство по установке и настройке телеграм-бота кликера :wrench:

<h4>Установка Docker:</h4>

- Перейдите на официальный сайт Docker: <a href="https://www.docker.com/">Docker Download</a>
- Скачайте и установите Docker для вашей операционной системы (Windows, macOS, Linux)
- Следуйте инструкциям на сайте для завершения установки.

<h4>Установка Docker Compose:</h4>

- Docker Compose обычно входит в состав Docker Desktop для Windows и macOS.
- Для Linux следуйте официальной инструкции: <a href="https://docs.docker.com/desktop/install/linux-install/">Install Docker Compose</a>

<h4>Первый запуск проекта (build)</h4>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://readme-typing-svg.herokuapp.com?font=Comic+Sans&duration=4000&pause=100&color=FFFFFF&background=000000&random=false&width=435&lines=cd+Telegram-Bot-Clicker;docker+compose+up+--build">
    <!-- Светлая тема -->
    <img alt="Typing SVG" src="https://readme-typing-svg.herokuapp.com?font=Comic+Sans&duration=4400&pause=1000&color=000000&background=FFFFFF&random=false&width=460&lines=cd+Telegram-Bot-Clicker;docker+compose+up+%E2%80%94build">
</picture>
<h4>Дополнительно:</h4>

- Запуск всех сервисов: 
```
docker-compose up
```

- Запуск сервисов в фоновом режиме: 
```
docker-compose up -d
```
- Завершение работы бота
```
docker-compose down
```

## Функционал :star:
- Игроки могут кликать на монетку и получать за это внутриигровую валюту 💸
- Когда игрок накопит достаточно монет, он может покупать карточки 🎴
- Карточки дают пассивный доход 📈
- Можно покупать бусты для увеличения лимита энергии и количества монет, выдаваемых за клик ⚡
- 6 раз в день разрешают бесплатно восполнить энергию (активировать можно только раз в час) 🔋
- Игроки могут приходить в игру по реферальным ссылкам от друзей или просто людей в интернете, чтобы получить приветственные бонусы 🤝

## Поддержка :pencil:
> [!NOTE]
> Если у вас возникли проблемы или вопросы, пожалуйста, создайте новый вопрос в разделе "Issues" этого репозитория.

## Технологии 📚

Создано с помощью:
- Python 🐍
- aiogram 🤖
- Docker 🐋
