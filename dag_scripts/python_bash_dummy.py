import datetime

from airflow import models
from airflow.operators import python_operator
from airflow.operators import bash_operator
from airflow.operators import dummy_operator

yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time()
)

default_args = {
    'start_date' : yesterday
}

with models.DAG(
    'running_bash_python_dummy_operators',
    schedule_interval=datetime.timedelta(days=1),
    default_args= default_args
) as dag:

    def hello_world():
        print('hello world')
        return 1

    def greeting():
        print('Greetings from spikey world')
        return 'Greetings from spikey world'

    hello_world_operator = python_operator.PythonOperator(task_id='python_1', python_callable=hello_world)

    greeting_operator = python_operator.PythonOperator(task_id='python_2', python_callable=greeting)

    bash_greeting_operator = bash_operator.BashOperator(task_id='bash_bye',
                                                        bash_command='echo bye! Hope to see you')

    dummy = dummy_operator.DummyOperator(task_id='dummy')

    hello_world_operator >> greeting_operator >> bash_greeting_operator >> dummy