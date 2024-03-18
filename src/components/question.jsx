import { Link } from "react-router-dom";
import DropdownComponent from "./Search2";

const Question = () => {
  return (
    <div className="w-[1167px] flex-1 flex flex-col items-end justify-start pt-[3px] px-[45px] pb-[37px] box-border relative gap-[44px_0px] max-w-full text-left text-15xl text-black font-nunito-sans lg:pl-[22px] lg:pr-[22px] lg:box-border mq750:gap-[44px_0px]">
      <img
        className="w-[724px] h-[543px] absolute !m-[0] bottom-[-31px] left-[200px] object-cover z-[1]"
        loading="lazy"
        alt=""
        src="/images-4@2x.png"
      />
      <div className="w-full h-full absolute !m-[0] top-[0px] right-[0px] bottom-[1px] left-[0px] rounded-xl bg-gray-500 shadow-[4px_4px_10px_rgba(0,_0,_0,_0.25)] z-[2]" />
      <div className="self-stretch flex flex-row items-start justify-center py-0 pr-[54px] pl-0">
        <h1 className="m-0 relative text-15xl text-inherit font-semibold font-inherit z-[3] mq450:text-9xl mq1050:text-19xl ">
          Topic
        </h1>
      </div>
      <div className="w-[1014px] flex-1 flex flex-row items-start justify-start pt-0 pb-[5px] px-0 box-border max-w-full text-xl z-[3]">
        <div className="self-stretch w-[931px] flex flex-col items-start justify-start gap-[28px_0px] max-w-full">
        <DropdownComponent/>
        </div> 
      </div>
      <Link to="reportpage" className="cursor-pointer pt-2.5 pb-2 pr-[34px] pl-[37px] bg-darkslategray-100 rounded-xl shadow-[6px_4px_10px_rgba(0,_0,_0,_0.25)] flex flex-row items-center justify-center border-[0px] border-solid border-darkslategray-100 hover:bg-dimgray relative text-11xl font-semibold font-nunito-sans text-white text-5xl text-left z-[3] mq450:text-lg mq1050:text-5xl">
            Next
          </Link>
    </div>
  );
};

export default Question;
