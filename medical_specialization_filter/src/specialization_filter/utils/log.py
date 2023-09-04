import logging.config


def get_config():
    return {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {"format": "%(levelname)s - %(name)s - %(message)s"},
        },
        "handlers": {
            "stdout": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "default",
            }
        },
        "root": {"level": "DEBUG", "handlers": ["stdout"]},
    }


def setup_parser(parser):
    group = parser.add_argument_group("log")
    group.add_argument("--logging-level", help="Logging level")


def setup_logging(level=None):
    config = get_config()

    if level:
        config["handlers"]["stdout"]["level"] = level

    logging.config.dictConfig(config)
