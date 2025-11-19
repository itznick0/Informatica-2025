import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        String codice, quantita, linee;
        Scanner scanner;
        String[] parts;
        int newS;
        String[] lineee = new String[99999999]; // massime righe 100
        boolean trovato = false;

        if (args.length == 2) {
            codice = args[0];
            quantita = args[1];
            if (Integer.parseInt(quantita)>0){ 
                scanner = new Scanner(new File("../../dati/prodotti.csv"));
                int i = 0;
                // cambiato logica operando su una'array di stringhe contenente le linee invece che sulle linee stesse
                while (scanner.hasNextLine()) {
                    lineee[i]=scanner.nextLine();
                    i++;
                }
                scanner.close();
                try (
                    FileWriter fw = new FileWriter("../../dati/prodotti.csv", false);
                    PrintWriter out = new PrintWriter(fw)
                ) {
                    for (int j=0; j<i; j++){
                        linee = lineee[j];
                        if (linee.startsWith(codice)&&Integer.parseInt(codice)>100){
                            trovato = true;
                            parts = linee.split(";");
                            if (Integer.parseInt(quantita) > Integer.parseInt(parts[3])) {
                                System.out.println("Errore 3" + parts[3]); 
                                out.println(linee);
                            } else {
                                newS = Integer.parseInt(parts[3]) - Integer.parseInt(quantita);
                                out.println(parts[0] + ";" + parts[1] + ";" + parts[2] + ";" + newS);
                                System.out.println(parts[1] + ";" + parts[2] + ";" + newS);
                            } 
                        } else {
                            out.println(linee);
                        }
                    }
                    if (!trovato) {
                        System.out.println("Errore 4");
                    }
                }                                 
                catch (IOException e) {
                    System.err.println("Errore 5");
                }
            } else {
                System.out.println("Errore 6");
            }
        } else {
            System.err.println("Errore 7");
        }

    }
}