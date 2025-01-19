import pendulum
from airflow import DAG
from airflow.operators.email import EmailOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_email_operator",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    t1 = EmptyOperator(task_id="t1")

    send_email_task = EmailOperator(
        task_id="send_email_task",
        to="nice1998@gmail.com",
        subject="Airflow 테스트 메일",
        html_content="Airflow 테스트 메일 내용입니다.",
    )

    t1 >> send_email_task

