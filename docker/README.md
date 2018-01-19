# Dockerfile for running slackipy in a container

Just build the container `docker build -t my_namespace/slackipy:latest` and then run the container
`docker run -v ${PWD}/slackipy.cfg:/app/slackipy.cfg:ro -e SLACKIPY_CONFIG=/app/slackipy.cfg my_namespace/slackipy:latest`.
