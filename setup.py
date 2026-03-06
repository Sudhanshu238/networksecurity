'''
The setup.py file is an esssential part of packaging and distrbuting Python objects.
It is used by setuptools (or distutils in older Python version)
to define the configuration of your projects , such as its metadata, dependencies, and more


'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    Thiss function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            ## Read line from the file 
            lines=file.readlines()
            ##Process each line
            for line in lines:
                requirement=line.strip()
                ##ignore the empty line  and -e.
                if requirement and requirement!='-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found ")

    return requirement_lst  


print(get_requirements())


setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Sudhanshu",
    author_email="tiwarysudhanshu03@gmail.com",
    package=find_packages(),
    install_requires=get_requirements( )


)