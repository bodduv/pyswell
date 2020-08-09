# -*- coding: utf-8 -*-

"""
Basic logging infrastructure to provide execution information.
"""


from logging import INFO, LoggerAdapter, getLogger


class Logger(LoggerAdapter):
    """Wrapper around logging with a default logging level.
    """

    def __init__(self, log_level=INFO, formatter=None, extra=None):
        self.wrapped = getLogger(__name__)
        self.wrapped.setLevel(log_level)
        self.extra = extra or {}
        super(Logger, self).__init__(self.wrapped, self.extra)

    def echo(self, message: str, log_level=INFO):
        self.wrapped.log(log_level, message, extra={})


logger = Logger(log_level=INFO)
