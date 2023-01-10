
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./requirements.txt /code/requirements.txt
COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x entrypoint.sh
# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY  . /app

ENV PORT=8080

ENTRYPOINT ["sh", "entrypoint.sh"]
# 
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT}"]

# FROM tiangolo/uvicorn-gunicorn-fastapi:latest


# RUN pip install --upgrade pip

# COPY entrypoint.sh ./entrypoint.sh
# RUN chmod +x entrypoint.sh

# ARG poetry_version="master"
# # install-poetry.py and get-poetry.py are options; but get-poetry.py is deprecated though!
# ARG poetry_script_name="install-poetry.py"
# ARG debug_poetry="true"
# ENV PATH="/opt/poetry/bin:${PATH}"
# # Install Poetry
# RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/${poetry_version}/${poetry_script_name} | POETRY_HOME=/opt/poetry python && \
#     cd /usr/local/bin && \
#     ln -s /opt/poetry/bin/poetry && poetry config virtualenvs.create false && poetry config virtualenvs.in-project false && poetry config experimental.new-installer false

# RUN if [ ${debug_poetry} = "true" ] ; then echo $debug_poetry && apt-get update && apt-get install -y tree && cd /opt && tree -la . ; fi

# # Copy using poetry.lock* in case it doesn't exist yet
# COPY ./pyproject.toml ./poetry.lock* /app/
# WORKDIR /app/

# # If using get-poetry.py - /opt/poetry/env instead of /opt/poetry/venv
# RUN if [ ${poetry_script_name} = "get-poetry.py" ]; then which python && . /opt/poetry/env && poetry install --no-root --no-dev && poetry env info ; fi

# # If using install-poetry.py - /opt/poetry/venv instead of /opt/poetry/env
# RUN if [ ${debug_poetry} = "true" ] ; then echo $debug_poetry && apt-get update && apt-get install -y tree && cd /usr/local/bin && tree -la . ; fi

# RUN if [ ${poetry_script_name} = "install-poetry.py" ]; then poetry export -f requirements.txt --output requirements.txt && pip install --no-cache-dir -r requirements.txt ; fi


# # Final copy
# COPY . /app
# # RUN ./cloud-sql-proxy --credentials-file key.json ceri-m1-ecommerce-2022:europe-west1:mysql-primary


# RUN pytest /app/tests/test_utils.py
