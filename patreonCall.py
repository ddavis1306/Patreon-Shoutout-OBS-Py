#!/usr/bin/env python3
"""patreon api call"""
import patreon
import requests
from config import *
import patreon
from flask import request
#auth patreon api
from flask import Flask, render_template



api_client = patreon.API(access_token)

campaign_response = api_client.fetch_campaign()
campaign_id = campaign_response.data()[0].id()

all_pledges = []
#cursor None forces api to look through multiple pages of patrons
cursor = None
#filters pledges that have active ccd and the amout they pledged
while True:
    pledges_response = api_client.fetch_page_of_pledges(campaign_id,
     25, 
     cursor=cursor,
     fields= {'pledge': ['total_historical_amount_cents' , 'declined_since']}
     )

    cursor = api_client.extract_cursor(pledges_response)
    all_pledges += pledges_response.data()
    if not cursor:
        break

pledges_info = []

for pledge in all_pledges:
    declined = pledge.attribute('declined_since')
    reward_tier = 0
#sorts the reward teir of patrons
    if pledge.relationships()['reward']['data']:
        reward_tier = pledge.relationship('reward').attribute('amount_cents')

    if not declined and reward_tier >= 100:
        pledges_info.append({
            'first_name': pledge.relationship('patron').attribute('first_name'),
            'total_historical_amount_cents': pledge.attribute('total_historical_amount_cents')
        }) 

sorted_pledges = sorted(
    pledges_info,
    key=lambda pledge: pledge['total_historical_amount_cents'],
    reverse=True
)

pledge_names = [pledge['first_name'] for pledge in sorted_pledges]
print (pledge_names)
# pledge_list = ', '.join(pledge_names)
# print(pledge_list)
app = Flask(__name__)

@app.route('/')
def hello_world():
    # return pledge_list
    return render_template('home.html', pledge_names=pledge_names)
if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0" ,port=80)
#prints names of patrons
# for pledge in pledges_info:
#     print(pledge['first_name'])