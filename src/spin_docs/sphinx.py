# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2021 CONTACT Software GmbH
# All rights reserved.
# https://www.contact-software.com/

"""Module implementing the sphinx plugin for cs.spin"""

from spin import config, rmtree, setenv, sh, task

defaults = config(
    docs="{spin.project_root}/doc",
    opts="-qaE",
    build_dir="{sphinx.docs}/_build",
    requires=config(
        spin=["spin_python.python"],
        python=["sphinx"],
    ),
)


def cleanup(cfg):  # pylint: disable=unused-argument
    """Clear sphinx's build directory"""
    rmtree("{sphinx.build_dir}")


@task()
def docs(cfg, args):
    """Build the documentation using sphinx"""
    setenv(LATEXMKOPTS="-silent")
    sh(
        "sphinx-build",
        "-M",
        *args,
        cfg.sphinx.docs,
        cfg.sphinx.build_dir,
        cfg.sphinx.opts,
    )
