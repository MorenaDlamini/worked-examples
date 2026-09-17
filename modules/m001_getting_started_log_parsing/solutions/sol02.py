from ..exercises.ex02_parse_lines import ParseResult
from .sol01 import parse_line


def parse_lines(lines):
    entries, rejected = [], []
    for line in lines:
        entry = parse_line(line)
        (entries if entry is not None else rejected).append(entry if entry is not None else line)
    return ParseResult(entries=entries, rejected=rejected)
