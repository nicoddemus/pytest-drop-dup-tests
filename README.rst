pytest-drop-dup-tests
===================================

.. image:: http://img.shields.io/pypi/v/pytest-drop-dup-tests.svg
   :target: https://pypi.python.org/pypi/pytest-drop-dup-tests

.. |ci| image:: https://github.com/nicoddemus/pytest-drop-dup-tests/workflows/main/badge.svg
  :target: https://github.com/nicoddemus/pytest-drop-dup-tests/actions


A Pytest plugin to drop duplicated tests during collection.

Pytest by default will collect all tests from directories or files given
in the command-line. For example, if you execute::

    py.test tests/unit tests/

Tests from ``tests/unit`` will appear twice, because they will be collected
again when pytest sees the ``tests`` directory in the command-line.

This plugin is intended for the cases where the user wants to run all tests
from ``tests/unit`` first and then the rest of the tests under ``tests``,
without duplicates.

This plugin was born from the discussion taken in `#1187`_.


.. _`#1187`: https://github.com/pytest-dev/pytest/issues/1187

----

This `Pytest`_ plugin was generated with `Cookiecutter`_ along with `@hackebrot`_'s `Cookiecutter-pytest-plugin`_ template.


Requirements
------------

* Python 2.7 or 3.5+
* pytest >= 2.7


Installation
------------

You can install via `pip`_ from `PyPI`_::

    $ pip install pytest-drop-dup-tests


Usage
-----

The plugin is enabled by default, no other action is necessary.

Contributing
------------
Contributions are very welcome. Tests can be run with `tox`_, please ensure
the coverage at least stays the same before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "pytest-drop-dup-tests" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`Cookiecutter`: https://github.com/audreyr/cookiecutter
.. _`@hackebrot`: https://github.com/hackebrot
.. _`MIT`: http://opensource.org/licenses/MIT
.. _`BSD-3`: http://opensource.org/licenses/BSD-3-Clause
.. _`GNU GPL v3.0`: http://www.gnu.org/licenses/gpl-3.0.txt
.. _`cookiecutter-pytest-plugin`: https://github.com/pytest-dev/cookiecutter-pytest-plugin
.. _`file an issue`: https://github.com/nicoddemus/pytest-drop-dup-tests/issues
.. _`pytest`: https://github.com/pytest-dev/pytest
.. _`tox`: https://tox.readthedocs.org/en/latest/
.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`PyPI`: https://pypi.python.org/pypi
