# ==============================================================================
# Lets-Make-LLM (LML) Setup Script - v0.1.0-alpha
#
# Note:
#   Currently in the initial setup stage. Running editable installation 
#   (pip install -e .) will result in dependency or runtime errors at this time.
#
#   Local editable installation (pip install -e .) is planned for the next 
#   alpha release (v0.2.0-alpha), while remote PyPI distribution is deferred 
#   to a much later roadmap.
#
#   For now, this repository relies entirely on standalone scripts and native 
#   installers (Debian .deb / Inno Setup .exe).
# ==============================================================================

from setuptools import setup

setup(
    name='lml',
    version='0.1.0-alpha',
    py_modules=['lml_core', 'lml_engine', 'lml_config', 'lml_dataset_loader', 'lml_utils'],
    install_requires=[
        'transformers',
        'torch',
        'datasets',
        'accelerate',
    ],
    entry_points={
        'console_scripts': [
            'lml=lml_engine:main',
        ],
    },
)
