import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    title: "Navegation Basics",
    initialRoute: '/primeira',
    routes: {
      '/primeira': (context) => FirstRoute(),
      '/segunda': (context) => SecondRoute(),
    },
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
            Navigator.pushNamed(context, '/segunda');
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
            Navigator.pushNamed(context, '/primeira');
          },
        ),
      ),
    );
  }
}