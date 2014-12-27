from setuptools import setup

setup(name='cloudbarista',
      version='0.1',
      description='Declarative cloud orchestrization library',
      url='https://github.com/pphanireddy/cloud-barista',
      author='Phani Reddy',
      author_email='pphanireddy@gmail.com',
      license='MIT',
      packages=['cloudbarista'],
      install_requires=[
          'azure',
      ],
      zip_safe=False)
