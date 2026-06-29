#include <stdio.h>
int evaluacionNota(double calificacion) {

    if(calificacion > 7){
        printf("Aprobado");
    }
    else if(calificacion > 0){
        printf("Reprobado");
    }
    return 0;
}