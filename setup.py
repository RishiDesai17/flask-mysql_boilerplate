import io
from setuptools import setup

setup (
    name="bankApp",
    version="1.0.0",
    description="Bank portal built for DBMS & WT mini project",
    install_requires=["flask", "pymysql", "python-dotenv"],
)