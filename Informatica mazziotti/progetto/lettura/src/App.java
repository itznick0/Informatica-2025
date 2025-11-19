import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;


public class App {
    public static void main(String[] args) throws FileNotFoundException {
        Scanner scanner = new Scanner(new File("Informatica mazziotti\\progetto\\utenti.csv"));
        while (scanner.hasNextLine()) {
            String riga = scanner.nextLine();
            System.out.println(riga);
        }
    }
}