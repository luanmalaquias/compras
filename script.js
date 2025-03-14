function getComprasFromSessionStorage(){
    let compras = JSON.parse(sessionStorage.getItem("compras")) || [];
    return compras;
}

function saveComprasToSession(compras){
    sessionStorage.setItem('compras', JSON.stringify(compras))
}