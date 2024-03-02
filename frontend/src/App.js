import Title from "./components/Title";
import Footer from "./components/Footer";
import TemplateOne from "./components/Templateone";
import FormContainer from "./components/FormContainer";


function App() {
  return (
    <>
      <Title />
      <div className="container">
        <FormContainer />
        <TemplateOne />

      </div>

      <Footer />
    </>
  );
}

export default App;
