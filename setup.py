from setuptools import setup, find_packages
import os

setup(
    name='django_project_templates',
    description="Paster templates for creating Django applications as eggs",
    author='Gareth Rushgrove',
    author_email='gareth@morethanseven.net',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    install_requires=[
        'setuptools',
        'PasteScript>=1.3',
        'Cheetah',
    ],
    entry_points="""
        [paste.paster_create_template]
        django_project=django_project_templates.pastertemplates:DjangoProjectTemplate
    """,
)