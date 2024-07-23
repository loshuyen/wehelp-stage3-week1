
FROM python:3.12.4

WORKDIR /stage_3_week_1

COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["fastapi", "run", "app.py"]