FROM python:3.13.7-slim
    
WORKDIR /workspace    

COPY app.py .

CMD ["python", "app.py"]