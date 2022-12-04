#include <stdio.h>
#include <stdlib.h>

int main(void) {
  char line[20];
  int count = 0;
  while(fgets(line, sizeof(line)-1, stdin)) {
    int s1, e1, s2, e2;
    sscanf(line, "%d-%d,%d-%d", &s1, &e1, &s2, &e2);
    count += (e1 >= s2) && (e2 >= s1);
  }
  printf("%d\n", count);
}
