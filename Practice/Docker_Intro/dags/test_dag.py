from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
import datetime

now = datetime.datetime.now()

def print_time():
    TEXT_FILE_NAME = str(now.strftime('%m-%d-%Y_%H-%M-%S')) + '.txt'
    f = open('test_folder/' + TEXT_FILE_NAME, 'w+')
    f.write('1234')
    f.close()
    print(TEXT_FILE_NAME)


dag = DAG(
    dag_id='test_dag',
    default_args={
        'start_date': days_ago(1),
    },
    schedule_interval='*/2 * * * *',
    catchup=False
)

print_task_1 = PythonOperator(
    task_id='extract',
    python_callable=print_time,
    dag=dag
)

print_task_2 = PythonOperator(
    task_id='transform',
    python_callable=print_time,
    dag=dag,
)

print_task_1 >> print_task_2
