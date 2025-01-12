import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./components/landingPage/LandingPage";
import QuestionPage1 from "./components/question1/QuestionPage1";
import QuestionPage2 from "./components/question2/QuestionPage2";
import RecommendationPage from "./components/recommendations/RecommendationPage";
import { Feedback } from "@mui/icons-material";
import Header from "./components/Header";
import Footer from "./components/Footer";

function App() {
  return (
    <Router>
      <main style={{ minHeight: "100vh", minWidth: "100vw" }}>
        {/* Header */}
        <Header />
        <Routes>
          <Route path="/" element={<LandingPage />} />
          <Route path="/question1" element={<QuestionPage1 />} />
          <Route path="/question2" element={<QuestionPage2 />} />
          <Route path="/recommendation" element={<RecommendationPage />} />
          <Route path="/feedback" element={<Feedback />} />
        </Routes>
        {/* Footer */}
        <Footer />
      </main>
    </Router>
  );
}

export default App;
