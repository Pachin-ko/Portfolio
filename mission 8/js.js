// Récupérer le bouton Submit
const submitBtn = document.getElementById('submitbtn');

// Ajouter un événement au clic du bouton
submitBtn.addEventListener('click', () => {
    let score = 0;

    // Sélectionner toutes les checkbox cochées
    const checkedBoxes = document.querySelectorAll('input[type="checkbox"]:checked');

    // Parcourir les checkbox cochées
    checkedBoxes.forEach(checkbox => {
        score += parseInt(checkbox.value); // Ajouter la valeur de la checkbox au score
    });

    // Calculer le score maximum possible
    const totalPoints = document.querySelectorAll('input[type="checkbox"][value="1"]').length;

    // Afficher une alerte avec le score
    alert(`Votre score est : ${score}/${totalPoints}`);

    // Rediriger vers la page des réponses
    window.location.href = "reponses.html";
});
