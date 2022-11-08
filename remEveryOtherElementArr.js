// Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

function removEveryOther(arr) {
    let i = arr.length;
    while (i--)(i + 1) % 2 === 0 && (arr.splice(i,1));
    return arr;
    
}