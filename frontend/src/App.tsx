import "./App.css";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "./components/landingPage/LandingPage";
import QuestionPage1 from "./components/question1/QuestionPage1";
import QuestionPage2 from "./components/question2/QuestionPage2";
import RecommendationPage from "./components/recommendations/RecommendationPage";
import Feedback from "./components/feedback/Feedback";
import Header from "./components/Header";
import Footer from "./components/Footer";
import { SelectionProvider } from "./context/SelectionContext"; // Import SelectionProvider

function App() {
  return (
    <SelectionProvider> {/* Der Kontext umschließt die gesamte App */}
      <Router>
        <main style={{ minHeight: "100vh", minWidth: "100vw" }}>
          {/* Header */}
          <Header />
          <Routes>
            {/* Landing Page */}
            <Route path="/" element={<LandingPage />} />

            {/* Question Pages */}
            <Route path="/question1" element={<QuestionPage1 />} />
            <Route path="/question2" element={<QuestionPage2 />} />

            {/* Recommendation Page */}
            <Route path="/recommendation" element={<RecommendationPage />} />

            {/* Feedback Page */}
            <Route path="/feedback" element={<Feedback />} />
            </Routes>
          {/* Footer */}
          <Footer />
        </main>
      </Router>
    </SelectionProvider>
  );
}

export default App;
