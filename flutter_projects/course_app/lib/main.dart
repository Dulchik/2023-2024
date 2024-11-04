import 'package:flutter/material.dart';
import 'package:course_app/gradient_container.dart';

void main() {
  runApp(
    const MaterialApp(
      home: Scaffold(
        body: GradientContainer(Color.fromARGB(255, 242, 114, 105),
            Color.fromARGB(255, 232, 56, 43)),
      ),
    ),
  );
}
