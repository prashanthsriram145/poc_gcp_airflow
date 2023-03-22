import datetime
import random

from airflow import models
from airflow.operators import python_operator
from airflow.operators import bash_operator, dummy_operator, branch_operator

yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time()
)

default_args = {
    'start_date' : yesterday
}

with models.DAG(
    'branching_python_operator',
    schedule_interval=datetime.timedelta(days=1),
    default_args=default_args
) as dag:

    def greeting():
        print('Hello from spikey developers')
        return 'Hello, from spikey developers'

    def branch():
        val = random.randint(1,5)
        if val <= 2:
            return 'dummy_branch'
        else:
            return 'spikey_sales_operator'

    dummy_start = dummy_operator.DummyOperator(task_id='dummy_start')

    branching = python_operator.BranchPythonOperator(task_id='branching_operator',
                                                     python_callable=branch)

    dummy_start >> branching

    spikey_sales_operator = python_operator.PythonOperator(task_id='spikey_sales_operator',
                                                           python_callable=greeting)

    dummy_branch = dummy_operator.DummyOperator(task_id='dummy_branch')

    def bye_merge():
        print('Bye, from spikey developers')

    bye_merge_operator = python_operator.PythonOperator(task_id='bye_merge_operator',
                                                        python_callable=bye_merge,
                                                        trigger_rule='one_success')

    branching >> spikey_sales_operator >> bye_merge_operator
    branching >> dummy_branch >> bye_merge_operator