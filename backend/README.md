# arq-ui-backend

## Development

```
pdm install
cd src
uvicorn main:app --reload
```

## Configuration

You can configure Redis connection through environment variables:

### Option 1: Redis URL (recommended for managed Redis instances)
```
REDIS_URL=redis://username:password@host:port/db
# OR for SSL/TLS connections:
REDIS_URL=rediss://username:password@host:port/db
```

### Option 2: Individual Redis parameters
```
REDIS_HOST=redis
REDIS_PASSWORD=your_password
REDIS_USERNAME=your_username
REDIS_PORT=6379
REDIS_SSL=False
REDIS_SSL_CERT_REQS=none
REDIS_DB=0
```

If both REDIS_URL and individual parameters are provided, REDIS_URL takes precedence.