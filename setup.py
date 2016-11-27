from setuptools import find_packages
from distutils.core import setup
from distutils.extension import Extension
import os
import io

def readfile(fname):
    path = os.path.join(os.path.dirname(__file__), fname)
    return io.open(path, encoding='utf8').read()

package_data = {
    'pyfit': ['*/*.pxd'],
}

source = "pyfit/"
directories = {
    "cardio": source+"cardio/",
    "model": source+"model/",
    "sport": source+"sport/"
}

ext_modules = [
    Extension("balance", [source+"balance.c"]),
    Extension("enums", [source+"enums.c"]),
    Extension("mets", [source+"mets.c"]),

    Extension("cardio.cardiac", [directories["cardio"]+"cardiac.c"]),
    Extension("cardio.energy", [directories["cardio"]+ "energy.c"]),
    Extension("cardio.respiration", [directories["cardio"]+ "respiration.c"]),

    Extension("composition", [source+"composition.c"]),

    Extension("flexibility", [source+"flexibility.c"]),

    Extension("models.aerobic", [directories["model"]+ "aerobic.c"]),
    Extension("models", [directories["model"]+ "aerobic.c"]),

    Extension("sport.running.adjustment", [directories["sport"]+"running/adjustment.c"]),
    Extension("sport.running.grading", [directories["sport"]+"running/grading.c"]),
    Extension("sport.running.jackdaniels", [directories["sport"]+"running/jackdaniels.c"]),

    Extension("strength", [ source+"strength.c"]),
]


try:
    from Cython.Build import cythonize
    use_cython =  True
except ImportError:
    use_cython = False

if use_cython:
    setup(
        name="pyfit",
        version='2.0',
        description='Python framework for fast health-care calculations',
        long_description=readfile('README.md'),
        packages= find_packages(),
        package_data=package_data,
        ext_modules = cythonize([
            source+"balance.pyx",
            source+"enums.pyx",
            source+"mets.pyx",
            directories["cardio"]+"cardiac.pyx",
            directories["cardio"]+"energy.pyx",
            directories["cardio"]+"respiration.pyx",

            source+"flexibility.pyx",

            directories["model"] + "aerobic.pyx",

            directories["sport"] + "running/adjustment.pyx",
            directories["sport"] + "running/grading.pyx",
            directories["sport"] + "running/jackdaniels.pyx",

            source+"composition.pyx",
            source+"strength.pyx"
        ]),
        test_suite='test',
        author=u'Doug Fenstermacher',
        author_email='douglas.fenstermacher@gmail.com',
        url='dpfens.github.io/PyFit',
        keywords='health, physical fitness, cardio, heart rate, VO2Max, energy expenditure, resting metabolic rate, respiration, residual volume, body composition, metabolic equivalents, body surface area, strength, 1-rm, jack daniels',
        platforms='any',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python',
            'Intended Audience :: Science/Research',
            'Intended Audience :: Healthcare Industry',
            'Intended Audience :: Developers',
            'Topic :: Scientific/Engineering :: Mathematics',
            'Topic :: Scientific/Engineering :: Medical Science Apps.'
        ]
    )
setup(
    name="pyfit",
    version='2.0',
    description='Python framework for fast health-care calculations',
    long_description=readfile('README.md'),
    packages= find_packages(),
    package_data=package_data,
    ext_modules=ext_modules,
    author=u'Doug Fenstermacher',
    author_email='douglas.fenstermacher@gmail.com',
    url='dpfens.github.io/PyFit',
    keywords='health, physical fitness, cardio, heart rate, VO2Max, energy expenditure, resting metabolic rate, respiration, residual volume, body composition, metabolic equivalents, body surface area, strength, 1-rm, jack daniels',
    platforms='any',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
    ]
)
