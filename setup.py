from setuptools import setup

setup(
	name='python-testing',
	version='0.0.1',
	url='https://github.com/28064212/python-testing',
	# To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
            'python-testing=python-testing:main',
        ],
},
)