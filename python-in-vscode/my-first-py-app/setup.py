from setuptools import setup, find_packages

setup(
    name='my_first_py_app',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A short description of my awesome package.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/my-awesome-package',
    packages=find_packages(),
    license = "MIT",
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    install_requires=[
        'requests>=2.25.1',
        'numpy>=1.20.0'
    ]
)