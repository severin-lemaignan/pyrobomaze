import setuptools

setuptools.setup(
    name="pyrobomaze",
    version="1.0.0",
    author="Séverin Lemaignan",
    author_email="severin.lemaignan@brl.ac.uk",
    description="A A* pathfinder to solve the robomaze game",
    url="https://github.com/severin-lemaignan/pyrobomaze",
    install_requires=['requests'],
    package_dir = {'': 'src'},
    packages=['robomaze'],
    scripts=['scripts/pyrobomaze'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

