from setuptools import setup, find_packages

setup(
    name="mmsyllable",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Khant Sint Heinn",
    author_email="kalixlouiis@gmail.com",
    description="A simple, rule-based tool for Burmese syllable segmentation.",
    long_description=open("README.md").read() if open("README.md") else "Burmese syllable tokenizer",
    long_description_content_type="text/markdown",
    url="https://github.com/kalixlouiis/mm-syllable",
    project_urls={
        "Bug Tracker": "https://github.com/kalixlouiis/mm-syllable/issues",
    },
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
