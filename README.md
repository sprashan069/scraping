To run the project go through below steps:

Step1: Install scrapy framework
pip install scrapy

step2: Go to the data_extraction folder where your spider resides
cd data_extraction\spiders\data.py

Step3: Run this command to start execution
 scrapy runspider data.py

By doing above step your data will be scraped and stored in mysql database.


step:4 If you want to store the scrape data into json file just add -o option and file name like data.json
scrapy runspider data.py -o data.json

django project
https://github.com/hackstarsj/student_management_system_part_11
