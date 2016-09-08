"""
WSGI config for pkb_json project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys
import site

site.addsitedir('/opt/pikabu/lib/python2.7/site-packages')


sys.path.append('/opt/pikabu')
sys.path.append('/opt/pikabu/pkb_json')


from django.core.wsgi import get_wsgi_application




# Activate your virtual env
activate_env=os.path.expanduser('/opt/pikabu/bin/activate_this.py')
with open(activate_env) as f:
        code = compile(f.read(), activate_env, 'exec')
        exec(code, dict(__file__=activate_env))



os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pkb_json.settings")

application = get_wsgi_application()
