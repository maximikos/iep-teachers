### path setup ####################################################################################

from glob import glob
import datetime
import os
 
###################################################################################################
### Project Information ###########################################################################
###################################################################################################

project = 'IEP'
copyright = datetime.date.today().strftime("%Y") + ' International Society for Industrial Ecology'
version: str = 'teachers' # required by the version switcher

###################################################################################################
### Project Configuration #########################################################################
###################################################################################################

needs_sphinx = '5.3.0'

extensions = [
    # core extensions
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.napoleon',
    'sphinx.ext.inheritance_diagram',
    'sphinxcontrib.bibtex',
    #'sphinx.ext.githubpages',
    # iPython extensions
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    # Markdown support
    # 'myst_parser', # do not enable separately if using myst_nb, compare: https://github.com/executablebooks/MyST-NB/issues/421#issuecomment-1164427544
    # Jupyter Notebook support
    'myst_nb',
    # API documentation support
    #'autoapi',
    # responsive web component support
    'sphinx_design',
    # custom 404 page
    'notfound.extension',
    # custom favicons
    'sphinx_favicon',
    # copy button on code blocks
    "sphinx_copybutton",
]

root_doc = 'index'
html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = ['_build']
html_theme = "pydata_sphinx_theme"
html_logo = "_static/logo/iep_logo_small.png"

suppress_warnings = [
    "myst.header" # suppress warnings of the kind "WARNING: Non-consecutive header level increase; H1 to H3"
]

# https://myst-nb.readthedocs.io/en/v0.8.4/use/myst.html#parse-extensions-other-than-md-and-ipynb
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'myst-nb',
    '.ipynb': 'myst-nb',
    '.myst': 'myst-nb',
}

####################################################################################################
### Theme html Configuration #######################################################################
####################################################################################################

html_show_sphinx = False
html_show_copyright = True

html_css_files = [
    "css/custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" # for https://fontawesome.com/ icons
]

html_sidebars = {
    "index": [],
}

html_theme_options = {
    # https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/version-dropdown.html
    "switcher": {
        "json_url": "https://raw.githubusercontent.com/maximikos/iep-teachers/main/source/_static/switcher.json",
        "version_match": version
    },
    # page elements
    "navbar_start": ["navbar-logo", "version-switcher"],
    #"navbar_end": ["theme-switcher", "navbar-icon-links.html"],
    "navbar_end": ["navbar-icon-links.html"],
    "footer_start": ["copyright"],
    "footer_end": ["footer"],
    "secondary_sidebar_items": ["page-toc", "searchbox", "edit-this-page", "sourcelink", "support"],
    "header_links_before_dropdown": 3,
    # page elements content
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/maximikos/iep-teachers",
            "icon": "fa-brands fa-github",
            "type": "fontawesome",
        },
    ],
    # various settings
    "collapse_navigation": True,
    "show_prev_next": False,
    "use_edit_page_button": True,
    "navigation_with_keys": True,
    #"logo": {
    #    "text": "IEP",
    #    "image_light": "iep_logo.png",
    #    "image_dark": "logo/iep_logo_small.png"
    #},
}

# required by html_theme_options: "use_edit_page_button"
html_context = {
    "github_user": "maximikos",
    "github_repo": "iep-teachers",
    "github_version": "main",
    "doc_path": "source",
}

####################################################################################################
### Extension Configuration ########################################################################
####################################################################################################

# bibtex Configuration ############################################
# https://sphinxcontrib-bibtex.readthedocs.io

bibtex_bibfiles = ['references/refs.bib']

# linkcheck Configuration ###############################################
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

linkcheck_retries = 1
linkcheck_workers = 20
linkcheck_exclude_documents = []

# notfound Configuration ################################################
# https://sphinx-notfound-page.readthedocs.io

notfound_context = {
    'title': 'Page Not Found',
    'body': '''                                                                         <h1>🍂 Page Not Found (404)</h1>
    <p>
    Oops! It looks like you've stumbled upon a page that's been recycled into the digital abyss.
    But don't worry, we're all about sustainability here.
    Why not take a moment to reduce, reuse, and recycle your clicks by heading back to the main page?
    And remember, every little bit counts in the grand scheme of things.
    </p>
    ''',
}

notfound_urls_prefix = '/iep-teachers/'

# autoapi Configuration ################################################
# https://sphinx-autoapi.readthedocs.io/en/latest/reference/config.html#customisation-options

#autoapi_dirs = [
#    '...',
#]

autoapi_ignore = [
    '*/data/*',
    '*tests/*',
    '*tests.py',
    '*validation.py',
    '*version.py',
    '*.rst',
    '*.yml',
    '*.md',
    '*.json',
    '*.data'
]

autoapi_options = [
    'members',
    'undoc-members',
    'private-members',
    'show-inheritance',
    'show-module-summary',
    #'special-members',
    #'imported-members',
    'show-inheritance-diagram'
]

autoapi_python_class_content = 'both'
autoapi_member_order = 'groupwise'
autoapi_root = 'api'
autoapi_keep_files = False

# myst_parser Configuration ############################################
# https://myst-parser.readthedocs.io/en/latest/configuration.html

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
]

# myst-nb configuration ################################################
# https://myst-nb.readthedocs.io/en/latest/configuration.html

nb_execution_mode = 'off'


# sphinx-favicon configuration #########################################
# https://github.com/tcmetzger/sphinx-favicon

favicons = [
    {
        "rel": "icon",
        "sizes": "100x100",
        "href": "logo/iep_favicon.ico",
    },
]
