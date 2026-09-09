// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

function getReverse(word) {
    return word.split('').reverse().join('');
}

console.log(getReverse("hello")); 
console.log(getReverse("dasturlash")); 
console.log(getReverse("Developer"));