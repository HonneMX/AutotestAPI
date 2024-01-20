FROM python:3.9

WORKDIR /tests_project/

# Копируем файлы и устанавливаем зависимости
COPY requirements.txt .
COPY . .

ENV ENV=dev

RUN pip install --no-cache-dir -r requirements.txt

# Установка Allure
RUN apt-get update && apt-get install -y curl default-jre && apt-get clean
RUN curl -o allure-2.13.9.tgz -Ls https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/2.13.9/allure-commandline-2.13.9.tgz && \
    tar -zxvf allure-2.13.9.tgz -C /usr/local && \
    ln -s /usr/local/allure-2.13.9/bin/allure /usr/local/bin/allure

# Команда запуска тестов
CMD pytest --alluredir=/tests_project/test_results && allure serve /tests_project/test_results && sleep infinity