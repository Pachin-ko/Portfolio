function multiplication(){
    var n1 = document.getElementById("n1").value;
    var n2 = document.getElementById("n2").value;
    var n3 = document.getElementById("n3").value;
    var n4 = document.getElementById("n4").value;
    var n5 = document.getElementById("n5").value;
    var n6 = document.getElementById("n6").value;

    var r1 = Number(n1)*Number(n2);
    var r2 = Number(n3)*Number(n4);
    var r3 = Number(n5)*Number(n6);

    document.getElementById("r1").value = r1;
    document.getElementById("r2").value = r2;
    document.getElementById("r3").value = r3;

    var r4 = Number(r1)+Number(r2)+Number(r3);
    document.getElementById("r4").value = r4;
}

