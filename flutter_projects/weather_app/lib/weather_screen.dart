import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:intl/intl.dart';
import 'dart:convert';

class WeatherScreen extends StatefulWidget {
  const WeatherScreen({super.key});

  @override
  State<WeatherScreen> createState() => _WeatherScreenState();
}

class _WeatherScreenState extends State<WeatherScreen> {
  double temperature = 0.0;

  @override
  void initState() {
    super.initState();
    fetchTemperature('Amsterdam').then((temp) {
      setState(() {
        temperature = temp;
      });
    });
  }

  Future<double> fetchTemperature(String city) async {
    final response = await http.get(
      Uri.parse(
          'https://api.weatherapi.com/v1/current.json?key=be1079228d714a5da07141158243110&q=$city'),
    );

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      return data['current']['temp_c'];
    } else {
      throw Exception('Failed to load temperature');
    }
  }

  @override
  Widget build(BuildContext context) {
    DateTime now = DateTime.now();
    String formattedDate = DateFormat('dd.MM.yyyy').format(now);

    return Scaffold(
      appBar: AppBar(
        title: Text('Weather App'),
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(40),
          child: Column(
            children: [
              Text(formattedDate),
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Icon(Icons.cloud),
                  Text('Temperature: $temperature°C'),
                ],
              ),
              Text('Location'),
              Text('Weather'),
            ],
          ),
        ),
      ),
    );
  }
}


// API Key: be1079228d714a5da07141158243110