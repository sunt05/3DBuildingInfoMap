from setuptools import setup
import pandas as pd


ser_ver = pd.read_json("./src/shaft_version.json", typ="series", convert_dates=False)
print(ser_ver)
__version__ = f"{ser_ver.ver_milestone}.{ser_ver.ver_major}.{ser_ver.ver_minor}{ser_ver.ver_remark}"


def readme():
    try:
        with open("./README.md", encoding="utf-8") as f:
            return f.read()
    except:
        return f"SHAFT package"


setup(
    name="shaft",
    version=__version__,
    description="Simultaneous building Height And FootprinT extraction from Sentinel Imagery",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/LllC-mmd/3DBuildingInfoMap",
    author=", ".join(
        [
            "Ruidong Li"
            "Dr Ting Sun",
            "Prof Guangheng Ni",
        ]
    ),
    author_email=", ".join(
        [
            "lrd19@mails.tsinghua.edu.cn"
            "ting.sun@reading.ac.uk",
            "ghni@tsinghua.edu.cn",
        ]
    ),
    license="GPL-V3.0",
    packages=["shaft"],
    package_data={
        "shaft": [
            "*.json",
            "utils/*",
        ]
    },
    # distclass=BinaryDistribution,
    ext_modules=[],
    install_requires=[
        "pytorch=1.8.*",
        "torchvision=0.9.*",
        "albumentations=0.5.*",
        "scikit-learn=0.24.*",
        "scikit-image=0.17.*",
        "xgboost=1.3.*",
        "gdal=3.0.*",
        "opencv-python", 
        "numpy",
        "matplotlib",
        "scipy",
        "seaborn",
        "cartopy",  
        "pandas",  
        "h5py",  
        "rasterio",  
        "geopandas",  
        "lmdb",
        "pyarrow",
        "earthengine-api",
        "kneed",  # kneed point detection for CCAP algorithms
    ],
    include_package_data=True,
    python_requires="=3.7.*",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
    ],
    zip_safe=False,
)