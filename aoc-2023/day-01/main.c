#include <ctype.h>
#include <stdio.h>

#define ll long long
#define ar array

FILE *fptr;

int main(void) {

  int ans;
  char buffer[255];

  fptr = fopen("input.txt", "r");
  fgets(buffer, 255, fptr);

  for (int i = 0; buffer[i] != '\0'; i++) {
    if (isdigit(buffer[i])) {
      ans += (buffer[i] - '0');
    }
  }

  printf("%d", ans);

  fclose(fptr);

  return 0;
}
