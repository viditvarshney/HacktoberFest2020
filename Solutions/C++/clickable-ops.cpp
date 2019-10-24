#include <iostream>

template <int N, int From, int To, int Using>
class HanoiSolver
{
public:
static void solve()
{
HanoiSolver<N-1, From, Using, To>::solve();
std::cout << "Move " << From << " to " << To << std::endl;
HanoiSolver<N-1, Using, To, From>::solve();
}
};

template <int From, int To, int Using>
class HanoiSolver<0, From, To, Using>
{
public:
static void solve()
{
}
};

int main()
{
HanoiSolver<10, 1, 2, 3>::solve();
}
