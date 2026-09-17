from .sol01 import parse_line


def stream_parse(lines):
    for line in lines:
        entry = parse_line(line)
        if entry is not None:
            yield entry
