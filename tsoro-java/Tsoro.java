import java.util.*; 

public class Tsoro {
  ArrayList<Integer> board;
  int hand;
  int currHole;

  public Tsoro(ArrayList<Integer> initBoard){
    board = initBoard;; 
    hand = 0;
    currHole = 0;
  }

  public void showBoard() {
    int row = board.size()/2;
    
    // top row
    System.out.println("______");
    System.out.print("[");
    for (int j = row; j < board.size(); j++) {
        System.out.print(board.get(j));
    }
    System.out.println("]");

    // bottom row
    System.out.print("[");
    for (int i = 0; i < row; i++) {
      System.out.print(board.get(i));  
    }
    System.out.println("]");
  }

  protected ArrayList<Integer> makeMove (int handIndex) {
    hand = board.get(handIndex);
    if (hand > 0) { 
      currHole = handIndex+1;
      if (hand == 1 && board.get(currHole+1) == 0) {
	while (board.get(currHole)+1 == 0) {
	  currHole++;
	}
      }
      while (hand > 0) {
 	if (currHole == board.size()) {
          currHole -= board.size();
	}
      board.set(currHole, board.get(currHole)+1);
      hand -= 1;
      }        
    } else if (hand == 0 && currHole == 0) {
	System.out.println("Move complete!");
    } else {
      System.out.println("Please select a non-empty hand");
    }
    return board;
  }
}

