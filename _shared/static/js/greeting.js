const now = new Date();
const greetingElement = document.getElementById('greeting');
const currentHour = now.getHours();
let greeting;
if (currentHour < 12) {
    greeting = 'Good morning';
} else if (currentHour < 18) {
    greeting = 'Good afternoon';
} else {
    greeting = 'Good evening';
}
greetingElement.textContent = greeting;