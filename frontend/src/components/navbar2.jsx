const NavBar2 = () => {
  return (
    <header className="self-stretch bg-darkslategray-100 flex flex-row items-center justify-between pt-[11px] pb-1 pr-9 pl-3.5 box-border top-[0] z-[99] sticky max-w-full gap-[20px] text-left text-15xl text-lightseagreen font-advent-pro">
      <div className="h-[66px] w-[1440px] relative bg-darkslategray-100 hidden max-w-full" />
      <div className="flex flex-row items-start justify-start gap-[0px_34px]">
        <img
          className="h-[38px] w-[34.8px] relative z-[1]"
          loading="lazy"
          alt=""
          src="/-icon-drone.svg"
        />
        <h2 className="m-0 relative text-inherit font-semibold font-inherit whitespace-nowrap z-[1]">
          SympCheck
        </h2>
      </div>
      <div className="flex flex-row items-start justify-start gap-[0px_56px] max-w-full text-xl text-white font-inter mq750:gap-[0px_56px] mq1050:hidden">
        <div className="relative font-semibold whitespace-nowrap z-[1]">
          Symptom Checker
        </div>
        <div className="relative font-semibold whitespace-nowrap z-[1]">
          Sign In
        </div>
        <div className="relative font-semibold whitespace-nowrap z-[1]">
          Sign Up
        </div>
        <div className="relative font-semibold whitespace-nowrap z-[1]">
          contact us
        </div>
      </div>
    </header>
  );
};

export default NavBar2;
