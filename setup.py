import io
import re
from setuptools import setup

import os, sys
import shutil

try:
    shutil.rmtree(os.path.join(os.path.dirname(__file__), 'pheader'))
except:
    print("Can't Remove directory, directory not found ! [pass]")
    
try:
    os.makedirs(os.path.join(os.path.dirname(__file__), 'pheader'))
except:
    pass
try:
    os.remove(os.path.join('pheader', '__version__.py'))
except:
    pass
shutil.copy2('__version__.py', 'pheader')
shutil.copy2('pheader.py', 'pheader')
shutil.copy2('__init__.py', 'pheader')

# with io.open("README.rst", "rt", encoding="utf8") as f:
#     readme = f.read()

# with io.open("__version__.py", "rt", encoding="utf8") as f:
    # version = re.search(r"version = \'(.*?)\'", f.read()).group(1)
import __version__
version = __version__.version

requirements = [
        'make_colors>=3.12',
        'clipboard',
        'pydebugger',
    ]

setup(
    name="pheader",
    version=version,
    url="https://github.com/cumulus13/pheader",
    project_urls={
        "Documentation": "https://github.com/cumulus13/pheader",
        "Code": "https://github.com/cumulus13/pheader",
    },
    license="BSD",
    author="Hadi Cahyadi LD",
    author_email="cumulus13@gmail.com",
    maintainer="cumulus13 Team",
    maintainer_email="cumulus13@gmail.com",
    description="Just parser header from string/copy",
    # long_description=readme,
    # long_description_content_type="text/markdown",
    packages=["pheader"],
    install_requires=requirements,
    entry_points = {
         "console_scripts": [
             "pheader = pheader.pheader:usage",
         ]
    },
    # data_files=['__version__.py'],
    include_package_data=True,
    python_requires=">=2.7",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)
