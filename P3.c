// gcc P3.c -lgsl -lgslcblas -lm -o Prob3.out

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <gsl/gsl_errno.h>
#include <gsl/gsl_fft_complex.h>

#define REAL(z, i) ((z)[2 * (i)])
#define IMAG(z, i) ((z)[2 * (i) + 1])


int main()
{
  gsl_fft_complex_wavetable * wavetable;
  gsl_fft_complex_workspace * workspace;
  double *y;
  int N = 1024;
  double x, k, c_fac; 
  double range[] = {-100, 100};
  double dx = (range[1] - range[0]) / (N-1);
  double dk = 1 / ((N-1) * dx);
  y = (double*) malloc(sizeof(double) * 2 * N);;


  for (int i=0; i<N; i++) 
    {
      x = (i * dx) + range[0];
      if(x==0) REAL(y,i) = 1;
      else REAL(y, i) = sin(x) / x;
    }

  wavetable = gsl_fft_complex_wavetable_alloc (N);
  workspace = gsl_fft_complex_workspace_alloc (N);
  gsl_fft_complex_forward (y, 1, N, wavetable, workspace);

  double tmp;
  for (int i = 0; i < N/2; i++)      
    {
      tmp = REAL(y,i);
      REAL(y,i) = REAL(y,i + (N/2));
      REAL(y,i + (N/2)) = tmp;
      tmp = IMAG(y,i);
      IMAG(y,i) = IMAG(y,i + (N/2));
      IMAG(y,i + (N/2)) = tmp;
    }
  
  FILE *fp;
  int st=remove("csv.Prob3");
  fp = fopen("Prob3.csv", "w+");
  
  c_fac = dx/sqrt(2*M_PI);
  double ky;
  for(int i=0;i<N;i++)
    {
      k = 2*M_PI*((i - (N/2)) * dk);
      ky = (REAL(y,i)*cos(-1*k*range[0])) - (IMAG(y,i)*sin(-1*k*range[0]));
      fprintf(fp, "%f,%f \n", k, c_fac*ky);
    }
  
  free(y); fclose(fp);
  gsl_fft_complex_wavetable_free (wavetable);
  gsl_fft_complex_workspace_free (workspace);

  return(0);
}
