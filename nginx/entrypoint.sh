#!/bin/sh
envsubst '$ADMIN_HOST' < /etc/nginx/templates/admin_panel.conf.template > /etc/nginx/conf.d/admin_panel.conf
exec nginx-debug -g 'daemon off;'
