# Build Stage
FROM python:3.10-slim AS build

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry

COPY pyproject.toml poetry.lock ./

# Install dependencies including uvicorn
RUN poetry install --no-dev

COPY . .

# Production Stage
FROM python:3.10-slim AS production

WORKDIR /app

# Install Poetry in the production stage
RUN pip install --upgrade pip && \
    pip install poetry

# Copy the installed dependencies from the build stage
COPY --from=build /app /app

# Set environment variables for Poetry
ENV VIRTUAL_ENV=/root/.cache/pypoetry/virtualenvs
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Check if Uvicorn is installed correctly
RUN poetry install --only main

# Verify that Uvicorn is available in the PATH
RUN find /root/.cache/pypoetry/virtualenvs/ -name "uvicorn" -type f -executable


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT:-8080}"]
