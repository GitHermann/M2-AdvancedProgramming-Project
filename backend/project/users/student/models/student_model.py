import bcrypt

from project.app import app, database_client

students_collection = database_client["Project"]["students"]


class Student:
    @staticmethod
    def create_student(data):

        existing_user = students_collection.find_one({'nom_utilisateur': data['nom_utilisateur']})
        if existing_user:
            return {'message': 'Nom d\'utilisateur déjà utilisé'}, 400

        hashed_password = bcrypt.hashpw(data['mot_de_passe'].encode('utf-8'), bcrypt.gensalt())
        nouvel_utilisateur = {
            'nom_utilisateur': data['nom_utilisateur'],
            'adresse_email': data['adresse_email'],
            'mot_de_passe': hashed_password
        }
        students_collection.insert_one(nouvel_utilisateur)
        return {'message': 'Inscription réussie'}
