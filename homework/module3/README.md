1. SELECT COUNT(1) FROM `extended-web-448520-b2.example_dataset.yellow_taxi_jan_jun`.   20339093
2. SELECT DISTINCT PULocationID FROM example_dataset.yellow_regular;
	1. 0, 155.12 
3. - BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.
4. SELECT COUNT(1), FROM `example_dataset.yellow_regular` where fare_amount=0 -> 8333
5. ```CREATE OR REPLACE TABLE example_dataset.partitioned2PARTITION BY
DATE(tpep_dropoff_datetime)
CLUSTER BY VendorID AS
SELECT * FROM example_dataset.yellow_taxi_jan_jun;```
partition on tpep_dropoff_datetime cluster by VendorID. filter will only get partition of specifi datetime, clustering will have the sort ready already
6. - 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table
7. - GCP Bucket
8. False