--database test
--schema air_ds
--user db_owner
--GRANT ALL PRIVILEGES ON SCHEMA public TO db_owner;
---sql_alchemy_conn = postgresql+psycopg2://airflow:airflow@localhost:5432/airflow
--airflow db init
CREATE TABLE IF NOT EXISTS air_ds.pet (
            pet_id SERIAL PRIMARY KEY,
            name VARCHAR NOT NULL,
            pet_type VARCHAR NOT NULL,
            birth_date DATE NOT NULL,
            OWNER VARCHAR NOT NULL)


INSERT INTO air_ds.pet1 VALUES ( '101','Max', 'Dog', '2018-07-05', 'Jane');
INSERT INTO air_ds.pet1 VALUES ( '103','Susie', 'Cat', '2019-05-01', 'Phil');
INSERT INTO air_ds.pet1 VALUES ( '102','Lester', 'Hamster', '2020-06-23', 'Lily');
INSERT INTO air_ds.pet1 VALUES ( '105','Quincy', 'Parrot', '2013-08-11', 'Anne');


CREATE TABLE test_pet (
  pet_id int ,
  name char(20) ,
  pet_type char(20) ,
  birth_date date ,
  OWNER char(20)
)
INSERT INTO pet VALUES ( '101','Max', 'Dog', '2018-07-05', 'Jane');
INSERT INTO pet VALUES ( '103','Susie', 'Cat', '2019-05-01', 'Phil');
INSERT INTO pet VALUES ( '102','Lester', 'Hamster', '2020-06-23', 'Lily');
INSERT INTO pet VALUES ( '105','Quincy', 'Parrot', '2013-08-11', 'Anne');