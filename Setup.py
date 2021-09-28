#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup

with open("C:/Users/windowsChimp/Desktop/RUN2/NEW/README.txt","r") as fh:
    long_description=fh.read()
clas=[
    "Intended Audience :: Education",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
    "Programming Language :: Python :: 3"
]
setup(
    name="NPHIconvert",
    version="0.0.2",
    description="Apparent Neutron Porosity to True Porosity Conversion",
    py_modules=["NPHIconvert"],
    package_dir={"":"src"},
    classifiers=clas,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/farooqad0/NPHIconvert",
    author="Farooq Arshad",
    author_email="farooqad0@gmail.com",
    install_requires = [
        "numpy>=1.15",
        "matplotlib>=3.0",
        ]
    
    
)
    
