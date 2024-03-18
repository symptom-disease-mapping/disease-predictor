import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import {
  Route,
  RouterProvider,
  createBrowserRouter,
  createRoutesFromElements,
} from "react-router-dom";
import Layout from "./Layout.jsx";
import HeroPage from "./pages/heroPage.jsx";
import SignInPage from "./pages/signInPage.jsx";
import SignUpPage from "./pages/signUpPage.jsx";
import InfoPage from "./pages/infoPage.jsx";
import InputPage from "./pages/inputPage.jsx";
import QuestionPage from "./pages/questionPage.jsx";
import ReportPage from "./pages/ReportPage.jsx";

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<Layout />}>
      <Route path="/" element={<HeroPage />} />
      <Route path="symptomchecker" element={<InfoPage />} />
      <Route path="symptomchecker">
        <Route path="inputpage" element={<InputPage />} />
        <Route path="inputpage">
          <Route path="questionpage" element={<QuestionPage />} />
          <Route path="questionpage">
              <Route  path="reportpage" element={<ReportPage/>} />
          </Route>
        </Route>
      </Route>
      <Route path="signin" element={<SignInPage />} />
      <Route path="signup" element={<SignUpPage />} />
    </Route>
  )
);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
