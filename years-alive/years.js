const rawAge = prompt("Enter your age: ");
const age = parseInt(rawAge);

const years = 90 - age;

const months = years * 12;
const weeks = years * 52;
const days = years * 365;

console.log(`You have ${years} years, ${months} months, ${weeks} weeks, and ${days} days left to live.`);