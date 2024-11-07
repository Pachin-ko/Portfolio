function login(){
    var login = document.getElementById("t1").value;
    var password = document.getElementById("h1").value;
    if(login == "admin" && password == "admin")
    {
        window.location.href="ok.html"
    }
else {
    alert("Identification non reconnus");
    window.location.href="denied.html";
}
}