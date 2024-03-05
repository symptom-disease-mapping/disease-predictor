import NavBar2 from "../components/navbar2";

import Footer from "../components/footer";
import InputSymp from "../components/inputsymp";

const InputPage = () => {
  return (
   
       <div className="w-full  bg-white overflow-hidden flex flex-col items-start justify-start gap-[217px_0px] tracking-[normal] text-left text-mini text-white font-inter mq450:gap-[217px_0px] mq750:h-auto mq750:gap-[217px_0px]">
       <section className="self-stretch flex flex-col items-start justify-start max-w-full shrink-0">
         <NavBar2 />
         <div className="self-stretch h-[571px] flex flex-col items-center justify-center pt-[37px] pb-[45px] pr-[21px] pl-5 box-border max-w-full mq750:pt-6 mq750:pb-[29px] mq750:box-border">
         <div className="w-[1440px] h-[570px] relative bg-azure hidden max-w-full" />
         <InputSymp/>
        </div>
         

         <Footer />
       </section>
     </div>
   );    
};

export default InputPage;
