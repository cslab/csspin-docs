# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2021 CONTACT Software GmbH
# All rights reserved.
# https://www.contact-software.com/

"""Module implementing the integration tests for spin_docs"""

from os import getcwd

import pytest
from spin import backtick, cd, cli


@pytest.fixture(autouse=True)
def cfg():
    """Fixture creating the configuration tree"""
    cwd = getcwd()
    cli.load_config_tree("tests/yamls/minimal.yaml")
    cd(cwd)


def execute_spin(tmpdir, what, cmd, path="tests/integration/yamls", props=""):
    """Helper to execute spin calls via spin."""
    output = backtick(
        f"spin -p spin.cache={tmpdir} {props} -C {path} --env {tmpdir} -f"
        f" {what} --cleanup --provision {cmd}"
    )
    output = output.strip()
    return output


@pytest.mark.integration()
def test_sphinx_provision(tmpdir):
    """Provision the sphinx plugin"""
    execute_spin(tmpdir=tmpdir, what="sphinx.yaml", cmd="docs --help")


@pytest.mark.integration()
@pytest.mark.xfail(reason="Latest plugin-package states may fail")
def test_sphinx_latest_provision(tmpdir):
    """Provision the sphinx plugin"""
    execute_spin(tmpdir=tmpdir, what="sphinx-latest.yaml", cmd="docs --help")
