import java.util.Arrays;
import java.util.Scanner;

public class Problem2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();
        //  String input="ACGCACT";
        char[] output = new char[input.length()];
        char[] inputCharArray = input.toCharArray();
        for (int i = 0; i < inputCharArray.length; i++) {
            char newChar;
            switch (inputCharArray[i]) {
                case 'A':
                    newChar = 'T';
                    break;
                case 'G':
                    newChar = 'C';
                    break;
                case 'C':
                    newChar = 'G';
                    break;

                default:
                    newChar = 'A';
            }
            output[inputCharArray.length - i - 1] = newChar;
        }
        System.out.println(new String(output));
    }
}
