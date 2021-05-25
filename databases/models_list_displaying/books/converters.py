from datetime import datetime, date


class PubDateConverter:
    regex = '[0-9]{4}-[0-9]{2}-[0-9]{2}'

    @staticmethod
    def to_python(value: str) -> date:
        return datetime.strptime(value, "%Y-%m-%d").date()

    @staticmethod
    def to_url(date: date) -> str:
        return date.strftime("%Y-%m-%d")
