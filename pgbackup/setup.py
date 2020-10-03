from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()
setup(
    name="pgbackup",
    version="0.1",
    description='Database backups locally or to AWS s3',
    long_description=readme,
    author='Nick',
    author_email='wildman@gmail.com',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'': 'src'}
)

