FROM python:3

WORKDIR /app

RUN pip install openai

COPY . .

CMD ["python", "app/chatbot.py"]