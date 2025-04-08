// Fonction pour vérifier si l'utilisateur est authentifié en vérifiant le cookie
function checkAuth() {
  const cookies = document.cookie.split(';');
  let token = null;

  cookies.forEach(cookie => {
    const [key, value] = cookie.trim().split('=');
    if (key === 'token') {
      token = value;
    }
  });

  if (!token) {
    // Si aucun token n'est trouvé, rediriger vers la page de login
    window.location.href = 'login.html';
  }
}

// Fonction pour gérer la connexion de l'utilisateur
async function loginUser(email, password) {
  try {
    const response = await fetch('http://127.0.0.1:5000/api/v1/auth/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ email, password })
    });

    if (response.ok) {
      const data = await response.json();
      // Stocker le JWT dans un cookie
			document.cookie = `token=${data.access_token}; path=/; Secure`;
			// Afficher un message de succès
			alert("Connexion réussie !");
			// Vérifier si l'utilisateur est authentifié
			checkAuth();
      // Rediriger vers la page d'accueil après la connexion
      window.location.href = 'index.html';
    } else {
      document.getElementById("error-message").style.display = "block";
    }
  } catch (error) {
    console.error('Login failed', error);
    document.getElementById("error-message").style.display = "block";
  }
}

// Ajouter l'événement au formulaire de login
document.addEventListener('DOMContentLoaded', () => {
  const loginForm = document.getElementById('login-form');

  if (loginForm) {
    loginForm.addEventListener('submit', async (event) => {
      event.preventDefault();
      const email = document.getElementById('email').value;
      const password = document.getElementById('password').value;
      await loginUser(email, password);
    });
  }

  // Vérifier si l'utilisateur est authentifié sur des pages protégées comme place.html
  if (window.location.pathname === '/place.html') {
    checkAuth();
  }

  // Affichage des détails de la place
  if (document.getElementById("place-name")) {
    document.getElementById("place-name").textContent = localStorage.getItem("placeName");
    document.getElementById("place-description").textContent = localStorage.getItem("placeDescription");
    document.getElementById("place-image").src = localStorage.getItem("placeImage");
  }
});

// Fonction pour afficher les détails d'un lieu
function viewDetails(placeId) {
  // Vérifier si l'utilisateur est authentifié avant de continuer
  const cookies = document.cookie.split(';');
  let token = null;

  cookies.forEach(cookie => {
    const [key, value] = cookie.trim().split('=');
    if (key === 'token') {
      token = value;
    }
  });

  if (!token) {
    // Si aucun token n'est trouvé, rediriger vers la page de login
    window.location.href = 'login.html';
    return;
  }

  const placeNames = {
    "1": "Beach House",
    "2": "Cozy Cabin",
    "3": "City Apartment"
  };

  const descriptions = {
    "1": "Beautiful house by the sea, perfect for a summer getaway.",
    "2": "Escape to the woods in this cozy and peaceful cabin.",
    "3": "Modern apartment in the heart of the city, close to everything."
  };

  const images = {
    "1": "https://source.unsplash.com/800x500/?house,beach",
    "2": "https://source.unsplash.com/800x500/?cabin,forest",
    "3": "https://source.unsplash.com/800x500/?apartment,city"
  };

  localStorage.setItem("placeName", placeNames[placeId]);
  localStorage.setItem("placeDescription", descriptions[placeId]);
  localStorage.setItem("placeImage", images[placeId]);

  window.location.href = "place.html";
}
