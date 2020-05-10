# from distutils.core import setup
import setuptools

setuptools.setup (
    name = 'nester',
    verison = '1.0.0',
    license='MIT',
    py_modules = ['nester'],
    description = 'nested 리스트를 간단하게 출력하기',
    author = 'smallrich',
    author_email = 'hanminwoo0306@gmail.com',
    long_description = open('README.md').read(),
    url = 'https://github.com/hanminwoo0306/smallrich',
    packages = setuptools.find_packages(),
    classifiers = [
        # 패키지에 대한 태그
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)