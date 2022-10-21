# notes
'''
This file is used for handling anything image related.
I suggest handling the local file encoding/decoding here as well as fetching any external images.
'''

# package imports
import base64
import os



# logo information
cwd = os.getcwd()
logo_path = 'C:\\Users\\niklas\\PSI\\Dashboard\\dashboard\\dashboard\\assets\\logos\\logo_main.png'
logo_tunel = base64.b64encode(open(logo_path, 'rb').read())
logo_encoded = 'data:image/png;base64,{}'.format(logo_tunel.decode())


