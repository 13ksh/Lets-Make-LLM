# ==============================================================================
# Lets-Make-LLM (LML) Setup Script
#
# Note:
#   This setup.py is designed for local editable installation (pip install -e .)
#   and script-based packaging (Debian .deb / Inno Setup .exe).
#   PyPI remote publishing is intentionally bypassed.
#
# Development Usage:
#   pip install -e .                  # Install in editable mode for active development
#   lml --version                     # Test CLI router directly
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
