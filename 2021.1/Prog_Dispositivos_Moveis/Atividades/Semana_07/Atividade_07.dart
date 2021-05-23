class Veiculo{
  double velocidade;
  String cor;
  double peso;
  Veiculo(this.velocidade,this.cor,this.peso);}

class Carro extends Veiculo{
Carro(double velocidade, String cor, double peso): super(velocidade,cor,peso);}

class Aviao extends Veiculo{
  int quantidade_h;
  
Aviao(double velocidade, String cor, double peso, this.quantidade_h): super(velocidade,cor,peso);}

void main() {
  Carro carro1 = Carro(60,'Vermelhor',900);
  print('Carro');
  print('Velocidade: ${carro1.velocidade}' + ' Km/h');
  print('Cor: ${carro1.cor}');
  print('Peso: ${carro1.peso}' + ' Kg');
  
  print('');
  
  Aviao aviao1 = Aviao(120,'Preto com Branco', 1000, 2);
  print('Avião');
  print('Velocidade: ${aviao1.velocidade}' + ' Km/h');
  print('Cor: ${aviao1.cor}');
  print('Peso: ${aviao1.peso}' + ' Kg');
  print('número de hélices: ${aviao1.quantidade_h}');
}