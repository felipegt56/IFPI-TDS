import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    title: "Navegation Basics",
    home: FirstRoute(),
    theme: ThemeData(
    primarySwatch: Colors.pink,
    ),
  ));
}

class FirstRoute extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Primeira Pagina'),
      ),
      body: Center(
        child: ElevatedButton(
          child: Text('Abrir segunda rota'),
          onPressed: () {
            Navigator.push(context,MaterialPageRoute(builder: (context) => SecondRoute()),);
          },
        ),
      ),
    );
  }
}


class SecondRoute extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Daiana De Sousa Pinto"),
      ),
      body: Center(
        child: ElevatedButton(
          child: Text('Retornar!'),
          onPressed: () {
            Navigator.pop(context);
          },
        ),
      ),
    );
  }
}
