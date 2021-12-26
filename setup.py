from setuptools import setup, find_packages

setup(
    name='hang_up_an_autumn_moon',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts':[
            'hang-up-an-autumn-moon=cli.main:cli',
        ]
    }        
)