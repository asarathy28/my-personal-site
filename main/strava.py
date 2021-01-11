import stravalib

STRAVA_CLIENT_ID = '55892'
STRAVA_CLIENT_SECRET = '20e4c1013a9dee4c9a1f5805a67fd0f977021ca4'
REFRESH_TOKEN = '0a8ddc3be42267e0c059f1c6f48f0125aeb72a5c'


def auth_url(scope=''):
    """
    Creates a URL that you can paste into your broswer and accept the permissions request

    the scope can be any of (or multiple, separated by a comma): activity:read, activity:read_all, activity:write (check the Strava docs on these values)
    """
    client = stravalib.Client()
    redirect_uri = 'https://localhost:8000/strava_authentication'
    auth_url = client.authorization_url(client_id = STRAVA_CLIENT_ID,
                                        redirect_uri=redirect_uri,
                                        approval_prompt='force',
                                        scope= 'activity:read_all')
    print(auth_url)
    return auth_url

def refresh_token():
    """
    After the timestamp in your athlete codes passes, you'll need a new authentication token. The codes given in your API settings on strava.com should actually be permanent though.

    refresh_token is the refresh_token given to you the last time you authenticated.
    """

    client = stravalib.Client()
    refresh = client.refresh_access_token(client_id=STRAVA_CLIENT_ID, client_secret=STRAVA_CLIENT_SECRET, refresh_token=REFRESH_TOKEN)

    new_codes = {
        'access_token': refresh['access_token'],
        'refresh_token': refresh['refresh_token'],
        'expires_at': refresh['expires_at']}
    #print(new_codes)
    return refresh['access_token']

def get_athlete_info():
    """
    Returns a stravalib athlete object containing Strava info about the athlete
    The authentication token in athlete_codes identifies the right athlete to return
    """
    access_token = refresh_token()
    client = stravalib.Client(access_token)
    athlete = client.get_athlete()
    return athlete


def get_a_bunch_of_activities():
    access_token = refresh_token()
    client = stravalib.Client(access_token)

    activities = client.get_activities(limit=100)#(after="2020-01-01") # this will get a list of non-detailed activity data.
    #for a in activities
        #activity_ids = [a.id] # extract all the activity IDs for example
    sample = list(activities)[0]
    sample.to_dict()
    return activities

def get_activity_details(activity_id):
    """
    Unlike the funciton above, returns super detailed info about one activity, since we can't get all this info in bulk
    """

    access_token = refresh_token()
    client = stravalib.Client(access_token)

    activity = client.get_activity(activity_id=activity_id) # gets a much more detaild version

    # Or, we can get stream data (an array of values by distance or time)
    types = ['time', 'latlng', 'altitude', 'heartrate', 'temp', ]
    streams = client.get_activity_streams(activity_id, types=types, resolution='medium')

    return activity, streams



def main():
    auth_url()
    #print(get_athlete_info())
    #print(get_a_bunch_of_activities())


main()
