#!/usr/bin/env python3
"""patreon api call"""
import patreon
import requests
from config import *
import patreon
from flask import request

api_client = patreon.API(access_token)

campaign_response = api_client.fetch_campaign()
campaign_id = campaign_response.data()[0].id()

all_pledges = []
cursor = None
while True:
    pledges_response = api_client.fetch_page_of_pledges(campaign_id, 25, cursor=cursor)
    cursor = api_client.extract_cursor(pledges_response)
    all_pledges += pledges_response.data()
    if not cursor:
        break


for pledge in all_pledges:
    print(pledge.relationship('patron').attribute('first_name'))

