# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0

#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import docutils
import os
import re
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Google maintained open source PDK'
copyright = '2022, Google LLC'
author = 'Google LLC'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.githubpages',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx_pdk_roles'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# Enable github links when not on readthedocs
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:
    html_context = {
        "display_github": True,              # Integrate GitHub
        "github_user": "google",             # Username
        "github_repo": "open-source-pdks",   # Repo name
        "github_version": "main",            # Version
        "conf_py_path": "/docs/",
    }
else:
    docs_dir = os.path.abspath(os.path.dirname(__file__))
    print("Docs dir is:", docs_dir)
    import subprocess
    subprocess.call('git fetch origin --unshallow', cwd=docs_dir, shell=True)
    subprocess.check_call('git fetch origin --tags', cwd=docs_dir, shell=True)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = re.sub('^v', '', os.popen('git describe ').read().strip())
# The short X.Y version.
version = release

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    '_build',
    'env',
    'venv',
    'Thumbs.db',
    '.DS_Store',
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None

# -- Options for HTML output -------------------------------------------------

# Prefix each section label with the name of the document it is in, followed by
# a colon. For example, index:Introduction for a section called Introduction
# that appears in document index.rst. Useful for avoiding ambiguity when the
# same section heading appears in different documents.
#autosectionlabel_prefix_document = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_symbiflow_theme"

html_logo = "_static/open-source-pdks-logo-top.png"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# https://sphinx-symbiflow-theme.readthedocs.io/en/latest/customization.html
html_theme_options = {
    'nav_title': 'Google maintained open source PDKs',

    'color_primary': 'indigo',
    'color_accent': 'blue',

    # Set the repo location to get a badge with stats
    'github_url': 'https://github.com/google/open-source-pdks',
    'repo_name': 'open-source-pdks',
    'repo_type': 'github',

    'globaltoc_depth': 0,
    'globaltoc_collapse': True,

    # Hide the symbiflow links
    'hide_symbiflow_links': True,
    'license_url' : 'https://www.apache.org/licenses/LICENSE-2.0',
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('open-source-pdks', 'Google maintained open source PDKs Documentation',
     [author], 1)
]
