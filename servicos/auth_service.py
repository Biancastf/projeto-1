import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)
    
from energy_guard.database.json_hadler import load_users
def autenticar_usuario(email, senha):
    users = load_users()
    for user in users:
        if user.get('email') == email and user.get('senha') == senha:
            return user
    return None
