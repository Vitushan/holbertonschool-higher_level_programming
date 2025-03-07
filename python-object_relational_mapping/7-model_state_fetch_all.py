#!/usr/bin/python3
"""
...
"""


#!/usr/bin/python3
"""
Liste tous les objets State de la base de données hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Importation des classes nécessaires

if __name__ == "__main__":
    # 1️⃣ Connexion à la base de données MySQL avec SQLAlchemy
    engine = create_engine(f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}", pool_pre_ping=True)

    # 2️⃣ Création d'une session pour interagir avec la base de données
    Session = sessionmaker(bind=engine)
    session = Session()

    # 3️⃣ Récupération et affichage des objets State triés par id
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

    # 4️⃣ Fermeture de la session
    session.close()
