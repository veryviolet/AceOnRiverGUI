from setuptools import setup, find_packages

setup(
    name = 'AceOnRiverGUI',
    version = '0.0.1',
    author = 'veryviolet',
    author_email = 'veryviolet@zoho.com',
    description = 'GUI application for AceOnRiver',
    license = 'MIT',
    keywords = 'python poker engine gui',
    url = 'https://github.com/veryviolet/AceOnRiver',
    packages = [pkg for pkg in find_packages() if pkg != "tests"],
    package_data={
        'aceonrivergui': [
            'server/static/*.css',
            'server/static/*.js',
            'server/static/images/*',
            'server/templates/*',
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
    ],
    install_requires=[
        'pypokerengine',
        'tornado==4.4.2',
        'click==6.7',
        'PyYAML==3.12',
    ],
    entry_points={
        'console_scripts': ['aceonrivergui=aceonrivergui.__main__:cli']
    },
    )

