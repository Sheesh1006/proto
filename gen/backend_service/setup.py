from setuptools import setup, find_packages


setup(
    name='backend_service',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'grpcio',
        'grpcio-tools'
    ],
    description='A package for Backend service',
    author='Sheesh1006',
    author_email='cloudmeme@yandex.ru',
    url='https://github.com/Sheesh1006/service-backend',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)