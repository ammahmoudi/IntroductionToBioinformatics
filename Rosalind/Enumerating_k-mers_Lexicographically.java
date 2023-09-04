import java.util.Arrays;
import java.util.LinkedList;
import java.util.List;

public class Problem3 {
    public static void main(String[] args) {

        char[] alphabets ={'A','B','C','D'};

        int n = 2;
        LinkedList<String> outputs = new LinkedList<>();
        char[] tchat=new char[n];
        Arrays.fill(tchat,alphabets[0]);
        recursive(n-1,n,alphabets,outputs,tchat);
        System.out.println(outputs);

    }
    public static LinkedList<String> recursive(int level,int n,char[] alphabets,LinkedList<String> outputs,char[] tempChar){
        char[] c = new char[n];
        int[] num=new int[n];
        Arrays.fill(num,0);
        for (int i = n-1; i >= level; i--) {
            for (int a = 0; a < alphabets.length; a++) {
                tempChar[i]=alphabets[a];
                  outputs.add(String.valueOf(tempChar));

            }
            level--;
            recursive(level,n,alphabets,outputs,tempChar);


        }
        return outputs;
    }
}
