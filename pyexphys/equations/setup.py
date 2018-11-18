from distutils.core import setup, Extension
from os import listdir
from os.path import abspath, basename, dirname, isdir, join, splitext

def get_abspath(file):
    file_dir = abspath(file)
    return dirname(file_dir)

def list_c_files(directory):
    files = []
    for file in listdir(directory):
        if file.endswith(".c"):
            file_dir = join(directory, file)
            files.append( abspath(file_dir) )
    return files

extension_definitions = {
    './cardiovascular/tee': {'sources': ['./cardiovascular/tee.c'], 'depends': ['cardiovascular/tee.h']},
    './cardiovascular/assessment': {'sources': ['./cardiovascular/assessment.c'], 'depends': ['cardiovascular/assessment.h']},
    './cardiovascular/hr': {'sources': ['./cardiovascular/hr.c'], 'depends': ['cardiovascular/hr.h']},
    './cardiovascular/rmr': {'sources': ['./cardiovascular/rmr.c'], 'depends': ['cardiovascular/rmr.h'],},
    './cardiovascular/cardiovascular': {'sources': ['./cardiovascular/tee.c', './cardiovascular/assessment.c', './cardiovascular/hr.c', './cardiovascular/rmr.c', './cardiovascular/models/cameron.c','./cardiovascular/models/purdy.c', './cardiovascular/models/riegel.c']},

    './cardiovascular/models/cameron': {'sources': ['./cardiovascular/models/cameron.c'], 'depends': ['cardiovascular/models/cameron.h']},
    './cardiovascular/models/purdy': {'sources': ['./cardiovascular/models/purdy.c'], 'depends': ['cardiovascular/models/purdy.h']},
    './cardiovascular/models/riegel': {'sources': ['./cardiovascular/models/riegel.c'], 'depends': ['cardiovascular/models/riegel.h']},

    './flexibility/assessment': {'sources': ['./flexibility/assessment.c'], 'depends': ['flexibility/assessment.h']},
    './flexibility/flexibility': {'sources': ['./flexibility/assessment.c']},

    './composition/mass': {'sources': ['./composition/mass.c'], 'depends': ['composition/mass.h']},
    './composition/density': {'sources': ['./composition/density.c'], 'depends': ['composition/density.h']},
    './composition/surfacearea': {'sources': ['./composition/surfacearea.c'], 'depends': ['composition/surfacearea.h']},
    './composition/stature': {'sources': ['./composition/stature.c'], 'depends': ['composition/stature.h']},
    './composition/indices': {'sources': ['./composition/indices.c'], 'depends': ['composition/indices.h']},
    './composition/composition': {"sources": ['./composition/mass.c', './composition/density.c', './composition/surfacearea.c', './composition/stature.c', './composition/indices.c']},

    './balance/assessment': {'sources': ['./balance/assessment.c'], 'depends': ['balance/assessment.h']},
    './balance/balance': {'sources': ['./balance/assessment.c']},

    './strength/rm': {'sources': ['./strength/rm.c'], 'depends': ['strength/rm.h']},
    './strength/lifting': {'sources': ['./strength/lifting.c'], 'depends': ['strength/lifting.h']},
    './strength/strength': {'sources': ['./strength/rm.c', './strength/lifting.c']},

    './sport/running/jackdaniels': {'sources': ['./sport/running/jackdaniels.c'], 'depends': ['sport/running/jackdaniels.h']},
    './sport/running/pace': {'sources': ['./sport/running/pace.c'], 'depends': ['sport/running/pace.h']},
    './sport/running': {'sources': ['./sport/running/jackdaniels.c', './sport/running/pace.c', ]},
    './strength/strength': {'sources': ['./strength/rm.c', './strength/lifting.c']}
}

ext_modules = []
for name, definition in extension_definitions.iteritems():
    # create absolute path for source files
    sources = definition['sources']
    for index, file in enumerate(sources):
        definition['sources'][index] = abspath(file)
    extension = Extension(name, **definition)
    ext_modules.append(extension)

balance = Extension("./balance/balance", sources=list_c_files("./balance") )

cardio_models= Extension("./cardiovascular/models/models", sources=list_c_files("./cardiovascular/models") )
cardiovascular = Extension("./cardiovascular/cardiovascular", sources=list_c_files("./cardiovascular") )

composition = Extension("./composition/composition", sources=list_c_files("./composition") )

flexibility = Extension("./flexibility/flexibility", sources=list_c_files("./flexibility") )

strength = Extension("./strength/strength", sources=list_c_files("./strength") )

sport = Extension("./sport/sport", sources=list_c_files("./sport") )
sport_running = Extension("./sport/running/running", sources=list_c_files("./sport/running") )

packages = ["pyexphys", "balance", "cardiovascular", "cardiovascular.models", "composition","flexibility", "mets", "strength", "sport", "sport.running"]

setup(name="pyexphys_equations", version="0.1", description="A collection of exercise physiology equations", author="Doug Fenstermacher", author_email="douglas.fenstermacher@gmail.com",  packages=packages, ext_package='pyexphys.equations', ext_modules=ext_modules )
