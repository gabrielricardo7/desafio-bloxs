import { Route, Routes } from "react-router-dom";
import Home from "../pages/Home";
import Abrir from "../pages/Abrir";

function AppRoutes() {
  return (
      <Routes>
        <Route element={<Home />} path="/" exact />
        <Route element={<Abrir />} path="/abrir" />
      </Routes>
  );
}

export default AppRoutes;
