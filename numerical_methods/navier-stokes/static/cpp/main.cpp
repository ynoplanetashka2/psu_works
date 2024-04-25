#include <stdio.h>
#include <iostream>

int main()
{
  int n = 51, m = 51, k = 0;
  float L = 1, H = 1, hx = L / n, hy = H / m, tay = 0.00001, tExit = 1, v = 1, w = 1, b = (hx * hx) / (hy * hy), eps = 0.001;
  float** fi,  **psi,  **psiLast;
  fi = new float* [n + 1];
  psi = new float* [n + 1];
  psiLast = new float* [n + 1];
  for (int i = 0; i < n + 1; i++) {
    fi[i] = new float[m + 1];
    psi[i] = new float[m + 1];
    psiLast[i] = new float[m + 1];
  }
  for (int i = 0; i < n + 1; i++) {
    for (int j = 0; j < m + 1; j++) {
      fi[i][j] = 0;
      psi[i][j] = 0;
    }
  }
  fi[5][5] = 0.0001;

  for (float tCycle = 0; tCycle < tExit; tCycle += tay) {

    for (int i = 1; i < n; i++) {
      for (int j = 1; j < m; j++) {
        fi[i][j] = fi[i][j] + tay * ((fi[i + 1][j] - 2 * fi[i][j] + fi[i - 1][j]) / (hx * hx) + (fi[i][j + 1] - 2 * fi[i][j] + fi[i][j - 1]) / (hy * hy) - ((psi[i][j + 1] - psi[i][j - 1]) / (2 * hy)) * ((fi[i + 1][j] - fi[i - 1][j]) / (2 * hx)) + ((psi[i + 1][j] - psi[i - 1][j]) / (2 * hx)) * ((fi[i][j + 1] - fi[i][j - 1]) / (2 * hy)));
      }
    }

    do {
      k = 0;
      for (int i = 0; i < n + 1; i++) {
        for (int j = 0; j < m + 1; j++) {
          psiLast[i][j] = psi[i][j];
        }
      }
      for (int i = 1; i < n; i++) {
        for (int j = 1; j < m; j++) {
          psi[i][j] = psi[i][j] + (w / (2 * (1 + b))) * (psi[i + 1][j] + psi[i - 1][j] + b * psi[i][j + 1] + b * psi[i][j - 1]- hx * hx * fi[i][j]) - w * psi[i][j];
        }
      }
      for (int i = 0; i < n + 1; i++) {
        for (int j = 0; j < m + 1; j++) {
          if ((abs(psi[i][j] - psiLast[i][j])) < eps) {
            k++;
          }
        }
      }
    } while (k != ((n + 1) * (m + 1)));

    for (int i = 0; i < n + 1; i++) {
      fi[i][m] = 2 * psi[i][m - 1] / (hy * hy) - 2 * v / hy;
      fi[i][0] = 2 * psi[i][1] / (hy * hy);
    }
    for (int j = 0; j < m + 1; j++) {
      fi[0][j] = 2 * psi[1][j] / (hx * hx);
      fi[n][j] = 2 * psi[n - 1][j] / (hx * hx);
    }

  }

  FILE* f;
  FILE* fff;
  f = fopen("./Flow1.txt", "a");
  fff = fopen("./Flow2.txt", "a");
  for (int i = 0; i < n + 1; i++) {
    for (int j = 0; j < m + 1; j++) {
      fprintf(f, "%f  %f  %f\n", i * hx, j * hy, fi[i][j]);
      fprintf(fff, "%f  %f  %f\n", i * hx, j * hy, psi[i][j]);
    }
  }
  fclose(f);
  fclose(fff);

  for (int i = 0; i < n + 1; i++) {
    delete[]fi[i];
    delete[]psi[i];
    delete[]psiLast[i];
  }
  delete[]fi;
  delete[]psi;
  delete[]psiLast;
}