export const formatCpf = (n) => {
  const cpf = n.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/g, "$1.$2.$3-$4");

  return cpf;
};
export const formatDate = (dt) => {
  const ndt = new Date(Date.parse(dt)).toLocaleDateString("pt-BR");

  return ndt;
};
