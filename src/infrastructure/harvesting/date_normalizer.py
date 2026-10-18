import re
from datetime import datetime, timezone
import dateparser

class DateNormalizer:
    """Normalizes relative or unstructured date strings into standard UTC datetimes."""

    @staticmethod
    def parse_date(raw_text_snippet: str) -> tuple[datetime, str]:
        """
        Scans for relative date strings (e.g., '2 hours ago', '1 day ago', 'yesterday')
        and converts to standard UTC datetime.
        """
        now = datetime.now(timezone.utc)

        # Common relative time patterns found in search snippets
        pattern = r'(\d+\s+(?:minute|hour|day|week|month)s?\s+ago|yesterday|just now)'
        match = re.search(pattern, raw_text_snippet, re.IGNORECASE)

        if match:
            time_str = match.group(1).strip()
            parsed_dt = dateparser.parse(
                time_str,
                settings={'TIMEZONE': 'UTC', 'RETURN_AS_TIMEZONE_AWARE': True}
            )
            if parsed_dt:
                return parsed_dt, time_str

        # Fallback to current UTC if no explicit date pattern is detected
        return now, "Recent"
