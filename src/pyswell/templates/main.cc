
#include <iostream>
#include <functional>

auto main() -> int
{

  // Create a reference wrapper to std::cout,
  // capture it in a lambda that takes no parameters.
  // In the lambda body, dereference the captured reference wraper
  // pass a string to write out, and finally call this lambda.
  [out = std::ref(std::cout << "\n\t\t")]()
  {
    out.get() << "All is swell!\n" << std::endl;
  }();

}
