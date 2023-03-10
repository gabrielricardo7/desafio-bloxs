import { Route, Routes } from "react-router-dom";
import Home from "../pages/Home";
import Abrir from "../pages/Abrir";
import Deposito from "../pages/Deposito";
import Saldo from "../pages/Saldo";
import Saque from "../pages/Saque";
import Bloqueio from "../pages/Bloqueio";
import Extrato from "../pages/Extrato";

function AppRoutes() {
  return (
    <Routes>
      <Route element={<Home />} path="/" exact />
      <Route element={<Abrir />} path="/abrir" />
      <Route element={<Deposito />} path="/deposito" />
      <Route element={<Saldo />} path="/saldo" />
      <Route element={<Saque />} path="/saque" />
      <Route element={<Bloqueio />} path="/bloqueio" />
      <Route element={<Extrato />} path="/extrato" />
    </Routes>
  );
}

export default AppRoutes;
