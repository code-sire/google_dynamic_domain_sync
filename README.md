Google Dynamic Domain Updater

1. Update the Python script with your domain credentials
2. Place the Python script in `/usr/local/bin`
3. Add the line below to your Cron Jobs

```
*/5 * * * * /usr/bin/python3 /usr/local/bin/Google_Dynamic_Domain_Updater.py

```
