package Java.Tareas;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*App que permite registrar tareas y/o eliminarlas en una lista, se agrega el título, descripcion
y fecha de vencimiento de la tarea, y se puede visualizar todas las tareas registradas
en la lista con sus datos*/

public class App_tareas {
    
    public static void main(String[] args){
    
        Scanner scan = new Scanner(System.in);
        List<List<String>> todas_tareas = new ArrayList<>();
        int posicion = 0;
        int continuar = 9;
        while (continuar!=0){
            List<String> elementos = new ArrayList<>();
            System.out.println("Bienvenido, que desea realizar? \n 1 - Crear Tarea \n 2 - Borrar Tarea \n 3 - Ver Lista\n 0 - Salir");
            continuar = scan.nextInt();
            System.out.println("\n");
            if(continuar==1){
                Tarea tarea = new Tarea(elementos);
                System.out.println("Agrege el Titulo de la Tarea:");
                scan.nextLine();
                tarea.titulo = scan.nextLine();          
                elementos.add(tarea.titulo);

                System.out.println("Agrege la descripción de la Tarea:");
                tarea.descripcion = scan.nextLine();
                elementos.add(tarea.descripcion);

                System.out.println("Agrege la fecha de vencimiento de la Tarea en formato dd/mm/aa:");
                tarea.vencimiento = scan.nextLine();
                elementos.add(tarea.vencimiento);

                elementos.add(String.valueOf("La posicion de la tarea es:"+posicion+"\n"));

                //tarea.agregarTarea(tarea.titulo, tarea.descripcion, tarea.vencimiento);
                todas_tareas.add(elementos);
                posicion++;
            }
            if(continuar==2){
                System.out.print("Ingrese la posición del elemento a eliminar: ");
                int posicionAEliminar = scan.nextInt();

                if (posicionAEliminar >= 0 && posicionAEliminar < todas_tareas.size()) {
                    // Eliminar el elemento en la posición especificada
                    todas_tareas.remove(posicionAEliminar);
                }else{
                    System.out.println("La posicion ingresada es incorrecta, intente nuevamente.");
                }
            }
            if(continuar==3){
                for (List<String> listaInterna : todas_tareas) {
                    for (String elemento : listaInterna){
                        System.out.println(elemento);
                    }
                }
            
            }    
        }   scan.close();
    }
}
