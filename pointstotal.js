function points(games) {
    let count = 0;
    let len = games.length;
    for (var i = 0; i < len; i++){
        var x = games[i].split(":");
        if (x[0] > x[1]){
            let count = count + 3
        } else if (x[0] === x[1]) {
            let count = count +1

        }
    }
    return count 
}
// ESTA MAL ESTA MADRE HAY QUE REGRESAR A CORREGIRLA Y ENTENDERLA 
