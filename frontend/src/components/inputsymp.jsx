const InputSymp = () => {
  return (
    <div className="w-full h-[832px] bg-white overflow-hidden text-left text-xl text-white font-inter">
      <section className="absolute top-[368px] left-[0px] bg-azure w-full h-[290px]" />

      <img
        className="absolute top-[37px] left-[561px] w-[318px] h-[318px] object-cover "
        loading="lazy"
        alt=""
        src="/images-41@2x.png"
      />

      <div className="absolute top-[330px] left-[494px] w-[462.9px] h-[62.2px] text-5xl text-gray-300 font-nunito-sans">
        <div className="absolute h-full top-[0px] bottom-[0px] left-[0px] w-[398.6px]">
          {/* <div className="absolute top-[0px] left-[0px] w-[398.6px] h-[62.2px] flex items-center justify-center border-solid "> */}
          {/* <img
              className="w-full h-full object-contain absolute left-[6px] top-[4px] [transform:scale(1.322)]"
              alt=""
              src="/rectangle-96393.svg"
            /> */}
          <input
            type="text"
            placeholder=" Symptoms..."
            className="w-full h-full  absolute left-[6px] top-[4px] [transform:scale(1.322)] font-semibold inline-block rounded-xl outline-none border-gray-400 border px-4 py-2 text-black  shadow-[4px_4px_10px_rgba(0,_0,_0,_0.25)] box-border"
          />

          {/* </div> */}
          
        </div>
        <button className="absolute h-full top-[0px] bottom-[0px] left-[397px] w-[65.9px] bg-darkgray">
          {/* <img
            className="absolute top-[0px] left-[0px] w-[65.9px] h-[62.2px] object-contain"
            alt=""
            src="/rectangle-9640.svg"
          /> */}
          <img
            className="absolute top-[18.1px] left-[20.4px] w-[24.6px] h-[26.3px]"
            loading="lazy"
            alt=""
            src="/group-1.svg"
          />
        </button>
      </div>
      <textarea
        className="bg-white h-[211.4px] w-[243px] [outline:none] absolute top-[409px] left-[603px] rounded-xl shadow-[4px_4px_10px_rgba(0,_0,_0,_0.25)] box-border py-[26.30000000000001px] px-[26.300000000000182px] font-inter text-[16px] text-black border-[1px] border-solid border-gray-400"
        placeholder="Fever"
        rows={11}
        cols={12}
      />

      <button className="cursor-pointer [border:none] p-0 bg-[transparent] absolute top-[560px] left-[1257px] w-[137px] h-[59.6px]">
        <div className="absolute top-[0px] left-[0px] w-[137px] h-[59.6px]">
          <div className="absolute top-[0px] left-[0px] rounded-xl w-[137px] h-[59.6px] flex items-center justify-center">
            <img
              className="w-full h-full object-contain absolute left-[6px] top-[4px] [transform:scale(1.336)]"
              alt=""
              src="/rectangle-96392.svg"
            />
          </div>
          <div className="absolute top-[9.7px] left-[37px] text-11xl font-semibold font-nunito-sans text-white text-left">
            Next
          </div>
        </div>
      </button>
    </div>
  );
};

export default InputSymp;
