const form = document.getElementById('interaction-form');
const greetingText = document.getElementById('greeting-text');
const surpriseButton = document.getElementById('surprise-button');
const surpriseText = document.getElementById('surprise-text');
const themeSelect = document.getElementById('theme');

form.addEventListener('submit', (event) => {
  event.preventDefault();

  const name = document.getElementById('name').value.trim();
  const theme = themeSelect.value;

  if (name.length === 0) {
    greetingText.textContent = 'Please enter your name to continue.';
    return;
  }

  greetingText.textContent = `Hello, ${name}! Welcome to your interactive web page.`;
  document.body.className = '';

  if (theme === 'dark') {
    document.body.classList.add('theme-dark');
  } else if (theme === 'colorful') {
    document.body.classList.add('theme-colorful');
  }
});

surpriseButton.addEventListener('click', () => {
  surpriseText.classList.toggle('hidden');
});
