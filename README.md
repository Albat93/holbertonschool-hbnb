
# 🏠 HBnB - Clone simplifié d’Airbnb

HBnB est une application web complète inspirée d’Airbnb permettant aux utilisateurs de publier, consulter et gérer des lieux, des avis et des commodités. Elle repose sur une architecture RESTful développée avec Flask, accompagnée d'une interface utilisateur responsive.

---

## 🧩 Fonctionnalités

### 🔐 Authentification & Sécurité
- Connexion avec génération de tokens JWT (access + refresh)
- Blacklist des tokens pour le logout sécurisé
- Rôles utilisateur / admin
- Propriétaire ou admin requis pour certaines actions (delete, update)

### 👥 Utilisateurs
- Inscription avec option de promotion à admin via un `admin_secret`
- Lecture, modification et suppression de compte
- Listing admin-only des utilisateurs

### 🏡 Lieux (Places)
- Création de lieux avec titre, description, prix, coordonnées
- Association possible de commodités à un lieu
- Validation des données serveur-side
- Listing filtré côté client par prix

### 🧰 Commodités (Amenities)
- CRUD disponible
- Ajout libre, suppression restreinte (admin ou propriétaire)

### 🌟 Avis (Reviews)
- Ajout de notes et commentaires sur un lieu
- Visibles publiquement, authentification requise pour poster

---

## 🗂️ Architecture du projet

```
.
├── run.py                      # Point d'entrée Flask
├── config.py                   # Configuration Flask/JWT
├── requirements.txt            # Dépendances Python
├── app/
│   ├── __init__.py             # Création de l'app + registration API
│   ├── services/
│   │   └── facade.py           # Façade unifiée pour toutes les opérations métier
│   ├── api/v1/
│       ├── users.py            # Routes utilisateurs
│       ├── auth.py             # Authentification JWT
│       ├── admin.py            # Fonctions d'administration
│       ├── amenities.py        # Gestion des commodités
│       ├── places.py           # (non fourni, mais attendu)
│       ├── reviews.py          # (non fourni, mais attendu)
├── templates/
│   ├── index.html              # Liste des lieux
│   ├── login.html              # Connexion
│   ├── place.html              # Détails d’un lieu
│   ├── add_review.html         # Formulaire d’ajout d’avis
├── static/
│   ├── styles.css              # Design responsive
│   ├── scripts.js              # Comportement dynamique JS
│   └── images/                 # Icônes et logo
```

---

## 🧪 Installation et lancement

### 📦 Prérequis
- Python 3.8+
- pip

### ⚙️ Installation
```bash
pip install -r requirements.txt
```

### ▶️ Lancement
```bash
python run.py
```

Accessible ensuite via `http://127.0.0.1:5000`.

---

## 🌐 Interface utilisateur

### 🖼 Pages fournies
| Page               | Description                            |
|--------------------|----------------------------------------|
| `index.html`       | Liste de lieux avec filtre de prix     |
| `login.html`       | Formulaire de connexion                |
| `place.html`       | Détail d’un lieu + avis + lien review  |
| `add_review.html`  | Ajout d’un avis                        |

### 📱 Responsive Design
Le site est responsive mobile/tablette grâce à `styles.css` et utilise une grille dynamique pour afficher les lieux.

---

## 🔑 Endpoints API (sélection)

| Verbe | URL                         | Description                    | Auth |
|-------|-----------------------------|--------------------------------|------|
| POST  | `/api/v1/auth/login`        | Connexion utilisateur          | ✅   |
| GET   | `/api/v1/users/`            | Liste des utilisateurs (admin) | ✅   |
| POST  | `/api/v1/users/`            | Création d’un utilisateur      | ❌   |
| GET   | `/api/v1/places/`           | Lister tous les lieux          | ✅   |
| POST  | `/api/v1/reviews/`          | Ajouter un avis                | ✅   |
| GET   | `/api/v1/amenities/`        | Lister les commodités          | ✅   |

---

## 🔒 Sécurité

- **JWT** pour sécuriser toutes les opérations sensibles
- **Blacklist** des tokens pour gérer les logouts
- **Contrôle d’accès** dans chaque route (admin / owner check)
- **Validation côté serveur** pour les données critiques

---

## 🛠️ Développement futur

- Système de réservation
- Uploads d’images réels pour les lieux
- Dashboard admin plus avancé

---

## 👨‍💻 Auteurs

 **Alexis Battistoni** → https://github.com/Albat93
