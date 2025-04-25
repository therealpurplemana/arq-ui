# arq-ui

This is a fork of arq-ui to allow passing REDIS_URL including username. 
![arq UI](./docs/screenshot1.png)

## Features

- Providing statistics on job statuses: total number, number of jobs in queue, jobs being executed, and jobs with errors.
- Visualization of jobs distribution over time in the form of a timeline.
- Displaying a list of jobs with filtering, searching, and sorting capabilities.
- Ability to abort jobs.

## Limitations

- The interface reads data directly from Redis, not storing the state of jobs, which allows tracking tasks only for the last hour. There are plans to add functionality for permanent data storage.
- `arq` uses the `pickle` library for data serialization, which limits the ability to deserialize objects of custom classes that are not accessible. If `arq-ui` cannot deserialize the data, tasks with such data will not be displayed in the monitoring.
- To enable job cancellation, the worker must be configured with the `allow_abort_jobs` parameter.
- Handling a large number of jobs (more than 50,000) may decrease the application's performance.
- The interface does not have built-in security features, therefore it is not recommended to be exposed to the public without additional security measures.


## Demo

[https://demo.arq-ui.florm.io/arq/ui/](https://demo.arq-ui.florm.io/arq/ui/)

## Installation and Launch

### Using Docker

To launch:

```bash
docker pull antonk0/arq-ui
docker run -p 8000:8000 -e REDIS_HOST=redis.host.com -e REDIS_PORT=6379 antonk0/arq-ui
```

docker-compose.yml

```yaml
version: '3'
services:
  arq-ui:
    image: antonk0/arq-ui:latest
    restart: unless-stopped
    environment:
      # Option 1: Use REDIS_URL for managed Redis instances
      - REDIS_URL=redis://username:password@redis.host.com:6379/0
      # OR use rediss:// for SSL/TLS connections:
      # - REDIS_URL=rediss://username:password@redis.host.com:6379/0
      
      # Option 2: Use individual Redis parameters
      # - REDIS_HOST=redis.host.com
      # - REDIS_USERNAME=your_username
      # - REDIS_PASSWORD=your_password
      # - REDIS_PORT=6379
      # - REDIS_SSL=False
      # - REDIS_SSL_CERT_REQS=none
      # - REDIS_DB=0
    ports:
      - 8000:8000
```

### Running from Source

Download the latest stable release from the GitHub releases, unzip it, and execute the following commands:

```bash
pdm install
cd src
pdm run uvicorn main:app --host=0.0.0.0 --port=8000
```

If `pdm` is not installed, you can install it using `pip`:

```bash
pip install pdm
```

## Configuration

The interface is accessible at `/arq/ui/`. Swagger API documentation is available at `/arq/api/docs/`.

Possible environment variables:

| Variable | Description | Default Value |
| -------- | ----------- | ------------- |
| `REDIS_URL` | Complete Redis connection URL (e.g., redis://username:password@host:port/db or rediss://username:password@host:port/db) | `""` |
| `REDIS_HOST` | Address of the Redis server (ignored if REDIS_URL is provided) | `redis` |
| `REDIS_PORT` | Port of the Redis server (ignored if REDIS_URL is provided) | `6379` |
| `REDIS_USERNAME` | Username for connecting to Redis (ignored if REDIS_URL is provided) | `""` |
| `REDIS_PASSWORD` | Password for connecting to Redis (ignored if REDIS_URL is provided) | `""` (no password) |
| `REDIS_SSL` | Whether to use SSL for connecting to Redis (ignored if REDIS_URL is provided) | `False` |
| `REDIS_SSL_CERT_REQS` | SSL certificate requirements (ignored if REDIS_URL is provided) | `none` |
| `REDIS_DB` | Redis database number (ignored if REDIS_URL is provided) | `0` |
| `MAX_JOBS` | Maximum number of tasks that can be displayed in the interface | `50000` |
| `REQUEST_SEMAPHORE_JOBS` | Number of tasks that can be requested simultaneously | `5` |
| `QUEUE_NAME` | Name of the queue in Redis | `arq:queue` |

## Development


```
docker compose -f docker-compose.dev.yml build
docker compose -f docker-compose.dev.yml up
```

### Links

| Name | Link |
| ------ | ------ |
| Frontend | [http://localhost:5173/arq/ui](http://localhost:5173/arq/ui) |
| Backend | [http://localhost:8000/arq/api/docs](http://localhost:8000/arq/api/docs) |
| P3X Redis UI | [http://localhost:7843/](http://localhost:7843/) |