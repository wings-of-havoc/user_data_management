<script>
  // Check if a userId already exists in localStorage
  let userId = localStorage.getItem('userId');

  if (!userId) {
    // Make a GET request to your server's API endpoint
    fetch('/generate_user_id')  
      .then(response => {
        if (!response.ok) {
          console.error('API request failed:', response.status, response.statusText);
          return;
        }
        return response.json();
      })
      .then(data => {
        if (data && data.user_id) {
          userId = data.user_id;
          localStorage.setItem('user_id', user_id);

          // Push the userId to the dataLayer
          dataLayer.push({
            'event': 'user_id_generated', // Optional: Use a custom event
            'user_id': user_id
          });
        } else {
          console.error('Invalid response from server:', data);
        }
      })
      .catch(error => {
        console.error('API request error:', error);
      });
  }
</script>
