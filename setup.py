try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='evxpredictor',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    version='0.1.6',
    description='A package for predicting buy and sell signals',
    license='MIT',
    author='Nicolus Rotich',
    author_email='nicholas.rotich@gmail.com',
    install_requires=[
    	"setuptools>=57",
    	"wheel",
    	"Keras==2.4.3",
    	"silence-tensorflow==1.1.1",
    	"tensorflow==2.2.0",
    	"scikit-learn==0.22.2.post1",
    	"scipy==1.4.1",
    	"h5py==2.10.0",
    	"scipy==1.4.1",
        "fire"
    ],
    url='https://nkrtech.com',
    download_url='https://github.com/moinonin/evxpredictor/archive/refs/heads/main.zip',
    classifiers=[
        'License :: OSI Approved :: MIT License',
    ],
)
