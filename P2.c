//gcc P2.c -lfftw3 -lm -o Prob2.out
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <complex.h>
#include <fftw3.h>


int main()
{
  fftw_complex *y, *ky;
  fftw_plan p;
  int N = 1024;
  double x, k, c_fac; 
  double range[] = {-100, 100};
  double dx = (range[1] - range[0]) / (N-1);
  double dk = 1 / ((N-1) * dx);

  y = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);
  ky = (fftw_complex*) fftw_malloc(sizeof(fftw_complex) * N);

  for (int i = 0; i < N; i++) 
    {
      x = (i * dx) + range[0];
      if(x==0) y[i] = 1;
      else y[i] = sin(x)/x;
    }
  
  p = fftw_plan_dft_1d(N, y, ky, FFTW_FORWARD, FFTW_ESTIMATE);
  fftw_execute(p);
  
  c_fac = dx/sqrt(2*M_PI);
  double tmp;
  
  for (int i = 0; i < N/2; i++)
    {
      tmp = ky[i];
      ky[i] = ky[i + (N/2)];
      ky[i + (N/2)] = tmp;
    }
  
  FILE *fp;
  int st=remove("Prob2.csv");
  fp = fopen("Prob2.csv", "w+"); 
  fftw_complex p_fac;
  for(int i=0;i<N;i++)
    {
      k = 2*M_PI*((i - (N/2)) * dk);
      p_fac = cos( -1 * k * range[0]) + I * sin( -1 * k * range[0]);
      fprintf(fp, "%f,%f \n", k, c_fac*creal(ky[i]*p_fac));
    }
  
  fftw_destroy_plan(p);
  fftw_free(y); fftw_free(ky); fclose(fp);

  return(0);
}
