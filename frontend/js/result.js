let result = await fetch('localhost:8080/upload');
console.log(result);

let res = document.getElementById('getRes');

res.textContent = result;