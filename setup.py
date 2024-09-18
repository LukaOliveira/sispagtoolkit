from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="SispagToolKit",
    version="0.1.1",
    description="Biblioteca para geração de remessas de pagamento CNAB240 baseada para o sistema SISPAG da instituição Itaú.",
    long_description=long_description,  # Apontando para o conteúdo do README
    long_description_content_type="text/markdown",  # Definindo o formato como Markdown
    author="Pedro Luka Oliveira",
    author_email="pedrolukaoliveira@protonmail.com",
    url="https://github.com/LukaOliveira/sispagtoolkit", 
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
