from setuptools import find_packages, setup

from os import path
top_level_directory = path.abspath(path.dirname(__file__))
with open(path.join(top_level_directory, 'README.md'), encoding='utf-8') as file:
    long_description = file.read()

setup(
    name='netbox_zero',
    version='0.1.0',
    url='https://github.com/sapcc/netbox-zero',
    download_url='https://github.com/sapcc/netbox-zero/archive/v0.1.0.tar.gz',
    description='A zero touch provisioning plugin for Netbox.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Andrew Battye',
    author_email='andrew.battye@sap.com',
    install_requires=[],
    packages=find_packages(),
    license='Apache',
    include_package_data=True,
    keywords=['netbox', 'netbox-plugin', 'plugin'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
