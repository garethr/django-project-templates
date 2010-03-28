from paste.script.templates import Template
from paste.script.templates import var
from random import choice

class DjangoTemplate(Template):

    vars = [
    ]

    use_cheetah = True
    required_templates = []

    def check_vars(self, vars, command):
        if not command.options.no_interactive and \
           not hasattr(command, '_deleted_once'):
            del vars['package']
            command._deleted_once = True
        return super(DjangoTemplate, self).check_vars(vars, command)

def append_secret_key(vars):
    default_key = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])
    vars.append(
        var('secret_key', 'Secret key', default=default_key)
    )
    
def append_db_password(vars):
    default_key = ''.join([choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(10)])
    vars.append(
        var('db_password', 'DB Password', default=default_key)
)

class DjangoProjectTemplate(DjangoTemplate):
    _template_dir = 'templates/django_project'
    summary = 'Template for a Django project'
    
    def __init__(self, name):
        append_secret_key(self.vars)
        super(DjangoProjectTemplate, self).__init__(name)
        
class DjangoCruiseControlTemplate(Template):
    _template_dir = 'templates/django_cruisecontrol_project'
    summary = 'CruiseControl Template for a Django project'

class NewsAppsProjectTemplate(DjangoTemplate):
    _template_dir = 'templates/newsapps_project'
    summary = 'Template for a News Applications Django project'
    
    vars = [
        var('staging_domain',
            'Parent domain for your staging site.',
            default="beta.example.com"),
        var('production_domain',
            'Parent domain for your production site.',
            default="example.com"),
        var('repository_url',
            'Git repo where your project will be deployed from.',
            default="git@git.example.com:example/project_name.git"),
    ]
    
    def __init__(self, name):
        append_secret_key(self.vars)
        append_db_password(self.vars)
        super(NewsAppsProjectTemplate, self).__init__(name)
