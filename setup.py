from setuptools import find_packages, setup
from typing import List 


HYPHEN_DOT_E = '-e .'

def get_requirements(file_path:str)-> List[str]:
    
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements= [req.replace('\n',"") for req in requirements]
        
        if HYPHEN_DOT_E in requirements:
            requirements.remove(HYPHEN_DOT_E)
    return requirements

setup(
    
    name= 'Student ML Project',
    version = "1.0",
    author="Ashan",
    author_email="ashanddb@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)