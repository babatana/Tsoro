import java.util.*; 

public class Tsoro {
  ArrayList<Integer> board;
  int hand;	
  int currHole;
  int nextHole;
  int destHole;

  public Tsoro(ArrayList<Integer> initBoard){
    board = initBoard;
    hand = 0;
    currHole = 0;
    nextHole = currHole+1;;
    destHole = 0;
  }

  public void showBoard() {
    int row = board.size()/2;
    
    // top row
    System.out.println("______________");
    System.out.print("[");
    for (int j = board.size()-1; j >= row; j--) {
        System.out.print(" " + board.get(j) + " ");
    }
    System.out.println("]");
    
    // bottom row
    System.out.print("[");
    for (int i = 0; i < row; i++) {
      System.out.print(" " + board.get(i) + " ");   
    }
    System.out.println("]");
  }
  
  protected void checkIfOutOfIndex() {
    if (currHole >= board.size() || nextHole >= board.size()) {
      currHole -= board.size();
      nextHole -= board.size();
    }
  } 

  protected ArrayList<Integer> makeMove (int handIndex) {
    System.out.println("Move");

    if (board.get(handIndex) > 0) {
      hand = board.get(handIndex);      
      board.set(handIndex, 0);
      currHole = handIndex+1;
    } else {
      System.out.println("You selected an empty hand, hole " + currHole);
    }
    
    while (hand > 0) {
      // avoid out-of-range error 
      if (currHole >= board.size()) {
        currHole -= board.size();
      }
 
      if (hand == 1 && board.get(currHole) == 0) {
        int emptyHoleTracker = 0;
        while (board.get(nextHole) == 0) {
          if (currHole >= board.size() || nextHole >= board.size()) {
            currHole -= board.size();
            nextHole -= board.size();
          }
          currHole++;
          nextHole++;
          if (currHole >= board.size() || nextHole >= board.size()) {
            currHole -= board.size();
            nextHole -= board.size();
          }
        }
      }

      if (hand == 1 && currHole == board.size()Z) {
        System.out.println("Move complete!");
        return board;
      }
      board.set(currHole, board.get(currHole)+1);
      hand -= 1;
      currHole++; 	
    }
    showBoard();
    return board;
  }
}

