import logging.config

from os import environ


def config_logging():
    logging_conf_file: str = environ.get("LOGGING_CONF_FILE", "logging.conf")
    logging.config.fileConfig(logging_conf_file)

    logging.info(f"Logging config file '{logging_conf_file}' loaded")


if __name__ == "__main__":
    config_logging()
