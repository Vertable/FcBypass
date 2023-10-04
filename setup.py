from setuptools import setup, find_packages

setup(
    name='fcbypass',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        "requests"
    ],
    author='Vertable',
    author_email='Vertable@example.com',
    description='A package designed for making requests to Capbypass for Roblox.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    url='https://github.com/Vertable/fcbypass',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
