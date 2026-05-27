import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
project = 'wpipe-steps'
copyright = '2023, William Steve Rodriguez Villamizar'
author = 'William Steve Rodriguez Villamizar'
version = '0.105.0'
release = '0.105.0'
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx_rtd_theme',
]
templates_path = ['_templates']
exclude_patterns = []
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
