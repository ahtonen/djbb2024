import logging
from datetime import datetime

import pytz

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

colors = {
    "Finland flag blue": "#002F6C",
    "Jamaica flag green": "#009B3A",
    "Jamaica flag yellow": "#FED100",
    "scorchio": "#FFCF00",
}


class ISO8601Formatter(logging.Formatter):
    """Custom formatter for logging in ISO8601 format"""

    def formatTime(self, record, datefmt=None):
        return (
            datetime.fromtimestamp(record.created).astimezone(pytz.utc)
            # .astimezone(pytz.timezone("Europe/Helsinki"))
            .isoformat(timespec="milliseconds")
        )
