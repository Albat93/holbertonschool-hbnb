
# 🏠 HBnB - Simplified Airbnb Clone

HBnB is a full-featured web application inspired by Airbnb. It allows users to publish, browse, and manage places, reviews, and amenities. The system is built on a RESTful architecture using Flask and includes a responsive front-end interface.

---

## 🧩 Features

### 🔐 Authentication & Security
- JWT-based login system (access + refresh tokens)
- Token blacklist for secure logout
- User and admin roles
- Admin or ownership required for certain actions (delete, update)

### 👥 Users
- Signup with optional admin promotion via `admin_secret`
- View, update, and delete your account
- Admin-only user listing

### 🏡 Places
- Create places with title, description, price, and coordinates
- Optional amenity linking
- Server-side validation for data consistency
- Price filtering handled on client side

### 🧰 Amenities
- Full CRUD for amenities
- Public read access
- Delete/update restricted to owner or admin

### 🌟 Reviews
- Submit ratings and text reviews for places
- Publicly readable
- Authenticated users can post

---

## 🗂️ Project Structure

```
.
├── run.py                      # Flask entry point
├── config.py                   # Flask and JWT configuration
├── requirements.txt            # Python dependencies
├── app/
│   ├── __init__.py             # App factory + API namespace registration
│   ├── services/
│   │   └── facade.py           # Unified service layer
│   ├── api/v1/
│       ├── users.py            # User routes
│       ├── auth.py             # Authentication routes
│       ├── admin.py            # Admin operations
│       ├── amenities.py        # Amenity routes
│       ├── places.py           # (expected, not provided)
│       ├── reviews.py          # (expected, not provided)
├── templates/
│   ├── index.html              # Places list page
│   ├── login.html              # Login form
│   ├── place.html              # Place detail + reviews
│   ├── add_review.html         # Submit a new review
├── static/
│   ├── styles.css              # Responsive styles
│   ├── scripts.js              # Front-end logic
│   └── images/                 # Icons and logo
```

---

## 🧪 Installation & Launch

### 📦 Prerequisites
- Python 3.8+
- pip

### ⚙️ Installation
```bash
pip install -r requirements.txt
```

### ▶️ Run
```bash
python run.py
```

The app will be available at `http://127.0.0.1:5000`.

---

## 🌐 User Interface

### 🖼 Provided Pages
| Page               | Description                                |
|--------------------|--------------------------------------------|
| `index.html`       | Lists all places with price filter         |
| `login.html`       | User login form                            |
| `place.html`       | Details of a place + reviews + add review  |
| `add_review.html`  | Submit a new review                        |

### 📱 Responsive Design
The UI is fully responsive (desktop/tablet/mobile) and styled with `styles.css`, using a dynamic grid for place display.

---

## 🔑 API Endpoints (Sample)

| Method | URL                         | Description                    | Auth |
|--------|-----------------------------|--------------------------------|------|
| POST   | `/api/v1/auth/login`        | User login                     | ✅   |
| GET    | `/api/v1/users/`            | List users (admin only)        | ✅   |
| POST   | `/api/v1/users/`            | Create a new user              | ❌   |
| GET    | `/api/v1/places/`           | List all places                | ✅   |
| POST   | `/api/v1/reviews/`          | Submit a new review            | ✅   |
| GET    | `/api/v1/amenities/`        | List all amenities             | ✅   |

---

## 🔒 Security

- **JWT** ensures all sensitive endpoints are protected
- **Token blacklist** guarantees secure logout
- **Access control** enforced at route level (admin/owner)
- **Server-side validation** for all important data

---

## 🛠️ Future Development

- Booking system
- Real image upload support for places
- Advanced admin dashboard

---

## 👨‍💻 Contributors
---

- **Jean-Alain Renié** → https://github.com/JaRenie-spec
- **Killian Ripoche** → https://github.com/KillianRipoche
- **Alexis Battistoni** → https://github.com/Albat93

