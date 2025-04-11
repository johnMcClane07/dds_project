# Проект Django: ДДС (Движение Денежных Средств)

Этот проект представляет собой веб-приложение для учета движения денежных средств. Он построен на фреймворке Django и использует стандартные технологии для работы с базой данных и веб-сервисами.
ТЗ:https://drive.google.com/file/d/1vbPk2aiMe52pDFW57zMUDMaW7rqrHypc/view

## Установка и настройка проекта

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/johnMcClane07/dds_project
cd dds_project
```
### 2. Создайте виртуальное окружение

```bash
python -m venv myenv
```

Активируйте виртуальное окружение:

macOS/Linux
```bash
source myenv/bin/activate

```
Windows:

```bash
myenv\Scripts\activate
```

### 3. Установите зависимости
```bash
pip install -r requirements.txt

```


### 4. Настройка базы данных
```bash
python manage.py makemigrations
python manage.py migrate

```

### 5. Запуск веб-сервиса
```bash
python manage.py runserver

```


## Скриншоты 
<img width="1470" alt="Снимок экрана 2025-04-11 в 17 09 41" src="https://github.com/user-attachments/assets/4b3d2775-1177-4ab8-9a2e-a885f9eeb8ee" />
<img width="1470" alt="Снимок экрана 2025-04-11 в 17 10 07" src="https://github.com/user-attachments/assets/fcfd9d44-6503-4574-b7a0-0f91cf06d5a8" />
<img width="1470" alt="Снимок экрана 2025-04-11 в 17 10 27" src="https://github.com/user-attachments/assets/189ac776-4307-4f2c-9a42-02dd3937cf06" />

