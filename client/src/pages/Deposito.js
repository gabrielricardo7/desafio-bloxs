import axios from "axios";
import { useState } from "react";
import { Box, Button, TextField, Typography } from "@mui/material";
import { Send } from "@mui/icons-material";

function Deposito() {
  const [idConta, setIdConta] = useState(null);
  const [valor, setValor] = useState(null);
  const [msg, setMsg] = useState(null);
  const [data, setData] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    setData(null);
    const body = {
      valor: parseInt(valor),
    };
    axios({
      url: `/deposito/${idConta}`,
      method: "POST",
      data: body,
    })
      .then((response) => {
        if (response.status === 200) {
          setData(response.data);
          setMsg(null);
        }
      })
      .catch((error) => {
        if (error.response) {
          setMsg(error.response.data.msg);
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
  };

  return (
    <>
      <Typography variant="h4" component="h1">
        Realizar Depósito
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
          <TextField
            required
            id="outlined-required"
            label="Valor"
            type="number"
            onChange={(e) => setValor(e.target.value)}
          />
          <Button variant="contained" type="submit" endIcon={<Send />}>
            Enviar
          </Button>
        </Box>
      </Box>
      <div>{msg ? <p>{msg.toUpperCase()}</p> : null}</div>
      <div>
        {data ? (
          <Box>
            <Typography variant="h5" component="h2">
              Depósito
            </Typography>
            <p>ID da Transação: {data.idTransacao}</p>
            <p>Valor: R$ {data.valor.toFixed(2)}</p>
            <p>Data/Hora: {data.dataTransacao}</p>
            <p>Tipo: {data.tipo}</p>
            <p>ID da Conta: {data.idConta}</p>
          </Box>
        ) : null}
      </div>
    </>
  );
}

export default Deposito;
