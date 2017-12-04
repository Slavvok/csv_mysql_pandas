# csv_mysql_pandas

How to work with the scripts:
1. Create new mysql schema.
2. Open anomalybd.sql and execute it in order to create 'main' table
3. Use metric_creation.py to create metrics for csv file. 
   You can start code either by clicking on file, or by running it in your IDE.
4. Use anomaly_detection.py to find anomalies in data.
5. After executing scripts, user can easily access data in IDE console by typing >>> df. 

Anomaly_detection.py also replaces old data with the new one.

Some issue may occur: I have some charset mismatch mithin my system. So when I'm starting to transfer data to mysql db, 
sqlalchemy plugin shows warning. But script works. I will try to solve this problem. Write if you have the same trouble.

I also should note, that I changed csv file, adding 'num' as column label. There is aditional number after timestamp. 
I guess that it could be the part of a timestamp. But I made script without considering this data part.
Please notify me if I'm wrong. 

I'm waiting for your feedback. Please, answer, regardless of your decision. 

Sincerely, Svyatoslav.
