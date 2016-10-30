from distutils.core import setup
from distutils.extension import Extension

source = "src/"
directories = {
    "cardio": source+"cardio/",
    "model": source+"model/",
    "sport": source+"sport/"
}

ext_modules = [
    Extension("enums", [source+"enums.c"]),
    Extension("mets", [source+"mets.c"]),

    Extension("cardio.heart", [directories["cardio"]+"heart.c"]),
    Extension("cardio.vo2", [directories["cardio"]+ "vo2.c"]),
    Extension("cardio.rmr", [directories["cardio"]+ "rmr.c"]),
    Extension("cardio.tee", [directories["cardio"]+ "tee.c"]),
    Extension("cardio", [directories["cardio"]+ "heart.c", directories["cardio"]+"rmr.c", directories["cardio"]+ "tee.c", directories["cardio"]+"vo2.c" ]),

    Extension("composition", [source+"composition.c"]),

    Extension("models.aerobic", [directories["model"]+ "aerobic.c"]),
    Extension("models", [directories["model"]+ "aerobic.c"]),

    Extension("sport.running.adjustment", [directories["sport"]+"running/adjustment.c"]),
    Extension("sport.running.grading", [directories["sport"]+"running/grading.c"]),
    Extension("sport.running.jackdaniels", [directories["sport"]+"running/jackdaniels.c"]),
    Extension("sport.running.pace", [directories["sport"]+"running/pace.c"]),

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
        ext_modules = cythonize([
            source+"balance.pyx",
            source+"enums.pyx",
            source+"mets.pyx",
            directories["cardio"]+"heart.pyx",
            directories["cardio"]+"vo2.pyx",
            directories["cardio"]+"rmr.pyx",
            directories["cardio"]+"tee.pyx",

            source+"flexibility.pyx",

            directories["model"] + "aerobic.pyx",

            directories["sport"] + "running/adjustment.pyx",
            directories["sport"] + "running/grading.pyx",
            directories["sport"] + "running/jackdaniels.pyx",
            directories["sport"] + "running/pace.pyx",

            source+"composition.pyx",
            source+"strength.pyx"
        ])
    )
else:
    setup(name="pyfit", version='1.0', ext_package='pyfit', ext_modules=ext_modules)
