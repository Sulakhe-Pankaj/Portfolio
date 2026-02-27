// Check for saved user preference, if any, on load
(function() {
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
    }

    // Wait for DOM to load fully before adding listeners
    document.addEventListener('DOMContentLoaded', () => {
        const themeToggles = document.querySelectorAll('.theme-toggle');
        
        // Update icons on initial load
        themeToggles.forEach(toggle => {
            const icon = toggle.querySelector('i');
            if (savedTheme === 'light') {
                icon.classList.remove('fa-sun');
                icon.classList.add('fa-moon');
            } else {
                icon.classList.remove('fa-moon');
                icon.classList.add('fa-sun');
            }
            
            // Add click listener
            toggle.addEventListener('click', function(e) {
                e.preventDefault();
                toggleTheme();
            });
        });
    });
})();

function toggleTheme() {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    let newTheme = 'dark';
    
    if (currentTheme !== 'light') {
        newTheme = 'light';
    }
    
    // Apply theme
    if (newTheme === 'light') {
        document.documentElement.setAttribute('data-theme', 'light');
    } else {
        document.documentElement.removeAttribute('data-theme');
    }
    
    // Save to localStorage
    localStorage.setItem('theme', newTheme);
    
    // Update all toggle icons on the page
    const themeToggles = document.querySelectorAll('.theme-toggle');
    themeToggles.forEach(toggle => {
        const icon = toggle.querySelector('i');
        if (newTheme === 'light') {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        } else {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        }
    });
}
