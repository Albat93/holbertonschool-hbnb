function viewDetails(placeId) {
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

window.addEventListener("DOMContentLoaded", () => {
  if (document.getElementById("place-name")) {
    document.getElementById("place-name").textContent = localStorage.getItem("placeName");
    document.getElementById("place-description").textContent = localStorage.getItem("placeDescription");
    document.getElementById("place-image").src = localStorage.getItem("placeImage");
  }
});
