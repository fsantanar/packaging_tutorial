from setuptools import find_packages, setup

setup(
    name='example_package_fsantanar',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy==1.24.3',
        'PyYAML==6.0',
    ],
)
