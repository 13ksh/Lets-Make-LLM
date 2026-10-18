# ==============================================================================
# Lets-Make-LLM (LML) Setup Script
#
# Note:
#   Currently in initial setup stage. Editable installation (pip install -e .)
#   and PyPI package distribution are planned for upcoming versions (v0.2.0+).
#
#   For now, this repository relies on standalone scripts and native installers
#   (Debian .deb / Inno Setup .exe).
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
