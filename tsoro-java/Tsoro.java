import java.util.*;

public class Tsoro{
  ArrayList<Integer> board;

  public Tsoro() {
    Integer currHole = 0; 
    Integer destHole = 0; 
    Integer hand = 0;

  }

  public ArrayList<Integer> initboard(Integer boardSize, Integer stonesPerhole) {
    
    return board;
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


}