***POKER GAME***


We want to create a small simulation of the game of Poker.
To do this, implement the following classes:


**Card**: each characterized by a suit and a value
using own enumeration types. The class allows you to:
create suit and value data cards;
+ obtain its seed;
+ obtain its value;
+ get the matching 2 character string: <Value><Seed>
(e.g. "Qp" for Q of spades, "3q" for 3 of diamonds,
"Ac" for ace of hearts, "Xf" for the 10 of 1gold);


**Deck**: linear structure of 52 distinct cards; the class must have 
methods for:
+ create an initial deck of cards sorted by suit and by value;
+ shuffling the deck;
+ return (eliminating) his first n cards, with 1 n 5;
+ get the number of cards contained;


**Hand**: Consisting of 5 cards, with methods for:
+ scoring† as its own enumeration type;
+ get a hand in the form of string;
+ return his card collection;
+ replace some cards with as many cards (drawn from the deck) 
  supplied as parameters;


**Game**: having its deck of cards and its own
collection of 5 hands, with methods for
+ create his deck, shuffle it and create the starting hand collection;
+ request the replacement of a number of cards in
one of the hands (passed as parameters) by drawing them
from the deck;
+ get a string representing hands and respective scores;


**Test**: containing the main() method which, using the classes
implemented,
1. For 4 simulated matches:
   + create a new game and print it, also a video, its initial state;
   + manage the replacement of cards of hands of the match with 50% probability;
   + print the number of cards left after substitutions;
   + calculate the scores of each hand thus obtained;
   + print the highest scoring hand;
2. Save the simulated games on text files


----
_**Score Point**_: 
+ **Pair** (2 cards of the same rank); 
+ **Double Couple** (2 couples);
+ **Tris** (3 cards with the same value);
+ **Straight** (5 cards with consecutive ranks);
+ **Flush** (5 cards of the same suit);
+ **Full** (pair + three of a kind);
+ **Poker** (4 cards with the same value);
+ **Straight Flush** (straight of cards of the same suit).