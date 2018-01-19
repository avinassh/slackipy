FROM alpine:3.5

MAINTAINER "Andrej Rode <mail@andrejro.de>"

ENV security_updates_as_of 2018-01-19

RUN \
    apk add --no-cache \
    dumb-init \
    git \
    python3

RUN \
    pip3 install \
    Flask \
    Flask-WTF \
    gunicorn \
    git+https://github.com/avinassh/slackipycore.git \
    git+https://github.com/noc0lour/slackipy.git

ENTRYPOINT ["dumb-init"]

CMD ["/usr/bin/gunicorn", "slackipy:app","-b 0.0.0.0:5000"]
