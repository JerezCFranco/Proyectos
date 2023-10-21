package Padawan_Jedi.Estudiante;

import java.util.LinkedList;
import java.util.Scanner;

/*App que permite agregar y/o eliminar un estudiante a una LinkedList, se agrega su nombre,
sus tres calificaciónes, puedes buscar al estudiante por su Id, donde se muestra su nombre
notas y promedio, tambien puedes acceder a una lista de todos los estudiantes registrados*/
public class App_estudiante {
    
    public static void main(String[] args){

        Scanner scan = new Scanner(System.in);
        LinkedList<LinkedList<Estudiante>> todos_estudiantes = new LinkedList<>();
        int id = 0;
        int continuar = 9;
        while (continuar!=0){
            LinkedList<Estudiante> elementos = new LinkedList<>();
            System.out.println("Bienvenido, que desea realizar? \n 1 - Agregar Estudiante \n 2 - Borrar Estudiante \n 3 - Buscar Estudiante \n 4 - Lista de Estudiantes \n 0 - Salir");
            continuar = scan.nextInt();
            System.out.println("\n");
            if(continuar==1){
                System.out.println("Ingrese el nombre del estudiante:");
                scan.nextLine();
                String nombre = scan.nextLine();             

                System.out.println("Ingrese la primera calificación del estudiante:");
                int cal1 = scan.nextInt();

                System.out.println("Ingrese la segunda calificación del estudiante:");
                int cal2 = scan.nextInt();

                System.out.println("Ingrese la tercera calificación del estudiante:");
                int cal3 = scan.nextInt();

                int calfin = (cal1+cal2+cal3)/3;
                id++;
                elementos.add(new Estudiante(nombre, id, cal1, cal2,cal3, calfin));
                
                todos_estudiantes.add(elementos);             
            }

            if(continuar==2){
                System.out.print("Ingrese la Id del estudiante a eliminar: ");
                int posicionAEliminar = scan.nextInt();

                if (posicionAEliminar >= 0 && posicionAEliminar < todos_estudiantes.size()) {
                    // Eliminar el elemento en la posición especificada
                    todos_estudiantes.remove(posicionAEliminar);
                }else{
                    System.out.println("La posicion ingresada es incorrecta, intente nuevamente.");
                }
            }

            if(continuar==3){
                // Acceder a la información de un contacto específico
                int indiceListaInterna = 0; // Cambia este índice según la lista interna que desees acceder
                System.out.println("Id del estudiante que desea buscar:");
                int indiceEstudiante = scan.nextInt();    // Cambia este índice según el contacto que desees acceder
            
                if (indiceListaInterna >= 0 && indiceListaInterna < todos_estudiantes.size()) {
                    LinkedList<Estudiante> listaEstudiantes = todos_estudiantes.get(indiceListaInterna);

                    if (indiceEstudiante >= 0 && indiceEstudiante < listaEstudiantes.size()) {
                        Estudiante estudiante = listaEstudiantes.get(indiceEstudiante);
                        System.out.println("Nombre del estudiante: " + estudiante.getNombre());
                        System.out.println("Primera calificación del estudiante: " + estudiante.getCal1());
                        System.out.println("Segunda calificación del estudiante: " + estudiante.getCal2());
                        System.out.println("Tercera calificación del estudiante: " + estudiante.getCal3());
                        System.out.println("Promedio de calificación del estudiante: " + estudiante.getCalfin());
                        System.out.println("La id del estudiante es: " + estudiante.getId());
                    } else {
                        System.out.println("Id de estudiante no válido.");
                    }
                } else {
            System.out.println("Id de lista interna no válido.");
                }

            }
            
            if(continuar==4){

                // Iterar y mostrar la lista de todos los contactos
                for (LinkedList<Estudiante> listaEstudiantes : todos_estudiantes) {
                    for (Estudiante estudiante : listaEstudiantes) {
                    System.out.println("Nombre del estudiante: " + estudiante.getNombre());
                    System.out.println("La Id del estudiante es: " + estudiante.getId()+"\n");
                    }
                }
            } 
        }scan.close();
    }
}