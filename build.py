#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin
from pybuilder.core import init
from pybuilder.core import Author

use_plugin('python.core')
use_plugin('python.unittest')
use_plugin('python.flake8')
use_plugin('python.coverage')
# only enable when publishing
# requires dependent packages to be built from source on Alpine
use_plugin('python.distutils')
use_plugin('pypi:pybuilder_radon')
use_plugin('pypi:pybuilder_bandit')
use_plugin('pypi:pybuilder_anybadge')

name = 'mplogp'
authors = [Author('Emilio Reyes', 'soda480@gmail.com')]
summary = 'A log parser for parsing logs generated from multi-processing based tools.'
url = 'https://github.com/soda480/mplogp'
version = '0.1.0'
default_task = [
    'clean',
    'analyze',
    'publish',
    'radon',
    'bandit',
    'anybadge',
    'package']
license = 'Apache License, Version 2.0'
description = summary


@init
def set_properties(project):
    project.set_property('unittest_module_glob', 'test_*.py')
    project.set_property('flake8_max_line_length', 120)
    project.set_property('flake8_verbose_output', True)
    project.set_property('flake8_break_build', True)
    project.set_property('flake8_include_scripts', True)
    project.set_property('flake8_include_test_sources', True)
    project.set_property('flake8_ignore', '')
    project.build_depends_on_requirements('requirements-build.txt')
    project.depends_on_requirements('requirements.txt')
    project.set_property('distutils_console_scripts', ['mplogp = mplogp.mplogp:main'])
    project.set_property('radon_break_build_average_complexity_threshold', 4)
    project.set_property('radon_break_build_complexity_threshold', 10)
    project.set_property('bandit_break_build', True)
    project.set_property('anybadge_use_shields', True)
