#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
Example use of MySql related operators.
"""
from __future__ import annotations

import os
from datetime import datetime

from airflow import DAG
from airflow.providers.mysql.operators.mysql import MySqlOperator

#ENV_ID = os.environ.get("SYSTEM_TESTS_ENV_ID")
DAG_ID = "airflow_mysql"

with DAG(
    DAG_ID,
    start_date=datetime(2021, 1, 1),
    default_args={"mysql_conn_id": "airflow_db"},
    tags=["example"],
    catchup=False,
) as dag:

    # [START howto_operator_mysql]

    delete_table_mysql_task = MySqlOperator(
        task_id="delete_table_mysql", sql=r"""delete from pet where pet_id=101 ;""", dag=dag
    )

    # [END howto_operator_mysql]

    # [START howto_operator_mysql_external_file]

    insert_table_mysql_task = MySqlOperator(
        task_id="insert_table_mysql",
        sql=r"""INSERT INTO pet VALUES ( '105','Quincy', 'Parrot', '2013-08-11', 'Anne') ;""",
        dag=dag
    )

    delete_table_mysql_task >> insert_table_mysql_task

    # [END howto_operator_mysql_external_file]




#from tests.system.utils import get_test_run  # noqa: E402

# Needed to run the example DAG with pytest (see: tests/system/README.md#run_via_pytest)
#test_run = get_test_run(dag)