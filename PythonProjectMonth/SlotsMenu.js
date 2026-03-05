// This is the JS file for the SlotsMenu.html page.
// It handles the button clicks and keyboard navigation for the menu.

// What will be on the new window when 'Play' is clicked.
const editorTemplate = `<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Slot Machine Game</title>
    <style>
        body { font-family: monospace; padding: 1rem; background: #fafafa; }
        h1, p { color: #333; }
    </style>
</head>
<body contenteditable="true">
    <h1>Slot Machine</h1>
    <p>This is the Slot Machine game.</p>

    <button id="MainMenuButton" color="blue">Main Menu</button>
    
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const mainMenuBtn = document.getElementById('MainMenuButton');
            mainMenuBtn.addEventListener('click', () => {
                window.close();
            });
        });
    </script>
</body>
</html>`;

// Wait for the DOM to load before attaching event listeners
document.addEventListener('DOMContentLoaded', () => {
    const play = document.getElementById('PlayButton');
    const rules = document.getElementById('RulesButton');
    const credits = document.getElementById('CreditsButton');
    const exit = document.getElementById('ExitButton');
    const buttons = Array.from(document.querySelectorAll('.button-group button'));

    // Open a blank editable window for the user to type or paste content
    play.addEventListener('click', () => {
        const w = window.open('', 'Slot Machine', `width=${screen.availWidth},height=${screen.availHeight},scrollbars=yes`);
        if (w) {
            // write the editable template into the new window
            w.document.write(editorTemplate);
            w.document.close();
        }
    });

    rules.addEventListener('click', () => {
        const rulesText = `Rules:\n\n- Press Play to open the Slot Machine window.
        \n- You can type or paste content there and save locally if desired.
        \n- Close the editor window or this tab when finished.`;
        alert(rulesText);
    });

    credits.addEventListener('click', () => {
        const creditsText = `Credits:\n\n- Developed by Lance Griffin
        \n- Sprites by Broderick Goncalves`;
        alert(creditsText);
    });

    exit.addEventListener('click', () => {
        // Try to close window (may be blocked if not opened by script)
        if (window.close) window.close();
        else alert('Close the tab or window to exit.');
    });

    // Keyboard navigation: ArrowDown / ArrowUp moves focus between buttons
    document.addEventListener('keydown', (e) => {
        const active = document.activeElement;
        const idx = buttons.indexOf(active);
        if (e.key === 'ArrowDown') {
            e.preventDefault();
            const next = buttons[(idx + 1) % buttons.length];
            next.focus();
        } else if (e.key === 'ArrowUp') {
            e.preventDefault();
            const prev = buttons[(idx - 1 + buttons.length) % buttons.length];
            prev.focus();
        }
    });

    // Ensure first button is focusable on load for keyboard users
    buttons[0].setAttribute('tabindex', '0');
    buttons.slice(1).forEach(b => b.setAttribute('tabindex', '0'));
});