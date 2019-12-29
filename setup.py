from setuptools import setup, find_packages

setup(
    name="travelplanner",
    version="1.0.0",
    author='Yue Li',
    packages=find_packages(exclude=['*tests']),
    install_requires=['argparse', 'numpy', 'matplotlib'],
    entry_points={
        'console_scripts': [
            'bussimula = travelplanner.command:process'
        ]})
