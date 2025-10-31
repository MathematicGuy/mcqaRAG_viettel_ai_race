# airflow/Dockerfile
FROM apache/airflow:2.10.2-python3.11

USER root

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git \
        libpq-dev \
        poppler-utils \
        tesseract-ocr \
        libreoffice \
        pandoc \
    && rm -rf /var/lib/apt/lists/*

# Install UV package manager
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv /root/.local/bin/uv /usr/local/bin/uv && chmod +x /usr/local/bin/uv

# # Copy dependency files
COPY --chown=airflow:root airflow/requirements.txt /requirements.txt
WORKDIR /opt/airflow

# Chuyển sang airflow user
USER airflow

# # Install Python packages
RUN pip install --no-cache-dir -r /requirements.txt

# Copy DAGs, plugins, etc.
COPY --chown=airflow:airflow airflow/dags /opt/airflow/dags
# COPY --chown=airflow:airflow airflow/plugins /opt/airflow/plugins

# Copy entrypoint
COPY --chown=airflow:root airflow/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENV AIRFLOW_HOME=/opt/airflow
ENTRYPOINT ["/entrypoint.sh"]