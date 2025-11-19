import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class App {
    public static void main(String[] args) throws Exception {
        if (args.length != 3) {
            System.err.println("Errore: Nome, Cognome, Età richiesti");
            System.exit(1);
        }

        String nome = args[0];
        String cognome = args[1];
        String eta = args[2];
        
        String rigaUtente = nome + ";" + cognome + ";" + eta;

        try (
            FileWriter fw = new FileWriter("Informatica mazziotti\\progetto\\utenti.csv", true);
            PrintWriter out = new PrintWriter(fw)
        ) {
            out.println(rigaUtente); 
            
            System.out.println("Utente " + nome + " salvato");
            
        } catch (IOException e) {
            System.err.println("Errore durante la scrittura sul file: " + e.getMessage());
        }
    }
}