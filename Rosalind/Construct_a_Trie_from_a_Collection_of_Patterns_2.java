import java.util.LinkedList;
import java.util.Scanner;

public class Problem4_2 {

    static final int ALPHABET_SIZE = 26;
    static class TrieNode {
        int id;
        static int lastId = 0;
        static LinkedList<TrieNode> allNodes=new LinkedList<>();
        TrieNode[] children = new TrieNode[ALPHABET_SIZE];
        LinkedList<Edge> edges;
        boolean isEndOfWord;
        TrieNode() {
            id = lastId++;
            edges = new LinkedList<>();
            allNodes.add(this);
            for (int i = 0; i < ALPHABET_SIZE; i++)
                children[i] = null;
        }
    }

    static TrieNode root;

    static class Edge {
        static LinkedList<Edge> edges = new LinkedList<>();
        TrieNode father;
        TrieNode child;
        char content;

        @Override
        public String toString() {
            return father.id + "->" + child.id + ":" + content;
        }
    }

    static void insert(String key) {
        int level;
        int length = key.length();
        int index;
        TrieNode pointer = root;

        for (level = 0; level < length; level++) {
            index = key.charAt(level) - 'A';
            if (pointer.children[index] == null) {
                pointer.children[index] = new TrieNode();
                System.out.println(pointer.id + "->" + pointer.children[index].id + ":" + key.charAt(level));
            }
            boolean found = false;
            TrieNode child = null;
            for (Edge edges : pointer.edges) {
                if (edges.content == key.charAt(level)) {
                    child = edges.child;
                    found = true;
                }
            }
            if (!found) {
                //  System.out.println("not found");
                Edge edge = new Edge();
                edge.father = pointer;
                edge.content = key.charAt(level);
                edge.child = new TrieNode();
                Edge.edges.add(edge);
                child = edge.child;
                pointer.edges.add(edge);

            }
//            pointer = pointer.children[index];
            pointer = child;
        }
        pointer.isEndOfWord = true;

    }


    // Driver
    public static void main(String args[]) {
        //Scanner scanner = new Scanner(System.in);
        String input;
     //   input = scanner.nextLine();
        input="";
        String[] keys;
        keys = input.split("\n");
     //   System.out.println(input);
         //  keys = new String[]{"ATAGA", "ATC", "GAT"};
        root = new TrieNode();


        for (int i = 0; i < keys.length; i++) {
          //  System.out.println(keys[i]);
            insert(keys[i]);
        }
       Edge.edges.forEach((Edge e) -> System.out.println(e.toString()));
        for(TrieNode trieNode:TrieNode.allNodes){
            trieNode.edges.forEach((e)-> System.out.println(e));
        }

    }
}

