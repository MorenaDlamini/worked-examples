from collections import Counter


def top_sources(entries, n):
    counts = Counter(e.message.split(" ", 1)[0] for e in entries if e.message)
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
