import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore import Client


class FirebaseService:
    @staticmethod
    def connect():
        cred = credentials.Certificate("firebase-connection.json")
        firebase_admin.initialize_app(cred)
        return firestore.client()

    @staticmethod
    def disconnect():
        firestore.client().close()

    @staticmethod
    def add_system(connection: Client, system_name: str):
        doc_ref = connection.collection("systems").document(system_name)
        doc_ref.set({"name": system_name})
