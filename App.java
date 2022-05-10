import java.util.Arrays;

public class App {
    public static void main(String[] args) throws Exception {
        int size = 5;
        int[][] arr = new int[size][size];
        int i = 5 / 2;
        int counter = 1;
        for (int r = 0; r < size; r++) {
            for (int c = 0; c < size; c++) {
                arr[i][i] = counter;
            }
        }

        for (int[] x: arr) {
            System.out.println(Arrays.toString(x));
        }
    }
}