import "./App.css";
import { BrowserRouter } from "react-router-dom";
import Nav from "./components/Nav";
import AppRoutes from "./routes";

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Nav />
        <AppRoutes />
      </BrowserRouter>
    </div>
  );
}

export default App;
