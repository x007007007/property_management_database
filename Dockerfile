ARG PYPI_INDEX=https://mirrors.aliyun.com/pypi/simple/
ARG PYPI_TRUSTED_HOST=mirrors.aliyun.com
FROM python:3.9.16 as build
ARG PYPI_INDEX
ARG PYPI_TRUSTED_HOST
WORKDIR /build
RUN pip config set global.index-url ${PYPI_INDEX} \
    && pip config set global.trusted-host ${PYPI_TRUSTED_HOST} \
    && pip install "pdm==2.4.0" \
    && pdm config python.use_venv false
COPY ./pyproject.toml ./
RUN pdm install
RUN pdm export -f requirements -o ./req.txt
COPY ./ ./
RUN pdm build && ls -la

FROM python:3.9.16
RUN \
  mv /etc/apt/sources.list /etc/apt/sources.list.bk \
  && echo deb https://mirrors.aliyun.com/debian/ bullseye main non-free contrib >>/etc/apt/sources.list \
  && echo deb-src https://mirrors.aliyun.com/debian/ bullseye main non-free contrib >>/etc/apt/sources.list \
  && echo deb https://mirrors.aliyun.com/debian-security/ bullseye-security main  >>/etc/apt/sources.list \
  && echo deb-src https://mirrors.aliyun.com/debian-security/ bullseye-security main  >>/etc/apt/sources.list \
  && echo deb https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib >>/etc/apt/sources.list \
  && echo deb-src https://mirrors.aliyun.com/debian/ bullseye-updates main non-free contrib >>/etc/apt/sources.list \
  && echo deb https://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib >>/etc/apt/sources.list \
  && echo deb-src https://mirrors.aliyun.com/debian/ bullseye-backports main non-free contrib >>/etc/apt/sources.list \
  && apt-get update \
  && apt-get -y --no-install-recommends install avahi-utils \
  && apt-get clean all \
  && mv -f /etc/apt/sources.list.bk /etc/apt/sources.list
ARG PYPI_INDEX
ARG PYPI_TRUSTED_HOST
RUN pip config set global.index-url ${PYPI_INDEX} \
    && pip config set global.trusted-host ${PYPI_TRUSTED_HOST} \
    && /usr/local/bin/python -m pip install --upgrade pip
WORKDIR /opt/pmdb
#COPY --from=build /build/req.txt ./
#RUN #pip install -r ./req.txt
COPY --from=build /build/dist/* ./
RUN pip install ./property_manage_database-0.0.1-py3-none-any.whl
ENV DJANGO_SETTINGS_MODULE=property_management_database.settings.docker_settings \
    SECRET_KEY= \
    PORTAL_HOST=

VOLUME ["/data"]
CMD ["python", "-m", "property_management_database", "runserver", "0.0.0.0:80"]
