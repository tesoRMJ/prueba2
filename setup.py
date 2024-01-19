from setuptools import setup, find_packages
setup(
    name='prueba2',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts':[
            'ejecucion = prueba2.__main__:main',
        ],
    },
)