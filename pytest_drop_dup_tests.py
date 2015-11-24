

def pytest_collection_modifyitems(items, config):
    seen = set()
    remaining = []
    deselected = []
    for item in items:
        if item.nodeid not in seen:
            seen.add(item.nodeid)
            remaining.append(item)
        else:
            deselected.append(item)

    if deselected:
        config.hook.pytest_deselected(items=deselected)
        items[:] = remaining

