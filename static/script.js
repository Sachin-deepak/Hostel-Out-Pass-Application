document.addEventListener('DOMContentLoaded', function () {
    const passForm = document.getElementById('passForm');
    const passesList = document.getElementById('passesList');

    passForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const name = document.getElementById('name').value;
        const reason = document.getElementById('reason').value;

        fetch('/apply', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ name: name, reason: reason })
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            fetchPasses();
        })
        .catch(error => console.error('Error:', error));
    });

    function fetchPasses() {
        fetch('/passes')
            .then(response => response.json())
            .then(data => {
                passesList.innerHTML = '';
                data.forEach((pass, index) => {
                    const li = document.createElement('li');
                    li.innerHTML = `
                        ${pass.name}: ${pass.reason} - Status: ${pass.status}
                        ${isAdmin ? `
                        <button onclick="updatePassStatus(${index}, 'approve')">Approve</button>
                        <button onclick="updatePassStatus(${index}, 'reject')">Reject</button>
                        ` : ''}
                    `;
                    passesList.appendChild(li);
                });
            })
            .catch(error => console.error('Error:', error));
    }

    window.updatePassStatus = function(passId, action) {
        fetch(`/${action}/${passId}`, {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => {
            alert(data.message);
            fetchPasses();
        })
        .catch(error => console.error('Error:', error));
    }

    fetchPasses();
});
