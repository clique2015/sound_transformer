FROM python:3.12-slim

RUN apt-get update && apt-get install -y git ffmpeg libsndfile1 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

# Install GitHub package separately if needed
RUN pip install --default-timeout=300 git+https://github.com/facebookresearch/encodec.git
RUN pip install --default-timeout=300 --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7860

CMD ["python", "app.py"]

