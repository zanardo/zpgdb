import re
from setuptools import setup

# argh!
version = ""
with open("zpgdb.py", "r") as fp:
    version = re.search(r"^__VERSION__ = '(.+?)'$", fp.read(),
                        re.MULTILINE).group(1)
if not version:
    raise RuntimeError("Error getting version!")


setup(
    name="zpgdb",
    version=version,
    py_modules=["zpgdb"],
    install_requires=["psycopg2>=2.7.0,<=2.7.999"],
    package_data={
        "": ["README.md", "COPYING"]
    },
    author="Antonio Zanardo",
    author_email="zanardo@gmail.com",
    description="Library for simple PostgreSQL connection and transaction management",
    license="BSD",
    keywords="postgresql database transaction connection",
    url="https://github.com/zanardo/zpgdb",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Database",
    ],
)
