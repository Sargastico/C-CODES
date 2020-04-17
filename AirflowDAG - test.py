from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from airflow.operators.python_operator import BranchPythonOperator
from datetime import timedelta, datetime
import time

# DAG args set

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(2),
    # 'email': ['airflow@example.com'],
    # 'email_on_failure': False,
    # 'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}

# Test variables
run_id = 12
number_of_files = 6
missing_files = ['arquivo1', 'arquivo2', 'arquivo3']


def upload_files():
    print("Files uploaded")


def is_file_enought(**kwargs):

    if number_of_files <= 10:  # Dummy check
        task_instance = kwargs['ti']
        m_files = task_instance.xcom_pull(key=('missing_files ' + str(run_id)))
        return 'table_of_missing_files'

    else:
        return 'processing_report_data'


def table_of_missing_files(**kwargs):

    task_instance = kwargs['ti']
    task_instance.xcom_push(key=('missing files ' + str(run_id)), value=missing_files)

    # Código para rodar a verificação dos arquivos novamente (com o mesmo run id)


def report_process():
    print("PROCESSANDO DADOS")
    print("PROCESSAMENTO TERMINADO")


def report_deploy():
    print("RELATORIO DE X, Y, Z")


# Main DAG code

with DAG('test_DAG', start_date=datetime(2020, 4, 14), schedule_interval='@once', default_args=default_args,
         catchup=False) as dag:
    files_upload = PythonOperator(task_id='files_upload', python_callable=upload_files)

    checking_number_of_files = BranchPythonOperator(task_id='checking_number_of_files', python_callable=is_file_enought, provide_context=True)

    processing_report_data = PythonOperator(task_id='processing_report_data', python_callable=report_process)

    report_deployment = PythonOperator(task_id='report_deployment', python_callable=report_deploy)

    table_of_missing_files = BranchPythonOperator(task_id='table_of_missing_files', python_callable=table_of_missing_files, provide_context=True)

    upload_retry = DummyOperator(task_id='upload_retry')

    files_upload >> checking_number_of_files >> processing_report_data >> report_deployment
    files_upload >> checking_number_of_files >> table_of_missing_files >> upload_retry >> processing_report_data
