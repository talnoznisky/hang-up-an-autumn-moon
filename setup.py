from setuptools import setup, find_packages
import pathlib

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name='hang_up_an_autumn_moon',
    version='0.2.0',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['main'],
    long_description=README,
    long_description_content_type="text/markdown",
    install_requires=[
        'Click',
        'simple_term_menu',
        'prettytable',
        'numpy'
    ],
    entry_points={
        'console_scripts':[
            'hang-up-an-autumn-moon=cli.main:cli',
        ]
    }        
)
