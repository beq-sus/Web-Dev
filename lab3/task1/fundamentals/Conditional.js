let year = prompt('In which year was ECMAScript-2015 specification published?', '');

if (year == 2015){
    alert( 'You are right!' );
}  else if (year > 2015) {
  alert( 'Too late' );
} else {
  alert( 'Exactly!' );
}


let age = prompt('How old are you?', '');
let accessAllowed = (age > 18) ? true : false;

let message = (age < 3) ? 'Hi, baby!' :
  (age < 18) ? 'Hello!' :
  (age < 100) ? 'Greetings!' :
  'What an unusual age!';

alert( message );

