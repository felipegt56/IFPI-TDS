void main() {
  List frutas = ['Banana', 'Maça', 'Mamão', 'Limão', 'Laranja'];
  List preco = [5.99, 7.98, 3.00, 1.99, 4.50];

  int indice = 0;

  Map tabela={frutas[indice]:preco[indice].toStringAsFixed(2)};

  print(tabela);
}