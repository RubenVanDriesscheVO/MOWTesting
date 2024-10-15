import API_Handling as ah

#inloggen op API
tokens = ah.get_token("config.ini")
refresh_token = tokens['refresh_token']
access_token = tokens['access_token']
expiry_token = tokens['expires_in']


ah.send_representation(access_token, r'47644ac42d2e4b02a54ba89ff0540c2e10818f30f14747a6b8a077ac781864b1', r"C:\Users\Ruben\Downloads\Assembly Instruction - malm-bed-frame-black-brown__AA-2558683-1-100.pdf" )
