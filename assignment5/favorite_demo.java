import java.util.ArrayList;

import org.w3c.dom.Node;


public class Rack{
  ArrayList<Node> rack = new ArrayList<Node>();

  public Rack(){
  }

  //Plasserer en node i rack.
  public void insertNode(Node node){
    rack.add(node);
    System.out.println("Node inserted.");
  }

  //Antall noder.
  public int numbNodes(){
    int arrayLength = rack.size();
    return arrayLength;
  }

  /*Bruker teller til å finne antall prosessorer.*/
  public int numbCpu(){
    int numb = 0;
    while(numb < rack.size()){
      Node e = rack.get(counter);
      int f = e.numbCpu();
      numb += f;
    }
    return numb;
  }

  //Beregner antall noder i racket med minne over gitt grense.
  public int enoughMem(int minMem){
    int nodes = 0;
    for (int counter = 0; counter < rack.size(); counter++){
      Node f = rack.get(counter);
      if (f.enoughMem(minMem) == true) {
        nodes++;
      }
    }
    return nodes;
  }
}
