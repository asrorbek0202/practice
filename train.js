// TASK K
// Shunday function yozing, u string qabul qilsin va string ichidagi unli harflar sonini qaytarsin.
// MASALAN: countVowels("string") return 1;


function countVowels(word) {
  const vowels = "aeiouAEIOU";
  let count = 0;
  for (let vowel of word) {
    if (vowels.includes(vowel)) {
      count++;
    }
  }

  return count;
}

console.log(countVowels("string")); 
console.log(countVowels("Hello World"));

// def count_vowels(word):
//     vowels = "aeiouAEIOU"
//         count = 0
//         for char in word:
//         if char in vowels:
//             count += 1
            
//     return count
// print(count_vowels("string"))
// print(count_vowels("Hello World"))  



// TASK G 
// Yagona parametrga ega function tuzing.
// Va bu function parametr orqalik integer ma'lumot turlariga ega bo'lgan bir arrayni qabul qilsin.
// Ushbu function bizga arrayning tarkibidagi birinchi eng katta qiymatning indeksini qaytarsin.
// MASALAN: getHighestIndex([5, 21, 12, 21 ,8]); return qiladi 1 sonini
// Yuqoridagi misolda, birinchi indeksda 21 joylashgan.
// Va bu 21 soni arrayning tarkibidagi birinchi eng katta son hisobladi va bizga uning indeksi 1 qaytadi.

// function getHighestIndex(ary) {
//   let highestIndex = 0; 
//   for (let i = 0; i < ary.length; i++) {
//     if (ary[i] > highestIndex) {
//       highestIndex = ary[i];
//     }
//   }
//   let index = ary.indexOf(highestIndex)
//   return index;
// }
// console.log(getHighestIndex([5,31,67,20,17])); 


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