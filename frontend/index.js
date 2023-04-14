async function sendPostRequest(url, data){
    return await fetch(
        url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        }
    )
    .then(response => response.json())
    .catch((error) => {console.error(error)})
}


sendPostRequest(
    'http://127.0.0.1:8000/auth/users/activation/',
    {
        uid: "Nw",
        token: "bmnfnn-cdc42e8a86ba3eb5ee1a3482c1dd3f55"
    }
)