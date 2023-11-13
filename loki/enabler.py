import logging
from loki.handler import CarrierLokiBufferedLogHandler, CarrierLokiLogHandler


def enable_loki_logging(context):
    """Enable logging to Loki"""
    if "logging" not in context.settings and "loki" not in context.settings["logging"]:
        return
    #
    if context.settings.get("logging").get("loki").get("buffering", True):
        LokiLogHandler = CarrierLokiBufferedLogHandler
    else:
        LokiLogHandler = CarrierLokiLogHandler
    #
    handler = LokiLogHandler(context)
    handler.setFormatter(logging.getLogger("").handlers[0].formatter)
    logging.getLogger("").addHandler(handler)
