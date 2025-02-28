function toggle() {
    var x = document.getElementById('older');
    if (x.style.display == 'none') {
        x.style.display = 'block';
    } else {
        x.style.display = 'none';
    }
}

/* Function to toggle the "dark-mode" class and save preference in localStorage
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode);
}

// Check localStorage for the user's dark mode preference on page load
document.addEventListener('DOMContentLoaded', () => {
    const darkMode = localStorage.getItem('darkMode') === 'true';
    if (darkMode) {
        document.body.classList.add('dark-mode');
    }

    // Attach event listener to the toggle button
    document.getElementById('darkModeToggle').addEventListener('click', toggleDarkMode);
});
*/

// Function to toggle the "dark-mode" class and save preferences in localStorage
// function toggleDarkMode() {
//     // Toggle the "dark-mode" class on the body
//     document.body.classList.toggle('dark-mode');

//     // Get the button element
//     const button = document.getElementById('darkModeToggle');
//     // Toggle the "toggleddark" class on the button
//     button.classList.toggle('toggledark');

//     // Save the dark mode state and button style to localStorage
//     const isDarkMode = document.body.classList.contains('dark-mode');
//     const isButtonToggled = button.classList.contains('toggleddark');

//     localStorage.setItem('darkMode', isDarkMode);
//     localStorage.setItem('buttonToggled', isButtonToggled);
// }

// function togglebuttonstyle() {
//     const button = document.getElementById('darkModeToggle');
//     button.classList.toggle('toggledark');
    
// }

// // Check localStorage for the user's preferences on page load
// document.addEventListener('DOMContentLoaded', () => {
//     const darkMode = localStorage.getItem('darkMode') === 'true';
//     const buttonToggled = localStorage.getItem('buttonToggled') === 'true';

//     // Apply the dark mode class if saved in localStorage
//     if (darkMode) {
//         document.body.classList.add('dark-mode');
//     }

//     // Apply the button style if saved in localStorage
//     const button = document.getElementById('darkModeToggle');
//     if (buttonToggled) {
//         button.classList.add('toggleddark');
//     }

//     // Attach event listener to the toggle button
//     button.addEventListener('click', toggleDarkMode);
//     button.addEventListener('click', togglebuttonstyle);
// });