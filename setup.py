from setuptools import setup, find_packages

setup(
    name='mis-algorithm-group-b',
    url='https://git.scicore.unibas.ch/zavolan_group/teaching_and_tutorials/pls-2023-group-b',
    author='Seunghyun Kim, Xuehan Li, Thurre Loïc',
    author_email='seunghyun.kim@stud.unibas.ch, xuehan.li@stud.unibas.ch, loic.thurre@stud.unibas.ch',
    description='This project is a group project of Programming for Life Science that implements the MIS algorightm described in the following paper: Afek, Y., Alon, N., Barad, O., Hornstein, E., Barkai, N., & Bar-Joseph, Z. (2011). A biological solution to a fundamental distributed computing problem. science, 331(6014), 183-185.',
    license='MIT',
    version='1.0.0',
    packages=find_packages(),
    install_requires=["matplotlib", "networkx", "scipy"], 
    entry_points = {
        'console_scripts': ['mis-algorithm=src.main:main'],
    },
)