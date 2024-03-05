import NavBar2 from "../components/navbar2";

import Footer from "../components/footer";
import InputSymp from "../components/inputsymp";

const InputPage = () => {
  return (
   
       <div className="w-full h-full bg-white overflow-hidden flex flex-col items-start justify-start gap-[217px_0px] tracking-[normal] text-left text-mini text-white font-inter mq450:gap-[217px_0px] mq750:h-auto mq750:gap-[217px_0px]">
       <section className="self-stretch flex flex-col items-start justify-start max-w-full shrink-0">
         <NavBar2 />
       
     
         <InputSymp/>

         <Footer />
       </section>
     </div>
   );    
};

export default InputPage;
