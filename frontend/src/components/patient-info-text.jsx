const PatientInfoText = () => {
  return (
    <div className="w-[1165px] flex flex-col items-center justify-start pt-9 pb-[41px] pr-[61px] pl-[349px] box-border relative gap-[58px_0px] max-w-full text-left text-8xl text-black font-nunito-sans lg:pl-[174px] lg:pr-[30px] lg:box-border mq450:pl-5 mq450:box-border mq750:gap-[58px_0px] mq750:pl-[87px] mq750:pt-[23px] mq750:pb-[27px] mq750:box-border">
      <img
        className="w-[724px] h-[543px] absolute !m-[0] bottom-[-25px] left-[182px] object-cover z-[1]"
        alt=""
        src="/images-4@2x.png"
      />
      <div className="w-full h-full absolute !m-[0] top-[0px] right-[0px] bottom-[3px] left-[0px] rounded-xl bg-gray-100 shadow-[4px_4px_10px_rgba(0,_0,_0,_0.25)] z-[2]" />
      <div className="self-stretch flex flex-row items-center justify-center py-0 px-[9px] box-border max-w-full">
        <h1 className="m-0 h-[68px] w-[450px] relative font-semibold  inline-block shrink-0 max-w-full z-[3] text-8xl">
          Patient Information
        </h1>
      </div>
      <div className="self-stretch flex flex-col items-start justify-start gap-[42px_0px] max-w-full text-9xl text-dimgray-200 mq750:gap-[42px_0px]">
      <div className="w-[416px] flex flex-row items-start justify-center py-0 px-5 box-border max-w-full">
  <div className="w-[182px] rounded-xl bg-white shadow-[6px_4px_10px_rgba(0,_0,_0,_0.25)] box-border flex flex-row items-center justify-center pt-4 pb-[11px] pr-6 pl-[33px] gap-[17px] z-[3] border-[0px] border-solid border-black">
    <img
      className="h-[61.5px] w-[182.3px] relative rounded-xl hidden"
      alt=""
      src="/rectangle-9639.svg"
    />
    <h3 className="m-0 relative text-inherit font-semibold font-inherit z-[1] mq450:text-3xl">
      Age
    </h3>

    <input 
  type="integer" 
  className="w-[50px] h-[33px] px-2 rounded-lg border border-gray-300 shadow-sm" 
   min={0}
   max={120}
/>

  </div>
</div>

        <div className="self-stretch flex flex-col items-end justify-center gap-[21px_0px] max-w-full">
          <div className="self-stretch flex flex-row items-start justify-start max-w-full">
            <div className="flex flex-row items-center justify-center gap-[0px_47px] max-w-full mq450:gap-[0px_47px] mq750:flex-wrap">
              <button className="cursor-pointer pt-[5px] pb-1.5 pr-[61px] pl-[60px] bg-white rounded-xl shadow-[6px_4px_10px_rgba(0,_0,_0,_0.25)] flex flex-col items-center justify-center z-[3] border-[0px] border-solid border-black">
                <img
                  className="w-[183.8px] h-[106.7px] relative rounded-xl hidden"
                  alt=""
                  src="/rectangle-9639.svg"
                />
                <div className="h-[57px] flex flex-row items-center justify-center py-0 pr-0.5 pl-0 box-border">
                  <img
                    className="mb-[-4px] h-[61px] w-[61px] relative object-cover z-[4]"
                    alt=""
                    src="/240-f-549928360-lpdzuoiu6zjkcfp7b3hxjnaditqgtpn3-3@2x.png"
                  />
                </div>
                <div className="relative text-9xl font-semibold font-nunito-sans text-dimgray-200 text-left z-[1] mq450:text-3xl">
                  Male
                </div>
              </button>
              <button className="cursor-pointer pt-[5px] pb-1.5 pr-[61px] pl-[60px] bg-white rounded-xl shadow-[6px_4px_10px_rgba(0,_0,_0,_0.25)] flex flex-col items-center justify-center gap-[2px] z-[3] border-[0px] border-solid border-black">
                <img
                  className="w-[183.8px] h-[106.7px] relative rounded-xl hidden"
                  alt=""
                  src="/rectangle-9639.svg"
                />
                <img
                  className="w-12 h-[53px] relative object-cover z-[4]"
                  alt=""
                  src="/240-f-549928360-lpdzuoiu6zjkcfp7b3hxjnaditqgtpn3-2@2x.png"
                />
                <div className="relative text-9xl font-semibold font-nunito-sans text-dimgray-200 text-left z-[1] mq450:text-3xl">
                  Female
                </div>
              </button>
            </div>
          </div>
          <button className="cursor-pointer pt-2.5 pb-2 pr-[34px] pl-[37px] bg-darkslategray-100 rounded-xl shadow-[6px_4px_10px_rgba(0,_0,_0,_0.25)] flex flex-row items-center justify-center z-[3] border-[0px] border-solid border-darkslategray-100 hover:bg-dimgray-100 hover:box-border hover:border-[1px] hover:border-solid hover:border-dimgray-100">
            <img
              className="h-[59.6px] w-[137px] relative rounded-xl hidden"
              alt=""
              src="/rectangle-9639.svg"
            />
            <div className="relative text-11xl font-semibold font-nunito-sans text-white text-left z-[1] mq450:text-lg mq1050:text-5xl">
              Next
            </div>
          </button>
        </div>
      </div>
    </div>
  );
};

export default PatientInfoText;
