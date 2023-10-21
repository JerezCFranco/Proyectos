package Proyectos.Java.Estudiante;

public class Estudiante {
    
    String nombre;
    int id;
    int cal1;
    int cal2;
    int cal3;
    int calfin;

    public Estudiante(String nombre, int id, int cal1, int cal2, int cal3, int calfin){
        this.nombre = nombre;
        this.id = id;
        this.cal1 = cal1;
        this.cal2 = cal2;
        this.cal3 = cal3;
        this.calfin = calfin;
    }

    public String getNombre(){
        return nombre;
    }

    public int getId(){
        return id;
    }

    public int getCal1(){
        return cal1;
    }

    public int getCal2(){
        return cal2;
    }

    public int getCal3(){
        return cal3;
    }

    public int getCalfin(){
        return calfin;
    }

}
