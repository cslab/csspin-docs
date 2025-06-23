.. -*- coding: utf-8 -*-
   Copyright (C) 2024 CONTACT Software GmbH
   https://www.contact-software.com/

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

.. _spin_docs.sphinx:

==================
csspin_docs.sphinx
==================

The ``csspin_docs.sphinx`` plugin provides a way to run the `sphinx
<https://www.sphinx-doc.org/en/master/>`_ tool in the context of `csspin`_ for
example to build a sphinx-based documentation.

It provides the ``docs``-task that does not support building the documentation
for CONTACT Elements based projects and is currently only used for building the
documentation of pure python packages.

How to setup the ``csspin_docs.sphinx`` plugin?
###############################################

For using the ``csspin_docs.sphinx`` plugin, a project's ``spinfile.yaml`` must
at least contain the following configuration.

.. code-block:: yaml
    :caption: Minimal configuration of ``spinfile.yaml`` to leverage ``csspin_docs.sphinx``

    plugin_packages:
        - csspin-docs
        - csspin-python
    plugins:
        - csspin_docs.sphinx # provides the "docs"-task
    python:
        version: "3.11.9"

The provisioning of the required virtual environment as well as the plugins
dependencies can be done via the well-known ``spin provision``-command.

How to build documentation using ``csspin_docs.sphinx``?
########################################################

The plugin requires the documentation source files already to be present on the
host. Assuming the documentation source files are located below ``docs``, the
documentation can be built after provisioning:

.. code-block:: console
   :caption: Building the documentation using ``csspin_docs.sphinx``

   spin -p sphinx.build_dir=doc/ doc html

``csspin_docs.sphinx`` schema reference
#######################################

.. include:: sphinx_schemaref.rst
