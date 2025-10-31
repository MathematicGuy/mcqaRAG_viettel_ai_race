#!/usr/bin/env bash
set -e

# Wait for Postgres to be ready
echo "⏳ Waiting for Postgres..."
until pg_isready -h "$POSTGRES_HOST" -p "$POSTGRES_PORT" -U "$POSTGRES_USER" > /dev/null 2>&1; do
  sleep 2
done
echo "✅ Postgres is ready!"

# Initialize Airflow database if not already
airflow db migrate

# Create default admin user if not exists
airflow users create \
  --username "${AIRFLOW_ADMIN_USERNAME:-admin}" \
  --firstname Admin \
  --lastname User \
  --role Admin \
  --email "${AIRFLOW_ADMIN_EMAIL:-admin@example.com}" \
  --password "${AIRFLOW_ADMIN_PASSWORD:-admin}" || true

# Start webserver in background and scheduler in foreground
echo "🚀 Starting Airflow..."
airflow webserver --port 8080 &
exec airflow scheduler