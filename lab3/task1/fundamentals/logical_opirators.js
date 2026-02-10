let result = a || b;

alert( true || true );   // true
alert( false || true );  // true
alert( true || false );  // true
alert( false || false ); // false


if (1 || 0) { // works just like if( true || false )
  alert( 'truthy!' );
}


let hour = 9;
if (hour < 10 || hour > 18) {
  alert( 'The office is closed.' );
}

let firstName = "";
let lastName = "";
let nickName = "SuperCoder";

alert( firstName || lastName || nickName || "Anonymous"); // SuperCoder


alert( true && true );   // true
alert( false && true );  // false
alert( true && false );  // false
alert( false && false ); // false

alert( !true ); // false
alert( !0 ); // true

let userName = prompt("Who's there?", '');

if (userName === 'Admin') {

  let pass = prompt('Password?', '');

  if (pass === 'TheMaster') {
    alert( 'Welcome!' );
  } else if (pass === '' || pass === null) {
    alert( 'Canceled' );
  } else {
    alert( 'Wrong password' );
  }

} else if (userName === '' || userName === null) {
  alert( 'Canceled' );
} else {
  alert( "I don't know you" );
}