import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from django_firebase.settings import BASE_DIR
import os
# Use a service account
thepath = os.path.join(BASE_DIR, 'django-firebase-e4a40-firebase-adminsdk-m3l3m-e303f66f5a.json')
cred = credentials.Certificate(thepath)
firebase_admin.initialize_app(cred)
db = firestore.client()
 