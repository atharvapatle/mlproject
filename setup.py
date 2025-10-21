from setuptools import find_packages,setup
HED='-e .'
def get_requirements(file_path):
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HED in requirements:
            requirements.remove(HED)

setup(
    name='ml project',
    version='0.0.1',
    author='Atharva',
    author_email='atharvapatle001@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)