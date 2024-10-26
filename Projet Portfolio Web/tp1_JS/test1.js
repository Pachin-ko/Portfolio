function test_age() {
    let age = prompt("Quelle est votre âge ?");
    if (age < 18) {
        document.write("Vous êtes mineur");
        document.body.style.backgroundColor="red"
    }
    else {
        document.write("Vous êtes majeur");
        document.body.style.backgroundColor="rgb(91,129,9)";
    }
}

function calcul_moyenne() {
    var n1 = prompt("Donner la première note :");
    var n2 = prompt("Donner la seconde note :");
    var n3 = prompt("Donner la troisième note :");

    var somme = Number(n1) + Number(n2) + Number(n3);

    document.write("Voici la somme : " + somme + "<br>");
    var moyenne = somme/3;

    document.write("Voici la moyenne : " + moyenne + "<br>");
    if (moyenne < 10) {
        document.write("Désolé, vous êtes refusé.");
        document.body.style.backgroundColor="red"
    }
    else {
        document.write("Félicitation, vous êtes admis.");
        document.body.style.backgroundColor="rgb(91,129,9)";
    }

function test_couleur() {
    let couleur = prompt("Donner une couleur");
    document.body.style.backgroundColor = couleur;
}