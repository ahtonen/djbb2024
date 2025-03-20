import logging
from datetime import datetime

import pytz
from dateutil import relativedelta

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

colors = {
    "Finland flag blue": "#002F6C",
    "Jamaica flag green": "#009B3A",
    "Jamaica flag yellow": "#FED100",
}


class ISO8601Formatter(logging.Formatter):
    """Custom formatter for logging in ISO8601 format"""

    def formatTime(self, record, datefmt=None):
        return (
            datetime.fromtimestamp(record.created).astimezone(pytz.utc)
            # .astimezone(pytz.timezone("Europe/Helsinki"))
            .isoformat(timespec="milliseconds")
        )


def convert_seconds(n):
    """Convert seconds to hours and minutes"""
    rd = relativedelta.relativedelta(seconds=n)
    return "{}h {:02d}m".format(rd.days * 24 + rd.hours, rd.minutes)
