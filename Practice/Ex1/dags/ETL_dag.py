from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from extract import extract
from transform import transform
from load import load


dag = DAG(
    dag_id='ETL_dag',
    default_args={
        'start_date': days_ago(1),
    },
    schedule_interval='*/2 * * * *',
    catchup=False
)

extract = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag
)

transform = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag,
)

load = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag
)

extract >> transform >> load
# transform >> [load, load_2] # parallel