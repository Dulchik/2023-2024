import 'package:flutter/material.dart';
import 'dart:convert';
import 'package:http/http.dart' as http;

class QuoteScreen extends StatefulWidget {
  const QuoteScreen({super.key});

  @override
  State<QuoteScreen> createState() => _QuoteScreenState();
}

class _QuoteScreenState extends State<QuoteScreen> {
  String quote = 'Here will be displayed the Quote of the day';

  Future<void> fetchQoute() async {
    final response = await http.get(
      Uri.parse('https://api.api-ninjas.com/v1/quotes'),
      headers: {'X-Api-Key': 'jER9cvGuv2dbBT86jY1JNw==7i3HiaHGNno0cSSj'},
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      setState(() {
        quote = data[0]['quote'];
      });
    } else {
      throw Exception('Failed to load quote');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: Text('Qoute of the day'),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 30),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                quote,
                textAlign: TextAlign.center,
                style: TextStyle(fontSize: 24),
              ),
              SizedBox(height: 32),
              ElevatedButton(
                onPressed: fetchQoute,
                child: Text('New Quote'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
