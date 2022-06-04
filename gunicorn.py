command = "/home/www/code/FominFishing/env/bin/gunicorn"
pythonpath = "/home/dgolov/code/FominFishing"
bind = "127.0.0.1:8001"
workers = 3
user = "dgolov"
limit_request_fields = 32000
limit_request_field_size = 0
rav_env = "DJANGO_STTINGS_MODULE=FominFishing.settings"