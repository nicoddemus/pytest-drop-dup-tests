_seen_paths = set()


def pytest_configure():
    _seen_paths.clear()


def pytest_ignore_collect(collection_path):
    if collection_path.name == "__init__.py":
        return None
    if collection_path in _seen_paths:
        return True
    else:
        _seen_paths.add(collection_path)
        return None


def pytest_collection_modifyitems(config, items):
    seen_node_ids = set()
    new_items = []
    deselected_items = []
    for item in items:
        if item.nodeid not in seen_node_ids:
            new_items.append(item)
            seen_node_ids.add(item.nodeid)
        else:
            deselected_items.append(item)

    items[:] = new_items
    config.hook.pytest_deselected(items=deselected_items)
