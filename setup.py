from setuptools import setup, find_packages

setup(
    name="timetable-2024",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pandas","numpy","ortools","streamlit"],
)
