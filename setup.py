from setuptools import setup, find_packages
import os

setup(
    name='django-project-templates',
    version = "0.4",
    description="Paster templates for creating Django applications",
    author='Gareth Rushgrove',
    author_email='gareth@morethanseven.net',
    url='http://github.com/garethr/django-project-templates/',
    packages = find_packages('src'),
    package_dir = {'':'src'},
    license = "MIT",
    keywords = "django paster",
    install_requires=[
        'setuptools',
        'PasteScript>=1.3',
        'Cheetah',
        'fabric',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points="""
        [paste.paster_create_template]
        django_project=django_project_templates.pastertemplates:DjangoProjectTemplate
    """,
    classifiers = [
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)