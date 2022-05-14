/*
** PoC-Skyfall, 2022
** TRANSLATE-ME
** File description:
** Convert binary into C code
*/

int increment(int value)
{
  return value + 42;
}

int main(void)
{
  int var;

  var = increment(1);
  return var + 4;
}
