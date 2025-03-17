import logging
from datetime import datetime

import pandas as pd
import pytz

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

colors = {'Finland flag blue': '#002F6C'}

class ISO8601Formatter(logging.Formatter):
    """Custom formatter for logging in ISO8601 format"""

    def formatTime(self, record, datefmt=None):
        return (
            datetime.fromtimestamp(record.created).astimezone(pytz.utc)
            # .astimezone(pytz.timezone("Europe/Helsinki"))
            .isoformat(timespec="milliseconds")
        )


def totals_per_sport(df_training):
    """Calculate total moving time per sport type"""
    sport_types = list(df_training.type.unique())
    totals_hr = []

    for s in sport_types:
        totals_hr.append(
            df_training.loc[df_training.type == s].moving_time.sum() / 3600
        )

    return pd.DataFrame(
        data=totals_hr, index=sport_types, columns=["total moving time (h)"]
    )