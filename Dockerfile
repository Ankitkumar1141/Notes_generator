FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# 🔥 IMPORTANT LINE
RUN pip install -e .

EXPOSE 8501

CMD ["streamlit", "run", "src/ai_notes_generator/main.py", "--server.address=0.0.0.0", "--server.port=8501"]