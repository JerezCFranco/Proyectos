package Java.Contacto;
import java.util.Scanner;
import java.util.LinkedList;

/*App que permite registrar y/o eliminar contactos a una LinkedList, se agrega su nombre, teléfono
y correo, puedes buscar el contacto según su posición
y puedes ver la lista completa de contactos.*/

public class App_contacto {
    
    public static void main(String[] args){

        Scanner scan = new Scanner(System.in);
        LinkedList<LinkedList<Contacto>> todos_contactos = new LinkedList<>();
        int posicion = 0;
        int continuar = 9;
        while (continuar!=0){
            LinkedList<Contacto> elementos = new LinkedList<>();
            System.out.println("Bienvenido, que desea realizar? \n 1 - Agregar Contacto \n 2 - Borrar Contacto \n 3 - Buscar Contacto \n 4 - Lista de Contactos \n 0 - Salir");
            continuar = scan.nextInt();
            System.out.println("\n");
            if(continuar==1){
                System.out.println("Ingrese el nombre del contacto:");
                scan.nextLine();
                String nombre = scan.nextLine();             

                System.out.println("Ingrese el teléfono del contacto:");
                String telefono = scan.nextLine();

                System.out.println("Ingrese el correo del contacto:");
                String correo = scan.nextLine();
                
                elementos.add(new Contacto(nombre, telefono, correo, posicion));
                posicion++;
                todos_contactos.add(elementos);             
            }

            if(continuar==2){
                System.out.print("Ingrese la posición del contacto a eliminar: ");
                int posicionAEliminar = scan.nextInt();

                if (posicionAEliminar >= 0 && posicionAEliminar < todos_contactos.size()) {
                    // Eliminar el elemento en la posición especificada
                    todos_contactos.remove(posicionAEliminar);
                }else{
                    System.out.println("La posicion ingresada es incorrecta, intente nuevamente.");
                }
            }

            if(continuar==3){
                // Acceder a la información de un contacto específico
                int indiceListaInterna = 0; // Cambia este índice según la lista interna que desees acceder
                System.out.println("Indique el contacto que desea buscar:");
                int indiceContacto = scan.nextInt();    // Cambia este índice según el contacto que desees acceder
            
                if (indiceListaInterna >= 0 && indiceListaInterna < todos_contactos.size()) {
                    LinkedList<Contacto> listaContactos = todos_contactos.get(indiceListaInterna);

                    if (indiceContacto >= 0 && indiceContacto < listaContactos.size()) {
                        Contacto contacto = listaContactos.get(indiceContacto);
                        System.out.println("Nombre del contacto: " + contacto.getNombre());
                        System.out.println("Teléfono del contacto: " + contacto.getTelefono());
                        System.out.println("La posición de este contacto es de: " + contacto.getPosicion());
                    } else {
                        System.out.println("Índice de contacto no válido.");
                    }
                } else {
            System.out.println("Índice de lista interna no válido.");
                }

            }
            
            if(continuar==4){

                // Iterar y mostrar la lista de todos los contactos
                for (LinkedList<Contacto> listaContactos : todos_contactos) {
                    for (Contacto contacto : listaContactos) {
                    System.out.println("Nombre del contacto: " + contacto.getNombre());
                    System.out.println("Teléfono del contacto: " + contacto.getTelefono());
                    System.out.println("Correo del contacto: " + contacto.getCorreo());
                    System.out.println("La posición de este contacto es de: " + contacto.getPosicion()+"\n");
                    }
                }
            }   
        }scan.close();
    }
}
