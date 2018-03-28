from setuptools import setup

url = ""
version = "0.1.0"
readme = open('README.rst').read()

setup(
    name="lae_regression",
    packages=["lae_regression"],
    version=version,
    description="Least absolute error regression implmented using linear programming.",
    long_description=readme,
    include_package_data=True,
    author="Aaron Watters",
    author_email="awatters@flatironinstitute.org",
    url=url,
    install_requires=[],
    download_url="{}/tarball/{}".format(url, version),
    license="MIT"
)
