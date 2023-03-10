import axios from "axios";
import { useState } from "react";
import { Box, Button, TextField, Typography } from "@mui/material";
import { Send } from "@mui/icons-material";
import { formatCpf, formatDate } from "../utils";

function Extrato() {
  const [idConta, setIdConta] = useState(null);
  const [msg, setMsg] = useState(null);
  const [data, setData] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    setData(null);
    axios({
      url: `/extrato/${idConta}`,
      method: "GET",
    })
      .then((response) => {
        if (response.status === 200) {
          setData(response.data);
          setMsg(null);
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
        Recuperar Extrato
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
        <Box display="flex" alignItems="center" justifyContent="center">
          <TextField
            required
            id="outlined-required"
            label="ID da Conta"
            type="number"
            onChange={(e) => setIdConta(e.target.value)}
          />
          <Button variant="contained" type="submit" endIcon={<Send />}>
            Enviar
          </Button>
        </Box>
      </Box>
      <div>{msg ? <p>{msg}</p> : null}</div>
      <div>
        {data ? (
          <Box>
            <Typography variant="h5" component="h2">
              Extrato
            </Typography>
            <p>ID da Conta: {data.idConta}</p>
            <p>ID da Pessoa: {data.idPessoa}</p>
            <p>Nome: {data.nome}</p>
            <p>CPF: {formatCpf(data.cpf)}</p>
            <p>Data de Nascimento: {formatDate(data.dataNascimento)}</p>
            {data.extrato.map((x) => (
              <Box
                key={x.idTransacao}
                sx={x.tipo === "saque" ? { color: "red" } : { color: "blue" }}
              >
                <hr />
                <p>ID da Transação: {x.idTransacao}</p>
                <p>Valor: R$ {x.valor.toFixed(2)}</p>
                <p>Data/Hora: {x.dataTransacao}</p>
                <p>Tipo: {x.tipo}</p>
              </Box>
            ))}
          </Box>
        ) : null}
      </div>
    </>
  );
}

export default Extrato;
