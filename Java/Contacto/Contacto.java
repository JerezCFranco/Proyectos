package Java.Contacto;

public class Contacto {
    String nombre;
    String telefono;
    String correo;
    int posicion;

    public Contacto(String nombre, String telefono, String correo, int posicion) {
        this.nombre = nombre;
        this.telefono = telefono;
        this.correo = correo;
        this.posicion = posicion;
    }

    public String getNombre() {
        return nombre;
    }
    
    public String getTelefono() {
        return telefono;
    }

    public String getCorreo() {
        return correo;
    }

    public int getPosicion(){
        return posicion;
    }
}
