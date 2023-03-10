import axios from "axios";
import { useState } from "react";
import { Box, Button, TextField, Typography } from "@mui/material";
import { Send } from "@mui/icons-material";

function Bloqueio() {
  const [idConta, setIdConta] = useState(null);
  const [data, setData] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    setData(null);
    axios({
      url: `/bloqueio/${idConta}`,
      method: "POST",
    })
      .then((response) => {
        if (response.status === 200) {
          setData(response.data);
        }
      })
      .catch((error) => {
        if (error.response) {
          setData(error.response.data);
          console.log(error.response);
          console.log(error.response.status);
          console.log(error.response.headers);
        }
      });
  };

  return (
    <>
      <Typography variant="h4" component="h1">
        Bloquear Conta
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
      <Typography variant="h5" component="h2">
        {data ? <p>{data.msg.toUpperCase()}</p> : null}
      </Typography>
    </>
  );
}

export default Bloqueio;
