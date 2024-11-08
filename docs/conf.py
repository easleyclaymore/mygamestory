# -- Project information -----------------------------------------------------
# https://sphinx-doc.cn/en/master/usage/configuration.html#project-information

project = '我的游戏帝国'
copyright = '2000-2092, The Test Project Authors'
author = 'easleyclaymore'
version = release = '4.16'

# -- General configuration ------------------------------------------------
# https://sphinx-doc.cn/en/master/usage/configuration.html#general-configuration

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
]
extensions = []
language = 'en'
master_doc = 'index'
pygments_style = 'sphinx'
source_suffix = '.rst'
#templates_path = ['_templates']

# -- Options for HTML output ----------------------------------------------
# https://sphinx-doc.cn/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
#html_static_path = ['_static']