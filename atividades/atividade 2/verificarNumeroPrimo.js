

function verificarNumeroPrimo(n){
    if(n <= 1){
       return false;
    }if ((n != 2) && (n%2 == 0)) {
        return false;
        
    } 
    for( let i =3; i<n; i+= 2){
        if(i%)
    }
}

for(n=0; n<11; n++){
    console.log('n =' + n)
    console.log(' '+ verificarNumeroPrimo(n))
}
