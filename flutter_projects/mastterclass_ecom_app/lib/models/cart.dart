import 'package:flutter/material.dart';
import 'package:mastterclass_ecom_app/models/shoe.dart';

class Cart extends ChangeNotifier {
  List<Shoe> shoeShop = [
    Shoe(
      name: 'Air Jordan',
      price: '236',
      imagePath: 'lib/images/air_jordan.png',
      description: 'description',
    ),
    Shoe(
      name: 'Air Jordan Retro Blue',
      price: '236',
      imagePath: 'lib/images/jordan_retro_blue.png',
      description: 'description',
    ),
    Shoe(
      name: 'Air Jordan Retro',
      price: '236',
      imagePath: 'lib/images/jordan_retro.png',
      description: 'description',
    ),
    Shoe(
      name: 'Jordan Seafoam',
      price: '236',
      imagePath: 'lib/images/jordan_seafoam.png',
      description: 'description',
    ),
    Shoe(
      name: 'Jordan Seafoam',
      price: '236',
      imagePath: 'lib/images/jordan.png',
      description: 'description',
    ),
  ];

  List<Shoe> userCart = [];

  List<Shoe> getShoeList() {
    return shoeShop;
  }

  List<Shoe> getUserCart() {
    return userCart;
  }

  void addItemToCart(Shoe shoe) {
    userCart.add(shoe);
    notifyListeners();
  }

  void removeItemFromCart(Shoe shoe) {
    userCart.remove(shoe);
    notifyListeners();
  }
}
