Google Dynamic Domain Updater

Step 1 - Update the Python script with your domain credentials
Step 2 - Place the Python script in `/usr/local/bin`
Step 3 - Add the line below to your Cron Jobs

```
*/5 * * * * /usr/bin/python3 /usr/local/bin/Google_Dynamic_Domain_Updater.py

```
