import stravalib

STRAVA_CLIENT_ID = '55892'
STRAVA_CLIENT_SECRET = '0e4c1013a9dee4c9a1f5805a67fd0f977021ca4'
#refresh_token = 0a8ddc3be42267e0c059f1c6f48f0125aeb72a5c



codes = {
    'access_token': refresh['access_token'],
    'refresh_token': refresh['refresh_token'],
    'expires_at': refresh['expires_at']}


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

def refresh_token(refresh_token):
    """
    After the timestamp in your athlete codes passes, you'll need a new authentication token. The codes given in your API settings on strava.com should actually be permanent though.

    refresh_token is the refresh_token given to you the last time you authenticated.
    """

    client = stravalib.Client()
    refresh = client.refresh_access_token(STRAVA_CLIENT_ID, STRAVA_CLIENT_SECRET, refresh_token)

    new_codes = {
        'access_token': refresh['access_token'],
        'refresh_token': refresh['refresh_token'],
        'expires_at': refresh['expires_at']}
    print(new_codes)

    return new_codes

def get_athlete_info(athlete_codes):
    """
    Returns a stravalib athlete object containing Strava info about the athlete
    The authentication token in athlete_codes identifies the right athlete to return
    """

    client = stravalib.Client(access_token=athlete_codes['access_token'])
    athlete = client.get_athlete()
    return athlete

auth_url()
refresh_token(0a8ddc3be42267e0c059f1c6f48f0125aeb72a5c)
#print(get_athlete_info(54197197))
