# -*- mode: python; coding: utf-8 -*-
#
# Copyright (C) 2021 CONTACT Software GmbH
# All rights reserved.
# https://www.contact-software.com/

"""Module implementing the sphinx plugin for cs.spin"""

from spin import config, rmtree, sh, task

defaults = config(
    docs="{spin.project_root}/docs",
    opts="-qaE",
    build_dir="{spin.project_root}/docs/_build",
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
    cmd = [
        "make",
        "-C",
        cfg.sphinx.docs,
        f"SPHINXOPTS={cfg.sphinx.opts}",
        f"BUILDDIR={cfg.sphinx.build_dir}",
        "LATEXMKOPTS=-silent",
    ]
    sh(*cmd, *args)
