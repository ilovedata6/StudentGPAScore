from setuptools import setup,find_packages # type: ignore
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(path:str)->List[str]:
    requirements = []
    with open('requirements.txt') as f:
        requirements=f.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
            return requirements

setup(
    name="Student GPA Predictor",
    version="0.0.1",
    author="Bilal Saeed",
    author_email="ibilalsaeed@outlook.com",
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')
    
)