#!/usr/bin/env python3
"""patreon api call"""
import patreon
import requests
from config import *
import patreon
from flask import request
api_client = patreon.API(access_token)

# https://www.patreon.com/oauth2/authorize?response_type=code&client_id=HParCfn-rlHB062fNr3r6MWrfdiZrtHhYppqcrnw63AfcOZH-cv2Rt0rIves-dRC&redirect_uri=https://www.mysite.com/custom-uri&state=their_session_id
response_api = requests.get("https://www.patreon.com/oaut2/authorize?response_type=code&client_id=HParCfn-rlHB062fNr3r6MWrfdiZrtHhYppqcrnw63AfcOZH-cv2Rt0rIves-dRC&redirect_uri=https://www.mysite.com/custom-uri&state=their_session_id")
# campaign_response = api_client.fetch_campaign()
# campaign_id = campaign_response.data()[0].id()
print(response_api)
# print(response_api)
all_pledges = []
# print(campaign_response)
# cursor = None
# while True:
#    pledges_response = api_client.fetch_page_of_pledges(campaign_id, 25, cursor=cursor)
#    cursor = api_client.extract_cursor(pledges_response)
   
#    all_pledges += pledges_response.data()
#    print(pledges_response.data())
#    if not cursor:
#        break

print(all_pledges)