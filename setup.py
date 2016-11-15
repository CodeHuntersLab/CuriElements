from distutils.core import setup

setup(
    name='CuriElements',
    version='0.1.6.2',
    packages=['CuriElements'],
    url='https://github.com/CodeHuntersLab/CuriElements',
    license='LGPL3 GPL3',
    author='eyllanesc',
    author_email='e.yllanescuho@gmail.com',
    description='Proyecto orientado a la enseñanza y aprendizaje de la tabla períodica ',
    install_requires=["PyQt5>=5.7", "gTTS>=1.1.6", "wikipedia>=1.4.0"],
)
