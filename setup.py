from setuptools import setup
    
    
def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name='gadget', # project name
    version='0.1.0', # version
    author='Baoming Yu', # author's name
    author_email='dingxuanliang@icloud.com', # author's email
    url='https://github.com/Baoming520/gadget', # url on github
    description='Use an elegant way to assemble SQL blocks in python project.', # abstract
    long_description=readme(), # contents in README.MD file
    long_description_content_type="text/markdown", # type of long description
    packages=['gadget'], # pakages waiting for packing
    package_data={}, # data files in package
    install_requires=[], # required packages
)