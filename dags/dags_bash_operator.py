import datetime

import pendulum
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator",
    schedule_interval="0 0 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),  # 만료 시간
    tags=["example", "example_value"],
) as dag:
    # 객체명과 Task ID는 동일하게 줘야함
    bash_t1 = BashOperator(task_id="bash_t1", bash_command="echo 1")

    bash_t2 = BashOperator(task_id="bash_t2", bash_command="echo $HOSTNAME")

    bash_t1 >> bash_t2
