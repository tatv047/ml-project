from setuptools import find_packages,setup # find_packages: finds all the packages used in the project
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]: 
    """
    This function will return a list of all the requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        """
        readlines() will read all the lines in the file and return them as a list,
        but the problem is it will also include the '\n' character at the end of each line.
        Hence we are using list comprehension to strip the '\n' character from the end of each line.
        """
        requirements = [requirement.strip() for requirement in requirements] 

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements


# parameters/metadata info about the entire project
setup(
name = 'ML-Project',
version='0.0.1',
author='Utkarsh Dev',
author_email='utkarshdev047@gmail.com',
packages=find_packages(),
install_requires = get_requirements('requirements.txt') # all the requirements you want
)
