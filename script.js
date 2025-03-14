function getComprasFromSessionStorage(){
    let compras = JSON.parse(localStorage.getItem("compras")) || [];
    return compras;
}

function saveComprasToSession(compras){
    localStorage.setItem('compras', JSON.stringify(compras))
}