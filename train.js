// TASK G 
// Yagona parametrga ega function tuzing.
// Va bu function parametr orqalik integer ma'lumot turlariga ega bo'lgan bir arrayni qabul qilsin.
// Ushbu function bizga arrayning tarkibidagi birinchi eng katta qiymatning indeksini qaytarsin.
// MASALAN: getHighestIndex([5, 21, 12, 21 ,8]); return qiladi 1 sonini
// Yuqoridagi misolda, birinchi indeksda 21 joylashgan.
// Va bu 21 soni arrayning tarkibidagi birinchi eng katta son hisobladi va bizga uning indeksi 1 qaytadi.

function getHighestIndex(ary) {
  if (ary.length === 0) return -1;
  let highestIndex = 0; 
  for (let i = 1; i < ary.length; i++) {
    if (ary[i] > ary[highestIndex]) {
      highestIndex = i;
    }
  }
  return highestIndex;
}
console.log(getHighestIndex([5,31,67,20,17])); 


// TASK ====> F
// Yagona string argumentga ega findDoublers nomli function tuzing
// Agar stringda bittadan ortiq bir xil harflar ishtirok etgan bo'lsa
// true yokida false natija qaytarsin.

// MASALAN: findDoublers("hello"); natija true qaytadi. Sababi ikki marotaba takrorlangan 'll' harfi mavjud!

// function findDoublers(word) {
//     const soz = word.toLowerCase();
    
//     for (let i = 0; i < soz.length; i++) {
//         for (let j = i + 1; j < soz.length; j++) {
//             if (soz[i] === soz[j]) {
//                 return true;
//             }
//         }
//     }
//     return false;
// }

// console.log(findDoublers("hello"));
// console.log(findDoublers("world")); 



// TASK ===> E
// Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
// MASALAN: getReverse("hello") return qilsin "olleh"

// function getReverse(word) {
//     return word.split('').reverse().join('');
// }

// console.log(getReverse("hello")); 
// console.log(getReverse("dasturlash")); 
// console.log(getReverse("Developer"));