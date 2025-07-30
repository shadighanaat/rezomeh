# Use the official Python 3.12 image as the base
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND=noninteractive

# Set the working directory
WORKDIR /code

# Install system dependencies (including pkg-config)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    pkg-config \
    default-libmysqlclient-dev \
    libmariadb-dev \
    libpq-dev \
    libglib2.0-0 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    libffi-dev \
    libcairo2 \
    tzdata \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt /code/

RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /code/

# Copy .env file (optional; usually done via volumes or `.dockerignore`)
COPY .env /code/

# Collect static files
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "rezome.wsgi:application", "--bind", "0.0.0.0:8000", "--static-dir", "/usr/src/app/staticfiles"]
