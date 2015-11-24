# -*- coding: utf-8 -*-


def test_drop_duplicated(testdir):
    testdir.makepyfile("""
        def test_foo():
            pass
    """)
    result = testdir.runpytest('.', '.')
    result.stdout.fnmatch_lines([
        '*== 1 passed in * seconds ==*',
    ])
    assert result.ret == 0

