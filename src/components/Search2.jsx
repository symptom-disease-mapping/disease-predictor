import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useLocation } from 'react-router-dom';

const DropdownComponent = () => {
  const [options, setOptions] = useState([]);
  const [selectedOptions, setSelectedOptions] = useState([]);
  const [selectedValue, setSelectedValue] = useState('');
  const location = useLocation();

  // Set majorDisease with location.state.majorDisease or default value
  const majorDisease = location.state?.majorDisease || 'Default Major Disease';

  useEffect(() => {
    console.log(majorDisease); // Log major disease here

    const fetchData = async () => {
      try {
        if (!majorDisease) {
          console.error('No major disease found in location state');
          return;
        }

        const response = await axios.post('http://127.0.0.1:8000/getMajorSymptoms/', { symptoms: majorDisease });
        setOptions(response.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [majorDisease]);

  const handleSelectChange = (event) => {
    setSelectedValue(event.target.value);
  };

  const handleAddOption = () => {
    if (selectedValue) {
      setSelectedOptions([...selectedOptions, selectedValue]);
      setSelectedValue('');
    }
  };

  return (
    <div className="absolute h-full top-[0px] bottom-[0px] left-[30%] w-[398.6px]">
      <select
        value={selectedValue}
        onChange={handleSelectChange}
        className="w-full h-[50px] absolute left-[6px] top-[50%] bg-white transform scale-125 font-semibold inline-block rounded-xl outline-none border-gray-400 border px-4 py-2 text-black shadow-[4px_4px_10px_rgba(0,_0,_0,_0.25)] box-border"
      >
        <option value="">Symptoms...</option>
        {options.map((option, index) => (
          <option key={index} value={option}>
            {option}
          </option>
        ))}
      </select>
      <button
        onClick={handleAddOption}
        className="absolute top-[50%] text-black h-[50px]  bottom-[0px] left-[500px] w-[65.9px] bg-darkgray"
      >
        ADD
      </button>
      {selectedOptions.length > 0 && (
        <div className="absolute w-full text-black bg-white border border-gray-400 rounded-xl p-2 outline-none top-[90px] shadow-[4px_4px_10px_rgba(0,_0,_0,_0.25)] box-border py-[26.30000000000001px] px-[26px] font-inter text-[16px] border-solid border-gray-400">
          {selectedOptions.map((option, index) => (
            <div key={index} className="border-b border-gray-400 py-1">
              {option}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default DropdownComponent;
