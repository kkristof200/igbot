from codecs import open
from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))
p_readme = path.join(here, "README.md")

# Get the long description from the README file
if path.exists(p_readme):
    with open(p_readme, encoding="utf-8") as f:
        long_description = f.read()
else:
    long_description = ''

setup(
    name="kfork-instabot",
    version="0.117.2",
    description="Instagram bot scripts for promotion and API python wrapper.",
    long_description=long_description,
    author="Daniil Okhlopkov, Evgeny Kemerov",
    author_email="danokhlopkov@gmail.com, eskemerov@gmail.com",
    license="Apache Software License 2.0",
    url="https://github.com/instagrambot/instabot",
    keywords=["instagram", "bot", "api", "wrapper"],
    install_requires=["requests", "huepy", "rsa", "pytz", "~qdm", "schedule", "six", "responses", "requests_toolbelt", "pytest", "mock", "~ip", "moviepy", "Pillow", "pip", "pycryptodome", "pycryptodomex", "secrets", "tqdm"],
    classifiers=[
        # How mature is this project? Common values are
        "Development Status :: 5 - Production/Stable",
        # Indicate who your project is intended for
        "Intended Audience :: Information Technology",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: Apache Software License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
)
