# Base Image
FROM puckel/docker-airflow
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV AIRFLOW_HOME=/usr/local/airflow
WORKDIR $AIRFLOW_HOME
COPY ./start-airflow.sh $AIRFLOW_HOME/start-airflow.sh
COPY ./airflow.cfg $AIRFLOW_HOME/airflow.cfg
USER root
RUN chmod +x $AIRFLOW_HOME/start-airflow.sh
RUN chown -R airflow:airflow $AIRFLOW_HOME
USER airflow
CMD [ "./start-airflow.sh" ]
