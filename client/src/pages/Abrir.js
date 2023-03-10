import axios from "axios";
import { useState } from "react";
import { formatCpf, formatDate } from "../utils";
import { Box, Button, TextField, Typography } from "@mui/material";
import { Send } from "@mui/icons-material";

function Abrir() {
  const [idPessoa, setIdPessoa] = useState(null);
  const [saldo, setSaldo] = useState(null);
  const [limiteSaqueDiario, setLimiteSaqueDiario] = useState(null);
  const [tipoConta, setTipoConta] = useState(null);
  const [msg, setMsg] = useState(null);
  const [conta, setConta] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    setConta(null);
    const body = {
      idPessoa: idPessoa,
      saldo: saldo,
      limiteSaqueDiario: limiteSaqueDiario,
      tipoConta: tipoConta,
    };
    axios({
      url: "/abrir",
      method: "POST",
      data: body,
    })
      .then((response) => {
        if (response.status === 201) {
          setConta(response.data);
          setMsg("Conta criada com sucesso.");
        }
      })
      .catch((error) => {
        if (error.response) {
          setMsg(`Erro: ${error.response.status} - Tente novamente.`);
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
  };

  return (
    <>
      <Typography variant="h4" component="h1">
        Abrir Conta
      </Typography>
      <Box
        component="form"
        sx={{
          "& .MuiTextField-root": { m: 1, width: "25ch" },
        }}
        noValidate
        autoComplete="off"
        onSubmit={handleSubmit}
      >
        <div>
          <TextField
            required
            id="outlined-required"
            label="ID da Pessoa"
            type="number"
            onChange={(e) => setIdPessoa(e.target.value)}
          />
          <TextField
            required
            id="outlined-required"
            label="Saldo"
            type="number"
            onChange={(e) => setSaldo(e.target.value)}
          />
          <TextField
            required
            id="outlined-required"
            label="Limite de Saque Diário"
            type="number"
            onChange={(e) => setLimiteSaqueDiario(e.target.value)}
          />
          <TextField
            required
            id="outlined-required"
            label="Tipo de Conta"
            type="number"
            onChange={(e) => setTipoConta(e.target.value)}
          />
        </div>
        <Button variant="contained" type="submit" endIcon={<Send />}>
          Enviar
        </Button>
      </Box>
      <div>{msg ? <p>{msg}</p> : null}</div>
      <div>
        {conta ? (
          <Box>
            <hr />
            <Typography variant="h5" component="h2">
              Conta
            </Typography>
            <p>ID da Conta: {conta.idConta}</p>
            <p>Saldo: R$ {conta.saldo.toFixed(2)}</p>
            <p>
              Limite de Saque Diário: R$ {conta.limiteSaqueDiario.toFixed(2)}
            </p>
            <p>Flag Ativo: {conta.flagAtivo ? "sim" : "não"}</p>
            <p>Tipo de Conta: {conta.tipoConta}</p>
            <p>Data de Criação:{formatDate(conta.dataCriacao)}</p>
            <hr />
            <Typography variant="h5" component="h2">
              Pessoa
            </Typography>
            <p>ID da Pessoa: {conta.pessoa.idPessoa}</p>
            <p>Nome: {conta.pessoa.nome}</p>
            <p>CPF: {formatCpf(conta.pessoa.cpf)}</p>
            <p>Data de Nascimento: {formatDate(conta.pessoa.dataNascimento)}</p>
          </Box>
        ) : null}
      </div>
    </>
  );
}

export default Abrir;
