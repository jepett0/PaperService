FROM python:3.9

COPY db backend/db
COPY create_database.py backend/create_database.py
COPY drop_database.py backend/drop_database.py
COPY fill_database.py backend/fill_database.py
COPY main.py backend/main.py
COPY bot.py backend/bot.py 
COPY entrypoint.sh entrypoint.sh
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000

WORKDIR /backend
