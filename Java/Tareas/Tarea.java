package Padawan_Jedi.Tareas;

import java.util.List;

public class Tarea {
    String titulo;
    String descripcion;
    String vencimiento;
    List<String> tareas;
    public Tarea(List<String> tareas){
        this.tareas = tareas;
    }

    public List<String> getTarea() {
        return tareas;
    }
}
