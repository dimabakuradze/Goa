
let counter = 0;
const paragraph = document.getElementById('counter-paragraph');
const button = document.getElementById('increment-button');
button.addEventListener('click', function() {
    counter++; // 
    paragraph.textContent = counter; 
});
