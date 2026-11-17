from __future__ import annotations
from enum import Enum


class Event(str, Enum):
    """Eventos que el modelo y el controlador notifican a sus observadores."""

    MESSAGES_UPDATED = "messages_updated"
    CONFIG_CHANGED = "config_changed"
    GENERATING_START = "generating_start"
    GENERATING_DONE = "generating_done"
    GENERATING_ERROR = "generating_error"
    EXPORT_DONE = "export_done"
