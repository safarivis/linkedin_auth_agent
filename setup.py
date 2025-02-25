from setuptools import setup, find_packages

setup(
    name="linkedin_auth_agent",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
    ],
    author="safarivis",
    author_email="safarivis@github.com",
    description="A LinkedIn OAuth 2.0 authentication package using OpenID Connect",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/safarivis/linkedin_auth_agent",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
