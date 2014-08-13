from setuptools import setup, find_packages

setup(
    name='HoneyMalt',
    author='catalyst256',
    version='1.0',
    author_email='catalyst256@gmail.com',
    description='Maltego Transforms for interaction with Honeypots',
    license='GPL',
    packages=find_packages('src'),
    package_dir={ '' : 'src' },
    zip_safe=False,
    package_data={
        '' : [ '*.gif', '*.png', '*.conf', '*.mtz', '*.machine' ] # list of resources
    },
    install_requires=[
        'canari >= 1.0',
        'mysql_connector_python >= 1.2.2',
        'pygeoip >= 0.3.1'
    ],
    dependency_links=[
        # custom links for the install_requires
    ]
)
