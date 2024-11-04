import 'package:course_app/dice_roller.dart';
import 'package:flutter/material.dart';

const startALignment = Alignment.bottomCenter;
const endALignment = Alignment.topCenter;

class GradientContainer extends StatelessWidget {
  const GradientContainer(this.color1, this.color2, {super.key});

  final Color color1;
  final Color color2;

  @override
  Widget build(context) {
    return Container(
      decoration: BoxDecoration(
        gradient: LinearGradient(
          colors: [color1, color2],
          begin: startALignment,
          end: endALignment,
        ),
      ),
      child: Center(
        child: DiceRoller(),
      ),
    );
  }
}
