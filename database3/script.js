function fetchAndDisplayUsers() {
    fetch('http://localhost:3000/users')
        .then(response => response.json())
        .then(data => {
            console.log(data); // Log the received data directly
            displayUsers(data); // Call the displayUsers function to render the data on the page
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

function displayUsers(users) {
    const userDataDiv = document.getElementById('userData');
    userDataDiv.innerHTML = ''; // Clear previous data

    const userList = document.createElement('ul');
    
    // Iterate through each user and create list items to display their data
    users.forEach(user => {
        const listItem = document.createElement('li');
        listItem.textContent = `ID: ${user.id}, Username: ${user.username}, Email: ${user.email}   `;
        listItem.button = document.createElement('button');
        listItem.button.textContent = 'Delete';
        listItem.button.addEventListener('click', () => {
            deleteUser(user.id);
        });
        listItem.appendChild(listItem.button);
        userList.appendChild(listItem);
    });

    
    // Append the list of users to the userDataDiv
    userDataDiv.appendChild(userList);
}

function deleteUser(id) {
    fetch(`http://localhost:3000/deleteUser/${id}`, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            fetchAndDisplayUsers();
        } else {
            console.error('Error deleting user');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function updateUser(id) {
    const username = prompt('Enter new username:');
    const email = prompt('Enter new email:');

    fetch(`http://localhost:3000/updateUser/${id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, email })
    })
    .then(response => {
        if (response.ok) {
            fetchAndDisplayUsers();
        } else {
            console.error('Error updating user');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}