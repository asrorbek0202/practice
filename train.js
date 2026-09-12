// TASK ====> F
// Yagona string argumentga ega findDoublers nomli function tuzing
// Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
// true yokida false natija qaytarsin.

// MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

function findDoublers(word) {
    const soz = word.toLowerCase();
    
    for (let i = 0; i < soz.length; i++) {
        for (let j = i + 1; j < soz.length; j++) {
            if (soz[i] === soz[j]) {
                return true;
            }
        }
    }
    return false;
}

console.log(findDoublers("hello"));
console.log(findDoublers("world")); 



// TASK ===> E
// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

// function getReverse(word) {
//     return word.split('').reverse().join('');
// }

// console.log(getReverse("hello")); 
// console.log(getReverse("dasturlash")); 
// console.log(getReverse("Developer"));