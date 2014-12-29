import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
	name="django-bb-mchanga",
	version='0.1',
	packages=['bb_mchanga'],
	include_package_data=True,
	license='None',
	description='A small app to communicate with M-Changa API',
	long_description=README,
	url="http://onepercentclub.com",
	author="Loek van Gent",
	author_email="loek@onepercentclub.com",
	classifiers=[
	    'Environment :: Web Environment',
	    'Framework :: Django',
	    'Intended Audience :: Developers',
	    'License :: OSI Approved :: None', 
	    'Operating System :: OS Independent',
	    'Programming Language :: Python',
	    'Topic :: Internet :: WWW/HTTP',
	    'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
	]

)

