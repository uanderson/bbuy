import logging.config
import os


def config_logging():
    logging_conf_file: str = os.environ.get("LOGGING_CONF_FILE")
    logging.config.fileConfig(logging_conf_file)

    logging.info(f"Logging config file '{logging_conf_file}' loaded")


if __name__ == "__main__":
    config_logging()
