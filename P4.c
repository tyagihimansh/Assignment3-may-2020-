// gcc P4.c -lfftw3 -lm -o Prob4.out

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include <fftw3.h>

int main()
{
  fftw_complex *y, *ky;
  fftw_plan p;
  int N = 256;
  double x, c_factor; 
  double range[] = {-20, 20};
  double dx = (range[1] - range[0]) / (N-1);
  double dk = 1 / ((N-1) * dx);
  y = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
  ky = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
  double *act_sol = (double*) malloc(sizeof(double) * N);
  double *k = (double*) malloc(sizeof(double) * N);
     
  for (int i=0; i<N; i++)
    {
      x = (i*dx) + range[0];
      y[i] = exp( -1 * x * x);
    }
    
  p = fftw_plan_dft_1d(N, y, ky, FFTW_FORWARD, FFTW_ESTIMATE);
  fftw_execute(p); 

  fftw_complex tmp;
  for (int i = 0; i < N/2; i++)
    {
      tmp = ky[i];
      ky[i] = ky[i + (N/2)];
      ky[i + (N/2)] = tmp;
    }

  for (int i = 0; i < N; i++)
    {
      k[i] = 2*M_PI*((i - (N/2)) * dk);
      act_sol[i] = exp(-0.25 * k[i] * k[i]) / sqrt(2);
    }

  c_factor = dx/sqrt(2*M_PI);
  FILE *fp;
  int st=remove("Prob4.csv");
  fp = fopen("Prob4.csv", "w+"); 
  fftw_complex p_fac;
  for(int i=0;i<N;i++)
    {
      p_fac = cos( -1 * k[i] * range[0]) + I * sin( -1 * k[i] * range[0]);
      fprintf(fp, "%f,%f,%f \n", k[i], c_factor*creal(ky[i]*p_fac), act_sol[i]);
    }
  
  fftw_destroy_plan(p);
  fftw_free(y); fftw_free(ky); free(k); fclose(fp);

  return(0);
}
