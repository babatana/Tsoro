import java.util.*;

public class Main{
  public static void main(String args[]) {
    ArrayList <Integer> init_board = new ArrayList<Integer>(
	Arrays.asList(0, 0, 0, 0, 4, 4, 4, 4));    
    
    Tsoro game = new Tsoro(init_board);
    game.showBoard();
    game.makeMove(5);
    game.showBoard();
  }
}


