
# 🧭 Part 4 - Simple Web Client

Bienvenue dans la quatrième phase du projet **HBnB** ! Cette partie se concentre sur le **développement frontend** d'une interface utilisateur dynamique en utilisant **HTML5, CSS3 et JavaScript (ES6)**, pour interagir avec les services backend développés précédemment.

---

## 🎯 Objectifs

- Concevoir une interface utilisateur conviviale selon les spécifications données.
- Implémenter la communication avec l’API backend via JavaScript.
- Gérer les sessions utilisateur de manière sécurisée avec JWT.
- Appliquer les bonnes pratiques de développement web moderne.

---

## 📚 Compétences acquises

- Utilisation de HTML5 sémantique et de CSS3 responsive.
- Interrogation de l'API via Fetch API (AJAX).
- Authentification avec stockage de tokens JWT dans les cookies.
- Manipulation du DOM pour un rendu dynamique sans rechargement de page.

---

## 🧩 Structure du projet

### Pages implémentées :

- `login.html` – Page de connexion.
- `index.html` – Liste des lieux disponibles.
- `place.html` – Détails d’un lieu spécifique.
- `add_review.html` – Formulaire d’ajout d’un avis.

---

## ✅ Tâches réalisées

### 1. 🎨 Design

- 📂 Utilisation des fichiers `HTML` et `CSS` fournis (`styles.css`).
- 📄 Chaque page respecte les spécifications visuelles :
  - **Cartes de lieux** (`.place-card`)
  - **Détails** (`.place-details`)
  - **Avis** (`.review-card`)
  - **Formulaires** (`form` avec `.btn`)

### 2. 🔐 Login

- 📌 Connexion via `/api/v1/auth/login/`.
- ✅ Enregistrement du token JWT dans un cookie.
- ↪️ Redirection vers `index.html` si succès.
- ⚠️ Affichage d’un message d’erreur si échec.

### 3. 📍 Liste des lieux (Index)

- 📥 Récupération des lieux via `/api/v1/places/`.
- 🔍 Filtrage dynamique des lieux par prix.
- 👁️ Affichage conditionnel du bouton Login selon l’authentification.

### 4. 🧾 Détails d’un lieu

- 📄 Récupération d’un lieu via son ID depuis l’URL.
- 💬 Affichage de ses détails + ses équipements + ses avis.
- ✍️ Affichage du bouton "Add Review" si authentifié.

### 5. 📝 Ajout d’un avis

- ✅ Accès uniquement pour les utilisateurs connectés.
- 📨 Envoi des données via POST à `/api/v1/reviews/`.
- ✅ Affichage d’un message de succès ou d’échec.
- 🚫 Redirection vers `index.html` si non connecté.

---

## 🛡️ Sécurité & CORS

- CORS activé dans `run.py` via :
  ```python
  CORS(app, origins=['http://127.0.0.1:5500'], supports_credentials=True)
  ```
- ✅ Les appels `Fetch` incluent le token dans l’en-tête `Authorization` :
  ```js
  headers: {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + token
  }
  ```

---

## 🧪 Tests réalisés

- ✔ Connexion avec des identifiants valides/invalides.
- ✔ Redirection si token manquant.
- ✔ Affichage dynamique des données.
- ✔ Soumission d'avis uniquement en tant qu'utilisateur connecté.
- ✔ Validation responsive (mobile/desktop).

---

## 🚀 Lancer le projet

1. 📦 Lancer le backend avec `run.py`
2. 🌐 Ouvrir `index.html` via un serveur local (ex. Live Server dans VS Code)
3. 🎉 Profiter de l’expérience utilisateur interactive

---

## 📁 Technologies

- **Frontend** : HTML5, CSS3, JavaScript ES6
- **Backend** : Flask, JWT, SQLAlchemy
- **API** : RESTful avec Flask-RESTx

---

## 🧠 Ressources utiles

- [HTML5 Guide](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)
- [CSS3 Guide](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [JavaScript ES6](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
- [CORS in Flask](https://flask-cors.readthedocs.io/en/latest/)

---

## Author


 **Alexis Battistoni** → https://github.com/Albat93


