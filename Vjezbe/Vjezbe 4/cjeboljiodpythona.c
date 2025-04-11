#include <stdio.h>
#include <math.h>
#include <stdlib.h>

float domet(float);

float domet(float dt){
    float v0=10.;
    float fi=4*atan(1)/3.;
    float v[]={v0*cos(fi),v0*sin(fi)};
    float r[]={0.,0.};
    float g=-9.81;

    while (r[1]>=0){
        r[0]=r[0]+v[0]*dt;
        r[1]=r[1]+v[1]*dt;
        v[1]=v[1]+g*dt;
    }
    return r[0];
}

int main(void)
{

    double dt[300];
    double j=0.001;
    for (int i=0; i<300;i++)
    {
        dt[i]=j;
        //printf("%lf\n", j);
        j+=0.00033;
    }
    //printf("%lf", domet(0.01));
    double D = (100/9.81)*sin(4*atan(1)/3.);
    double pogreske[300];
    for(int i=0; i<sizeof(dt)/sizeof(double);i++){
    //printf("Test\n");
        pogreske[i]=fabs(domet(dt[i])-D)*100;
    }
    /*for(int i=0; i<300;i++)
    {
        printf("%lf\%\n", pogreske[i]);
    }*/

    FILE *gnuplotPipe = popen("gnuplot -persistent", "w");
    if (gnuplotPipe) {
        fprintf(gnuplotPipe, "set title 'Relativna pogreska'\n");
        fprintf(gnuplotPipe, "plot '-' with lines\n");

        // Send data points
        for (int i=0; i < 300; i++) {
            fprintf(gnuplotPipe, "%lf %lf\n", dt[i], pogreske[i]);
        }

        fprintf(gnuplotPipe, "e\n"); // End of data
        fflush(gnuplotPipe);         // Flush the pipe
        pclose(gnuplotPipe);         // Close pipe
    } else {
        printf("Error: Could not open pipe to gnuplot.\n");
    }

    return 0;
}
