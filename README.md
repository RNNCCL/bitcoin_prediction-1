# bitcoin_prediction

This project deals with the real time prediction of bitcoin prices. 

It accesses data from a website named blockchain.info through an API. The accessed data is then pushed into MongoDB instance. 
This pulling of data from the website is done everyday through a cron job. 

And then, a machine learning algorithm is run on the data saved in DB, to create a prediction model.
Finally, the results will are shown on a web server. 

