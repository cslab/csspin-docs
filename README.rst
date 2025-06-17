|Latest Version| |Python| |License|

`csspin-docs` is maintained and published by `CONTACT Software GmbH`_ and
serves plugins for building documentation using the `csspin`_ task runner.

The following plugins are available:

- `csspin_docs.sphinx`: Build sphinx-based documentation

Prerequisites
-------------

`csspin` is available on PyPI and can be installed using pip, pipx or any other
Python package manager, e.g.:

.. code-block:: console

   python -m pip install csspin

Using csspin-docs
-----------------

The `csspin-docs` package and its plugins can be installed by defining those
within the `spinfile.yaml` configuration file of your project.

.. code-block:: yaml

    spin:
      project_name: my_project

    # To develop plugins comfortably, install the packages editable as
    # follows and add the relevant plugins to the list 'plugins' below
    plugin_packages:
      - csspin-docs

    # The list of plugins to be used for this project.
    plugins:
      - csspin_docs.sphinx

    python:
      version: 3.9.8

If the ``spinfile.yaml`` is configured correctly, you can provision the project
using ``spin provision``, that will automatically create a Python virtual
environment and install the required dependencies. After that, you can run
tests using ``spin docs`` and do other great things.

.. _`CONTACT Software GmbH`: https://contact-software.com
.. |Python| image:: https://img.shields.io/pypi/pyversions/csspin-docs.svg?style=flat
    :target: https://pypi.python.org/pypi/csspin-docs/
    :alt: Supported Python Versions
.. |Latest Version| image:: http://img.shields.io/pypi/v/csspin-docs.svg?style=flat
    :target: https://pypi.python.org/pypi/csspin/
    :alt: Latest Package Version
.. |License| image:: http://img.shields.io/pypi/l/csspin-docs.svg?style=flat
    :target: https://www.apache.org/licenses/LICENSE-2.0.txt
    :alt: License
.. _`csspin`: https://pypi.org/project/csspin
