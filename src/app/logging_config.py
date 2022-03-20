from src.app.settings import settings

LOGGING_CONFIG = {
    "version": 1,
    "formatters": {
        "default": {
            "format": (
                "%(levelname)s::%(asctime)s:%(name)s." "%(funcName)s\n%(message)s\n"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "level": settings.log_level,
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "loggers": {
        "": {
            "level": settings.log_level,
            "handlers": ["console"],
        },
    },
}
