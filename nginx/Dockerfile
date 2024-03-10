FROM nginx
COPY nginx.conf /etc/nginx/nginx.conf
COPY templates /etc/nginx/templates
RUN rm /etc/nginx/conf.d/default.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
