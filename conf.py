from recommonmark.parser import CommonMarkParser
extensions = ['sphinx.ext.mathjax',
    'sphinx.ext.githubpages']
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
source_parsers = {
        '.md': CommonMarkParser,
        }
master_doc = 'index'
project = 'Tecnólogo em Sistemas para Internet'
copyright = '2018, IFRN'
author = 'IFRN'
version = '2012'
release = '2012'
language = 'pt_BR'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'tsidoc'
latex_elements = {
}
latex_documents = [
    (master_doc, 'tsi.tex', 'Tecnólogo em Sistemas para Internet',
     'IFRN', 'manual'),
]
man_pages = [
    (master_doc, 'tcnicointegradoeminformtica', 'Tecnólogo em Sistemas para Internet',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'tsi', 'Tecnólogo em Sistemas para Internet',
     author, 'tsi', 'One line description of project.',
     'Miscellaneous'),
]
