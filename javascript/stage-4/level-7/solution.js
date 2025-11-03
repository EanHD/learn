let contacts = [
  { name: "Alice", phone: "555-1234", email: "alice@email.com" },
  { name: "Bob", phone: "555-5678", email: "bob@email.com" }
];

function findContact(name) {
  for (let i = 0; i < contacts.length; i++) {
    if (contacts[i].name.toLowerCase() === name.toLowerCase()) {
      return contacts[i];
    }
  }
  return null;
}

function displayContact(c) {
  console.log(c.name);
  console.log("Phone: " + c.phone);
  console.log("Email: " + c.email);
}

let found = findContact("Alice");
if (found) {
  displayContact(found);
}
