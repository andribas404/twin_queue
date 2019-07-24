#!/bin/sh
if [ ! -z "${DEBUG}" ]
then
    echo "DEBUG is set"
    if [ ! -z "${NOTEBOOK}" ]
    then
        NOTEBOOK_CONFIG=/root/.jupyter/jupyter_notebook_config.py
        if [ ! -f ${NOTEBOOK_CONFIG} ]
        then
            jupyter notebook --generate-config
            echo $(python /opt/app/docker/bin/passwd.py) >> ${NOTEBOOK_CONFIG}
        fi
    fi
else
    echo "DEBUG not set"
fi
exec "$@";