FROM python:3.9.16 as build
WORKDIR /build
RUN pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/ && pip install "pdm==2.4.0"
RUN pdm config python.use_venv false
COPY ./pyproject.toml ./
RUN pdm install
RUN pdm export -f requirements -o ./req.txt
COPY ./ ./
RUN pdm build && ls -la

FROM python:3.9.16
RUN pip config set global.index-url http://devpi.home.x007007007.info/root/pypi/+simple/ \
    && pip config set global.trusted-host devpi.home.x007007007.info
RUN apt-get update && apt-get -y --no-install-recommends install avahi-utils && apt-get clean all
RUN /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /opt/pmdb
#COPY --from=build /build/req.txt ./
#RUN #pip install -r ./req.txt
COPY --from=build /build/dist/* ./
RUN pip install ./property_manage_database-0.0.1-py3-none-any.whl
ENV DJANGO_SETTINGS_MODULE=property_management_database.settings.docker_settings \
    SECRET_KEY= \
    PORTAL_HOST=

CMD ["python", "-m", "property_management_database", "runserver", "0.0.0.0:80"]
