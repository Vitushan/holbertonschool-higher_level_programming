

- `curl URL` → Fait une requête GET (par défaut)
- `curl -I URL` → Affiche uniquement les **en-têtes**
- `curl -X POST -d "data=..." URL` → Fait une requête **POST** avec données
- `curl -H "Header: value"` → Ajoute un en-tête HTTP
- `curl URL -o fichier.txt` → Enregistre la réponse dans un fichier