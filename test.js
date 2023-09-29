const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.question('', (a) => {
  rl.question('', (b) => {
    rl.question('', (c) => {
      rl.question('', (d) => {
        const first_product = a * b;
        const second_product = c * d;
        const difference = first_product - second_product;
        console.log(difference);
        rl.close();
      });
    });
  });
});