import os
import sys
from pathlib import Path


base_folder = Path(os.path.abspath(__file__)).parent.parent.parent.absolute()
src_folder = os.path.join(base_folder, 'src')
sys.path.insert(0,src_folder)
extensions = [
    'sphinx.ext.autodoc',
]

# Add any other necessary configurations

# -- Project information -----------------------------------------------------

project = 'Read The Docs Test'
author = 'Felipe Santana'



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
