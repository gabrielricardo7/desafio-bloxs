import { Link } from "react-router-dom";
import { AppBar, Box, Toolbar, Typography } from "@mui/material";

const Nav = () => {
  const routes = [
    { link: "/", title: "Início" },
    { link: "/abrir", title: "Abrir" },
    { link: "/deposito", title: "Depósito" },
    { link: "/saldo", title: "Saldo" },
    { link: "/saque", title: "Saque" },
    { link: "/bloqueio", title: "Bloqueio" },
    { link: "/extrato", title: "Extrato" },
  ];

  return (
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" color="transparent" sx={{bgcolor: "black"}}>
        <Toolbar sx={{alignContent: "center"}}>
          {routes.map((x) => (
            <Typography
              variant="h6"
              component="div"
              sx={{ flexGrow: 1 }}
              key={x.title}
            >
              <Link to={x.link}>{x.title}</Link>
            </Typography>
          ))}
        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default Nav;
