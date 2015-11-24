# -*- coding: utf-8 -*-


def test_drop_duplicated(testdir):
    """Make sure that pytest accepts our fixture."""
    testdir.makepyfile("""
        def test_foo():
            pass
    """)
    result = testdir.runpytest('.', '.')
    result.stdout.fnmatch_lines([
        '*== 1 passed, 1 deselected in * seconds ==*',
    ])
    assert result.ret == 0

