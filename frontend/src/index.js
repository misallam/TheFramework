const fetch = require('node-fetch');

async function main() {
  const res = await fetch('http://localhost:8000/tracker');
  const tracker = await res.json();
  console.log('World tracker:', tracker);
}

main();
