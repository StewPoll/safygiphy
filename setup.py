from setuptools import setup

setup(name='safygiphy',
      version='1.1.0',
      description='API Wrapper for the online Gif library, Giphy',
      url='https://code.tetraetc.com/SafyGiphy/',
      author="TetraEtc",
      author_email="administrator@tetraetc.com",
      install_requires=[
          'requests'
      ],
      packages=['safygiphy']
      )