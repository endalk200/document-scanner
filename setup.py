
import setuptools
import pathlib

BASE_DIR = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (BASE_DIR / 'README.md').read_text(encoding='utf-8')


setuptools.setup(
    name="document_scanner",
    version="0.1.9",

    author="Endalkachew Biruk",
    author_email="eb808826@gmail.com",

    description="Document scanner built using python opencv.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/endalk200/document-scanner",

    install_requires=[
        "matplotlib==3.2.2",
        "numpy==1.18.5",
        "ocrd-fork-pylsd==0.0.3",
        "opencv-python==4.2.0.34",
        "scipy==1.10.0"
    ],

    scripts=["./scan.py"],

    classifiers=[
        "Development Status :: 3 - Alpha",

        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        "Intended Audience :: Education",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

        "Topic :: Utilities",
    ],
    python_requires='>=3.4',
)