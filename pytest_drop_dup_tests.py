

_seen = set()


def pytest_ignore_collect(path, config):
    if path.basename == '__init__.py':
        return None
    if path in _seen:
        return True
    else:
        _seen.add(path)
        return None
