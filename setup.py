import setuptools


with open("README.md", "r") as ld:
    long_description = ld.read()



__version__ ="0.0.0"
Repo_name = "End_to_End_MLProject_with-MLFLOW"
Author_name = "saisuryachandraprasad"
Author_email = "saisuryachandraprasad@gmail.com"


setuptools.setup(
    name=Repo_name,
    author=Author_name,
    author_email=Author_email,
    version=__version__,
    long_description=long_description,
    url=f"https://github.com/{Author_name}/{Repo_name}",
    packages=setuptools.find_packages(where="src")
)