// Your React Vite component
import React, { useState } from 'react';
import axios from 'axios';

const SearchComponent = () => {
  const [symptom, setSymptom] = useState('');
  const [result, setResult] = useState(null);

  const handleSearch = async () => {
    try {
      const response = await axios.post('http://localhost:8000/search/', { symptom });

      if (response.status === 200) {
        setResult(response.data);
      } else {
        console.error('Error:', response.statusText);
      }
    } catch (error) {
      console.error('Error:', error.message);
    }
  };

  return (
    <div>
      <input type="text" value={symptom} onChange={(e) => setSymptom(e.target.value)} />
      <button onClick={handleSearch}>Search</button>

      {result && (
        <div>
          <h2>{result.disease}</h2>
          
          {/* Display other fields as needed */}
        </div>
      )}
    </div>
  );
};

export default SearchComponent;
