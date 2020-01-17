# -*- coding: utf-8 -*-


def test_drop_duplicated_dir(testdir):
    testdir.makepyfile("""
        def test_foo():
            pass
    """)
    result = testdir.runpytest('.', '.')
    result.stdout.fnmatch_lines([
        '* 1 passed in *',
    ])
    assert result.ret == 0


def test_drop_duplicated_pkg(testdir):
    testdir.makepyfile(**{
        "pkg/__init__.py": "",
        "pkg/test_foo.py": """
        def test_foo():
            pass
    """})
    result = testdir.runpytest('pkg', 'pkg')
    result.stdout.fnmatch_lines([
        '* 1 passed in *',
    ])
    assert result.ret == 0
