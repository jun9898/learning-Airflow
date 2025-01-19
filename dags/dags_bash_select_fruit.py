import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_select_fruit",
    schedule_interval="10 0 * * 6#1",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    t1 = BashOperator(
        task_id="t1",
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh ORANGE"
    )

    t2 = BashOperator(
        task_id="t2", 
        bash_command="/opt/airflow/plugins/shell/select_fruit.sh GRAPE"
    )

    t1 >> t2
