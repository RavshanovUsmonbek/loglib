import time
import socket
from tools import log
from tools.context import Context
import os
import yaml  # pylint: disable=E0401

from loglib.main_enabler import enable_loggings


def read_settings(path):
    """Unseed settings data from seed"""
    with open(path, "rb") as file:
        settings_data = file.read()
    settings = yaml.load(os.path.expandvars(settings_data), Loader=yaml.SafeLoader)
    return settings


def main():  # pylint: disable=R0912,R0914,R0915
    """Entry point"""
    # Enable logging and say hello
    log.enable_logging()
    log.info("Starting plugin-based Carrier core")
    # Make context holder
    context = Context()
    # Load settings from seed
    log.info("Loading and parsing settings")
    path = "pylon.yml"
    context.settings = read_settings(path)
    #
    context.node_name = context.settings.get("server", dict()).get(
        "name", socket.gethostname()
    )
    #
    enable_loggings(context)
    log.info("Creating Flask application")
    log.info("Creating SocketIO instance")
    log.info("Exiting")


if __name__ == "__main__":
    # Call entry point
    main()
    while True:
        log.info("HELLO")
        time.sleep(1)
