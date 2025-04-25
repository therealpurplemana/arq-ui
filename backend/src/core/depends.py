from arq.connections import RedisSettings
from core.cache import LRUCache
from core.config import Settings, get_app_settings

settings: Settings = get_app_settings()
cache_singleton = LRUCache(capacity=settings.max_jobs)


def get_lru_cache() -> LRUCache:
    """Get LRU cache."""
    return cache_singleton


def get_redis_settings() -> RedisSettings:
    """Get Redis settings."""
    if settings.redis_url:
        # If redis_url is provided, use it directly (supports both redis:// and rediss:// protocols)
        return RedisSettings.from_dsn(settings.redis_url)
    
    # Otherwise, use individual connection parameters
    return RedisSettings(
        host=settings.redis_host,
        port=settings.redis_port,
        database=settings.redis_db,
        password=settings.redis_password,
        username=settings.redis_username,
        ssl=settings.redis_ssl,
        ssl_cert_reqs=settings.redis_ssl_cert_reqs,
    )
