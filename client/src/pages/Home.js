import "../App.css";
import { Box, Typography } from "@mui/material";

function Home() {
  return (
    <>
      <Box
        display="flex"
        flexDirection="column"
        justifyContent="center"
        alignItems="center"
        height="42vh"
        margin="auto"
      >
        <Typography variant="h4" component="h1">
          Início - Sobre:
        </Typography>
        <Typography variant="h6" component="p">
          Desafio Full-Stack Developer (Python/Flask) Bloxs
        </Typography>
        <Typography variant="p" component="p">
          Aplicação web feita com React.JS que faz operações bancárias via API
        </Typography>
      </Box>
      <Typography variant="p" component="p" backgroundColor="#282c34" color="white">
        Copyright &copy; 2023 Gabriel Ricardo (
        <a
          rel="noopener noreferrer"
          target="_blank"
          href="https://github.com/gabrielricardo7"
        >
          gabrielricardo7
        </a>
        )
      </Typography>
    </>
  );
}

export default Home;
