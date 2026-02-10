let i = 0;
while (i < 3) { // shows 0, then 1, then 2
  alert( i );
  i++;
}

i = 0;
do {
  alert( i );
  i++;
} while (i < 3);


for (let i = 0; i < 3; i++) { // shows 0, then 1, then 2
  alert(i);
}

outer: for (let i = 0; i < 3; i++) {

  for (let j = 0; j < 3; j++) {

    let input = prompt(`Value at coords (${i},${j})`, '');

    // if an empty string or canceled, then break out of both loops
    if (!input) break outer; // (*)

    // do something with the value...
  }
}

alert('Done!');


i = 0;
while (i++ < 5) alert( i );

for (let i = 0; i < 5; i++) alert( i );

for (let i = 0; i < 3; i++) {
  alert( `number ${i}!` );
}


let num;

do {
  num = prompt("Enter a number greater than 100?", 0);
} while (num <= 100 && num);

let n = 10;

nextPrime:
for (let i = 2; i <= n; i++) { // for each i...

  for (let j = 2; j < i; j++) { // look for a divisor..
    if (i % j == 0) continue nextPrime; // not a prime, go next i
  }

  alert( i ); // a prime
}