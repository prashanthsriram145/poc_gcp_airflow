import datetime

from airflow import models
from scipy import stats
from airflow.operators import python_operator

yesterday = datetime.datetime.combine(
    datetime.datetime.today() - datetime.timedelta(1),
    datetime.datetime.min.time()
)

default_args = {
    'start_date' : yesterday
}

with models.DAG(
    'most_common_element_scipy',
    schedule_interval=datetime.timedelta(days=1),
    default_args=default_args
) as dag:

    def most_common_element():
        num = stats.mode([9,5,2,5,1,6])
        print(num)
        return 'Most common element is printed'

    most_common_element_operator = python_operator.PythonOperator(task_id='most_common_element',
                                                                  python_callable=most_common_element)

    most_common_element_operator