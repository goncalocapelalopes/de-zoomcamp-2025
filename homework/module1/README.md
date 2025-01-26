1.
docker run -it --entrypoint bash python:3.12.8
pip --version
24.3.1

2.
postgres:5432
db:5432

3.
```
WITH subset AS (
    SELECT *
    FROM green_taxi_data
    WHERE lpep_pickup_datetime >= TO_DATE('01/10/2019', 'DD/MM/YYYY') and lpep_dropoff_datetime < TO_DATE('01/11/2019', 'DD/MM/YYYY')
)
SELECT count(*) from subset where  trip_distance > 10;-- and trip_distance <= 10;
```
- 104,802; 198,924; 109,603; 27,678; 35,189
4.
```
SELECT EXTRACT(DAY FROM lpep_pickup_datetime) as day, max(trip_distance)
FROM green_taxi_data 
group by day
order by max(trip_distance) desc;
```
31

5.

```
select "Zone", sum(total_amount)
from green_taxi_data join zones on green_taxi_data."PULocationID"=zones."LocationID"
where lpep_pickup_datetime > TO_DATE('18/10/2019', 'DD/MM/YYYY') and lpep_pickup_datetime < TO_DATE('19/10/2019', 'DD/MM/YYYY')
group by "Zone"
having sum(total_amount) > 13000 
```
- East Harlem North, East Harlem South, Morningside Heights
6.
```
SELECT dropoffzone."Zone", MAX(t1."tip_amount") as max_tip
FROM green_taxi_data t1
JOIN zones AS pickupzone ON t1."PULocationID" = pickupzone."LocationID"
JOIN zones AS dropoffzone ON t1."DOLocationID" = dropoffzone."LocationID"
WHERE t1."lpep_pickup_datetime" > TO_DATE('01/10/2019', 'DD/MM/YYYY') 
AND t1."lpep_pickup_datetime" < TO_DATE('01/11/2019', 'DD/MM/YYYY') 
AND pickupzone."Zone" = 'East Harlem North'
GROUP BY dropoffzone."Zone"
ORDER BY max_tip DESC;
```
JFK Airport

7.
- terraform init, terraform apply -auto-approve, terraform destroy