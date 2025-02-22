document.getElementById('bot-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    const botName = document.getElementById('bot_name').value;
    const token = document.getElementById('token').value;

    const response = await fetch('/create-bot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ bot_name: botName, token: token })
    });

    const data = await response.json();
    document.getElementById('bot-code').textContent = data.bot_code;
});
