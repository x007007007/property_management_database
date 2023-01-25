FROM python:3.9.16-alpine3.17 as build
WORKDIR /build
RUN pip config set global.index-url=http://mirrors.aliyun.com/pypi/simple/ && pip install "pdm==2.4.0"
RUN pdm install && pdm build
RUN python setup.py build

FROM python:3.9.16-alpine3.17
WORKDIR /opt/pmdb
COPY --from=build /build/dist/property_manage_database-0.0.1-py3-none-any.whl ./
RUN pip install ./property_manage_database-0.0.1-py3-none-any.whl
ENV DJANGO_SETTINGS_MODULE=property_management_database.settings.docker_settings \
    SECRET_KEY= \
    PORTAL_HOST=

CMD python -m property_management_database runserve
