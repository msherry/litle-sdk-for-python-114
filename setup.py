#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup, find_packages
setup(name='LitleSdkPython-114',
      version='8.13.2',
      description='Litle & Co. SDK for Python',
      author='Litle & Co',
      author_email='SDKSupport@litle.com',
      url='http://www.litle.com/developers',
      packages=['litleSdkPython'],
      install_requires=[
          'PyXB_114',
      ],
      dependency_links=[
          'https://github.com/msherry/PyXB-1.1.4/tarball/master#egg=pyxb_114-1.1.4',
      ],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Environment :: Web Environment',
          'Environment :: MacOS X'
          'Environment :: Plugins'
          'Environment :: Win32 (MS Windows)'
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Intended Audience :: Information Technology',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent'
          'Operating System :: MacOS',
          'Operating System :: Microsoft',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Topic :: Office/Business :: Financial',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
     )
