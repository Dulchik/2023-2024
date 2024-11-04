import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      home: Scaffold(
        body: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
              colors: [
                Color.fromARGB(255, 56, 19, 120),
                Color.fromARGB(255, 89, 46, 164)
              ],
              begin: Alignment.topLeft,
              end: Alignment.bottomRight,
            ),
          ),
          child: Center(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Image.asset(
                  'assets/images/quizlogo.png',
                  width: 300,
                ),
                const SizedBox(
                  height: 60,
                ),
                Text(
                  'Learn FLutter the fun way!',
                  style: const TextStyle(
                    color: Colors.white70,
                    fontSize: 24,
                  ),
                ),
                const SizedBox(
                  height: 40,
                ),
                ElevatedButton(
                  onPressed: () {},
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Color.fromARGB(255, 72, 31, 143),
                    shape: ContinuousRectangleBorder(),
                  ),
                  child: Text(
                    'Start Quiz',
                    style: TextStyle(
                      color: Colors.white70,
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    ),
  );
}
