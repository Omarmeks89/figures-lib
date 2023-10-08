from setuptools import setup, find_packages


if __name__ == "__main__":
    setup(
        name="figures",
        version="0.1.0",
        package_dir={"": "figures"},
        packages=find_packages(where="figures"),
        python_requires=">=3.11",
        description="test assembly",
    )
