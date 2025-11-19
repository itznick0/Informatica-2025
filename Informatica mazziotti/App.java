import java.io.*;

public class App {
    public static void main(String args[]) {
        if (args.length < 2) {
            System.out.println("ERRORE: Inserisci codice e quantita");
            return;
        }
        String codiceCercato = args[0];
        String testoQuantita = args[1];
        int quantitaVendere = 0;
        try {quantitaVendere = Integer.parseInt(testoQuantita);
            if (quantitaVendere <= 0) {
                System.out.println("ERRORE: La quantità deve essere positiva");
                return;
            }
        } catch (Exception e) {
            System.out.println("ERRORE: La quantità deve essere un numero");
            return;
        }
        int righeTotali = 0;
        try {BufferedReader conta = new BufferedReader(new FileReader("../../dati/prodotti.csv"));
            String lineaContatore = conta.readLine();
            while (lineaContatore != null) {
                righeTotali = righeTotali + 1;
                lineaContatore = conta.readLine();
            }
            conta.close();
        } catch (Exception e) {
            System.out.println("ERRORE: impossibile leggere il file prodotti.csv");
            return;
        }
        String[] righe = new String[righeTotali];
        try {
            BufferedReader br = new BufferedReader(new FileReader("../../dati/prodotti.csv"));
            for (int i = 0; i < righeTotali; i = i + 1) {
                righe[i] = br.readLine();
            }
            br.close();
        } catch (Exception e) {
            System.out.println("ERRORE: problema durante la lettura del file");
            return;
        }
        boolean trovato = false;
        for (int i = 0; i < righeTotali; i = i + 1) {
            String riga = righe[i];
            if (riga == null || riga.equals("")) {
            } else {
                String[] parti = riga.split(";");
                if (parti.length >= 4) {
                    String codice = parti[0];
                    String descrizione = parti[1];
                    int prezzo = 0;
                    int quantitaStock = 0;
                    try {prezzo = Integer.parseInt(parti[2]);
                        quantitaStock = Integer.parseInt(parti[3]);
                    } catch (Exception e) {
                        System.out.println("ERRORE: dati numerici non validi nel file");
                        return;
                    }
                    if (codice.equals(codiceCercato)) {
                        trovato = true;
                        if (quantitaVendere > quantitaStock) {
                            System.out.println("ERRORE: Stock insufficiente. Disponibili: " + quantitaStock);
                            return;
                        }
                        int nuovaQuantita = quantitaStock - quantitaVendere;
                        righe[i] = codice + ";" + descrizione + ";" + prezzo + ";" + nuovaQuantita;
                        try {
                            BufferedWriter bw = new BufferedWriter(new FileWriter("../../dati/prodotti.csv"));
                            for (int j = 0; j < righeTotali; j = j + 1) {
                                bw.write(righe[j]);
                                bw.newLine();
                            }
                            bw.close();
                        } catch (Exception e) {
                            System.out.println("ERRORE: impossibile scrivere il file aggiornato");
                            return;
                        }
                        System.out.println(descrizione + ";" + prezzo + ";" + quantitaVendere);
                        return;
                    }
                }
            }
        }
        if (trovato == false) {
            System.out.println("ERRORE: Prodotto con codice " + codiceCercato + " non trovato");
        }
    }
}
