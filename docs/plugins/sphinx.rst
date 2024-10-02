.. -*- coding: utf-8 -*-
   Copyright (C) 2024 CONTACT Software GmbH
   All rights reserved.
   https://www.contact-software.com/

.. _spin_docs.sphinx:

================
spin_docs.sphinx
================

The ``spin_sphinx.sphinx`` plugin provides a way to run the `sphinx
<https://www.sphinx-doc.org/en/master/>`_ tool in the context of cs.spin for
example to build a sphinx-based documentation.

It provides the ``docs``-task that does not support building the documentation
for CONTACT Elements based projects and is currently only used for building the
documentation of pure python packages.

The plugin requires `make <https://www.gnu.org/software/make/>`_ to be in PATH
and executable.

How to setup the ``spin_docs.sphinx`` plugin?
#############################################

For using the ``spin_docs.sphinx`` plugin, a project's ``spinfile.yaml`` must
at least contain the following configuration.

.. code-block:: yaml
    :caption: Minimal configuration of ``spinfile.yaml`` to leverage ``spin_python.sphinx``

    plugin-packages:
        - spin_docs
        - spin_python
    plugins:
        - spin_docs.sphinx # provides the "docs"-task
    python:
        version: "3.11.9"

The provisioning of the required virtual environment as well as the plugins
dependencies can be done via the well-known ``spin provision``-command.

How to build documentation using ``spin_docs.sphinx``?
######################################################

The plugin requires the documentation source files already to be present on the
host. Assuming the documentation source files are located below ``docs``, the
documentation can be built after provisioning:

.. code-block:: console
   :caption: Building the documentation using ``spin_python.sphinx``

   spin -p sphinx.build_dir=docs/ docs html

``spin_docs.sphinx`` schema reference
#######################################

.. include:: sphinx_schemaref.rst
