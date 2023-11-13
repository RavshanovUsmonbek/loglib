from base.handler import LogHandlerBase, LogBufferingHandlerBase
from loki.emitter import CarrierLokiLogEmitter


class CarrierLokiLogHandler(LogHandlerBase):
    """Log handler - send logs to storage"""

    def __init__(self, context):
        super().__init__()
        self.settings = context.settings.get("logging").get("loki")
        #
        default_loki_labels = self.settings.get("labels", dict())
        if self.settings.get("include_node_name", True):
            default_loki_labels["node"] = context.node_name
        #
        self.emitter = CarrierLokiLogEmitter(
            url=self.settings.get("url"),
            user=self.settings.get("user", None),
            password=self.settings.get("password", None),
            token=self.settings.get("token", None),
            default_labels=default_loki_labels,
            verify=self.settings.get("verify", True),
        )


class CarrierLokiBufferedLogHandler(LogBufferingHandlerBase):
    """Log handler - buffer and send logs to storage"""

    def __init__(self, context):
        capacity = (
            context.settings.get("logging").get("loki").get("buffer_capacity", 100)
        )
        self.settings = context.settings.get("logging").get("loki")
        #
        default_loki_labels = self.settings.get("labels", dict())
        if self.settings.get("include_node_name", True):
            default_loki_labels["node"] = context.node_name
        #
        emitter = CarrierLokiLogEmitter(
            url=self.settings.get("url"),
            user=self.settings.get("user", None),
            password=self.settings.get("password", None),
            token=self.settings.get("token", None),
            default_labels=default_loki_labels,
            verify=self.settings.get("verify", True),
        )
        #
        self.__init__(emitter, capacity)
