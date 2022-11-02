from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    requirement_list:List[str]=[]
    fh = open('requirements.txt')
    for num in  fh:
        requirement_list.append(num[:-2]) 
    #print(requirement_list)
    return requirement_list



setup(
    name='sensor',
    version='0.0.1',
    author='sanjay',
    author_email='sanjaybalekar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)