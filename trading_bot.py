# import modules
from exchanges.bitfinex import bitfinex
import smtplib

# Function to send email
def trigger_email(msg):
	email_user = "donohue76@hotmail.com"
	email_password = ""
	smtp_server = ''
	smtp_port = 
	email_from = ""
	email_to = ""

	# login to the email server
	server = smtplib.SMTP(smtp_server, smtp_port)
	server.starttls()
	server.logins(email_user, email_password)

	# send email
	server.sendmail(email_from, email_to, msg)
	server.quit()

# define buy and sell threshholds for Bitcoin
buy_thresh = 4400
sell_thresh = 4400

# get Bitcoin prices
btc_sell_price = bitfinex().get_current_bid()
btc_buy_price = bitfinex().get_current_ask()

# Trigger Buy email if buy price is lower than threshhold
if btc_buy_price < buy_thresh:

	email_msg = """
	Bitcoin Buy Price is %s which is lower than the threshhold price of %s.
	Good time to buy!""" % (btc_buy_price, buy_thresh)

	trigger_email(email_msg)

# Trigger seel email if the sell price is higher than the threshhold
if bbtc_sell_price > sell_thresh:

	email_msg = """
	Bitcoin sell Price is %s which is higher than the threshhold price of %s.
	Good time to sell!""" % (btc_sell_price, sell_thresh)

	trigger_email(email_msg)





