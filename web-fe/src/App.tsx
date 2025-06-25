import './App.css'

import { useEffect } from 'react'

function App() {

  useEffect(() => {
    fetch('rest_api/movies?genres=88c18939-389d-485c-8b25-9150c7a4b321') // Use the service name as the hostname
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      console.log('Parsed JSON:', data);
    })
    .catch((error) => {
      console.error('FETCH ERROR:', error);
    });
  }, [])

  return (
    <>
      <div>
        <p>Movie Knight App</p>
      </div>
    </>
  )
}

export default App
