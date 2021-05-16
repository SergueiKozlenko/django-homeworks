from datetime import datetime, date


class DataConverter:
    regex = '[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}'

    @staticmethod
    def to_python(date: str) -> date:
        return datetime.strptime(date, "%Y-%m-%d").date()

    @staticmethod
    def to_url(date: date) -> str:
        return date.strftime("%Y-%m-%d")
