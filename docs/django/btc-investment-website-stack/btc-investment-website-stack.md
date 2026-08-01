# BTC Investment Website Stack

## Updated requirements

Build a BTC investment website using **Django templates** for the frontend.

Users can:

```txt
Sign up
Confirm email via activation link
Log in / log out
Change password
Edit profile
View investment dashboard
Generate BTC deposit address from xpub/public master key
Send BTC to generated address
See pending/detected/confirmed deposits
Have deposits confirmed after 6 confirmations
```

The app must **not** send BTC or store private keys.

## Updated tech stack

```txt
Django 5.2 LTS
Django templates
uv
Gunicorn
Docker Compose
PostgreSQL 16
Redis 7
Celery worker
Celery beat
Electrum daemon JSON-RPC
Electrum listener service
Nginx
Prometheus
Grafana
node-exporter
Real SMTP
Whitenoise
Ruff / pytest
```

## Base project

Use the GitHub ZIP project as the new base, but adapt it to our stack.

Keep from base:

```txt
uv
Docker structure
Gunicorn
Celery
PostgreSQL
Redis
Static files setup
Non-root user
Health checks
```

Change/add:

```txt
Django 5.2 LTS
Django templates frontend
accounts app
wallets app
investments app
Electrum daemon
Electrum listener
BTC deposit monitoring
Nginx reverse proxy
Prometheus/Grafana/node-exporter
Real SMTP
```

## BTC architecture

```txt
Django app
  ↓
Electrum daemon JSON-RPC
  ↓
Public Electrum servers
```

Event/fallback flow:

```txt
Electrum listener service
  ↓
Celery task
  ↓
Check deposit transaction
  ↓
Confirm after 6 confirmations
```

Fallback:

```txt
Celery beat scans pending deposits every 10 minutes
```

## Security rules

```txt
Never store seed phrase
Never store private keys
Use xpub/public master key only
No withdrawals
SMTP password via env only
Production secrets via env/secrets manager
```
Those old containers are still running from the previous project (`btc-investment-django-*`), so images are “still in use.”

Do a FULL cleanup:

## 1. Stop and remove ALL containers

```bash id="xj2iqn"
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
```

## 2. Remove all images

```bash id="yb1o4q"
docker rmi -f $(docker images -aq)
```

## 3. Remove all volumes

```bash id="z2jzzq"
docker volume rm $(docker volume ls -q)
```

## 4. Remove all networks

```bash id="77rv0o"
docker network prune -f
```

## 5. Nuclear cleanup

```bash id="d0f84v"
docker system prune -a --volumes -f
```

## 6. Verify clean state

```bash id="p1s2su"
docker ps -a
docker images
docker volume ls
```

All should be nearly empty.

Then rebuild fresh:

```bash id="rxmjlwm"
docker compose build --no-cache
docker compose up
```
