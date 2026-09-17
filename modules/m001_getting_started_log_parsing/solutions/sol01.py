from ..exercises.ex01_parse_line import Entry


def parse_line(line: str) -> Entry | None:
    parts = line.rstrip("\r\n").split(" ", 3)
    if len(parts) != 4 or any(p == "" for p in parts[:3]):
        return None
    return Entry(*parts)
