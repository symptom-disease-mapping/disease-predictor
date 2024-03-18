import React from 'react';
import { Link } from 'react-router-dom';

const ReportPage = ({ selectedDiseases = ["no diseases","sds"] }) => {
  return (
    <div className="flex flex-col items-center justify-center h-screen  bg-azure">
      <h1 className="text-15xl mb-8  font-semibold ">Report</h1>
      
      <div className="w-full max-w-md p-4 bg-gray-100 rounded-lg shadow-lg bg-white">
        <h2 className="text-lg font-semibold mb-4">Selected Diseases:</h2>
        <ul>
          {selectedDiseases.map((disease, index) => (
            <li key={index} className="mb-2">{disease}</li>
          ))}
        </ul>
      </div>

      <Link to="/symptomchecker" className="mt-8   py-2 px-4  text-5xl font-semibold font-nunito-sans text-white text-left  cursor-pointer pt-[11px] pb-[9px] pr-[21px] pl-6 bg-lightseagreen rounded-3xs shadow-[6px_4px_10px_rgba(0,_0,_0,_0.25)] flex flex-row items-center justify-center whitespace-nowrap z-[1] border-[1px] border-solid border-black hover:bg-turquoise hover:box-border hover:border-[1px] hover:border-solid hover:border-darkslategray-200">
        Check Another Symptom
      </Link>
    </div>
  );
};

export default ReportPage;
