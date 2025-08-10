from setuptools import setup, find_packages

setup(
    name=\'quantum_portfolio_optimization\',
    version=\'0.1.0\',
    packages=find_packages(),
    install_requires=[
        \'numpy\',
        \'scipy\',
        \'qiskit==0.45.0\', # Specific version for compatibility
        \'qiskit-aer==0.12.0\', # Specific version for compatibility
        \'qiskit-algorithms==0.2.1\', # Specific version for compatibility
        \'qiskit-optimization==0.5.0\', # Specific version for compatibility
    ],
    author=\'Manus AI\',
    description=\'Quantum-Enhanced Portfolio Optimization for Vanguard\',
    long_description=open(\'README.md\').read(),
    long_description_content_type=\'text/markdown\',
    url=\'https://github.com/your_username/quantum_portfolio_optimization\', # Replace with actual GitHub URL
    classifiers=[
        \'Programming Language :: Python :: 3\',
        \'License :: OSI Approved :: MIT License\',
        \'Operating System :: OS Independent\',
    ],
    python_requires=\'>=3.7\',
)


