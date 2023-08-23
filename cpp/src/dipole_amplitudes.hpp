#include <string>

#ifndef _DIPOLE_AMPLITUDES_H
#define _DIPOLE_AMPLITUDES_H

void initialize_amplitude(std::string file);
double check_Y(double Y);
double N_xy(double r, double delta, double Y);
double N_xyz(double r10, double r20, double r21, double delta, double Y);
double S_xy(double r, double Y);
double S_xyz(double r10, double r20, double r21, double Y);

double dNdY(double r, double delta, double Y);

double S_file(double r, double Y);
double S_GBW(double r, double Y);


double Qs2_GBW(double x);

#endif