//Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ()
function expressionsMatter(a, b ,c){
    const myList = [];
    myList.push(a + b + c, a * (b + c), a * b * c, a + b * c, (a + b) * c);
    return Math.max(...myList)
}