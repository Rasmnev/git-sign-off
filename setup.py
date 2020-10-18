from setuptools import setup, find_packages

setup(
    name="git-sign-off",
    version="0.1.0",
    description="Sign off git certificates for tasks and check them.",
    author="Alberto Ferreira",
    packages=find_packages(exclude=["tests"]),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "git-sign-off = git_sign_off.__main__:main_sign",
            "git-sign-off-check = git_sign_off.__main__:main_check",
        ]
    },
)
